"""Install / update downloadable packs — pure core, shared by desktop (Qt) and
mobile (Toga/WebView).

The UIs only fetch + render + collect choices; **all install/update logic lives
here** so the two front-ends stay thin and behave identically. A UI typically:

    base, entries = pack_repo.fetch_index()              # off the UI thread
    toml, sig = pack_repo.fetch_pack_files(entry, base)  # off the UI thread
    manifest, buttons = pack_format.parse_pack(toml)
    verified = pack_format.verify_signature(toml, sig) if sig else False
    # show command preview + (Pro) machine picker; Local is free, SSH = Pro
    install_pack(config, manifest, buttons, machine_ids, category, mode)

Gating (decided 2026-06-15, "option 1"): installing is free; the SSH/remote target
is the Pro boundary — enforced by the UI/machine layer, not here.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import tomli_w

from commandeck_core.i18n import _
from commandeck_core.models.command_button import CommandButton
from commandeck_core.models.pack_format import PackManifest, PACK_FORMAT_VERSION


def existing_pack_buttons(config, pack_id: str) -> list[CommandButton]:
    """Installed buttons from this pack — bare ``pack_id`` and ``pack_id#N`` duplicates."""
    return [b for b in config.load_buttons()
            if b.source_pack == pack_id or b.source_pack.startswith(pack_id + "#")]


def next_duplicate_marker(config, pack_id: str) -> str:
    """Next free ``pack_id#N`` (the first install is the bare id, the second is #2)."""
    markers = {b.source_pack for b in existing_pack_buttons(config, pack_id)}
    max_n = 1
    for m in markers:
        mm = re.match(rf"^{re.escape(pack_id)}#(\d+)$", m)
        if mm:
            max_n = max(max_n, int(mm.group(1)))
    return f"{pack_id}#{max_n + 1}"


def install_pack(config, manifest: PackManifest, buttons: list[CommandButton],
                 machine_ids: list[str], category: str | None = None,
                 mode: str = "auto") -> list[CommandButton]:
    """Install parsed pack ``buttons`` onto ``machine_ids``.

    ``mode``: ``"first"`` | ``"replace"`` (drop the pack's existing buttons first) |
    ``"duplicate"`` (add a numbered second copy) | ``"auto"`` (replace if already
    installed, else first). ``category`` overrides the pack's category for all
    buttons; ``None`` keeps each button's own/manifest category. Records the pack
    version (for "update available"). Returns the installed buttons."""
    pack_id = manifest.pack_id
    existing = existing_pack_buttons(config, pack_id)
    if mode == "auto":
        mode = "replace" if existing else "first"

    if mode == "replace":
        for b in existing:
            config.delete_button(b.id)
        marker = pack_id
    elif mode == "duplicate":
        marker = next_duplicate_marker(config, pack_id)
        mm = re.match(r"^.*#(\d+)$", marker)
        n = mm.group(1) if mm else "2"
    else:  # first
        marker = pack_id

    installed: list[CommandButton] = []
    for b in buttons:
        b.machine_ids = list(machine_ids)
        b.source_pack = marker
        b.pack_base_command = b.command  # baseline for "user edited?" on a later update
        if category is not None:
            b.category = category
        if mode == "duplicate":
            b.category = f"{b.category} ({n})"
        config.add_button(b)
        installed.append(b)

    config.record_installed_pack(pack_id, manifest.pack_ver)
    return installed


def installed_pack_ids(config) -> set[str]:
    """Pack ids that currently have buttons present (the authoritative "installed"
    signal for the gallery). Derived from the buttons themselves — not the recorded
    versions in installed_packs.toml — so a stale record (e.g. left after a reset)
    never makes an absent pack look installed. ``pack_id#N`` duplicates count as the
    bare pack_id."""
    ids: set[str] = set()
    for b in config.load_buttons():
        if b.source_pack:
            ids.add(b.source_pack.split("#", 1)[0])
    return ids


def uninstall_pack(config, pack_id: str) -> int:
    """Remove every button installed from this pack (bare ``pack_id`` and ``pack_id#N``
    duplicates) and forget its recorded version. Returns the count of deleted buttons."""
    buttons = existing_pack_buttons(config, pack_id)
    for b in buttons:
        config.delete_button(b.id)
    config.remove_installed_pack(pack_id)
    return len(buttons)


# Pack-defined fields refreshed on update (everything EXCEPT command — command is
# handled separately so a user edit can be preserved). machine_ids/category/position/
# id/source_pack/pack_button_id are the user's usage and are always preserved.
def _refresh_pack_fields(cur: CommandButton, nb: CommandButton) -> None:
    cur.name = nb.name
    cur.icon_name = nb.icon_name
    cur.color = nb.color
    cur.text_color = nb.text_color
    cur.tooltip = nb.tooltip
    cur.confirm_before_run = nb.confirm_before_run
    cur.show_output = nb.show_output
    cur.execution_mode = nb.execution_mode
    cur.timeout = nb.timeout
    cur.run_as_user = nb.run_as_user
    cur.os = nb.os


def plan_pack_update(config, manifest: PackManifest, new_buttons: list[CommandButton]):
    """Diff a freshly-parsed pack against what's installed, matched by stable
    ``pack_button_id``. Returns ``(to_refresh, to_add, removed, to_conflict)``:

      * ``to_refresh`` — ``(old, new)`` pairs that can be updated silently. A button
        the user never edited (``old.command == old.pack_base_command``), or one
        whose command the pack didn't change (``new.command == old.pack_base_command``),
        or a legacy button with no recorded baseline (``pack_base_command == ""``).
      * ``to_add`` — buttons new in this pack version.
      * ``removed`` — installed buttons no longer in the pack.
      * ``to_conflict`` — ``(old, new)`` pairs where the user edited the command AND
        the pack also changed it (both differ from the baseline) → needs the user to
        pick Overwrite vs Duplicate (``resolve_conflict``).

    Pure read — writes nothing."""
    existing = existing_pack_buttons(config, manifest.pack_id)
    by_stable = {b.pack_button_id: b for b in existing if b.pack_button_id}
    seen: set[str] = set()
    to_refresh, to_add, to_conflict = [], [], []
    for nb in new_buttons:
        seen.add(nb.pack_button_id)
        old = by_stable.get(nb.pack_button_id)
        if old is None:
            to_add.append(nb)
            continue
        base = old.pack_base_command
        user_edited = bool(base) and old.command != base
        pack_changed = bool(base) and nb.command != base
        if user_edited and pack_changed:
            to_conflict.append((old, nb))
        else:
            to_refresh.append((old, nb))
    removed = [b for b in existing if b.pack_button_id and b.pack_button_id not in seen]
    return to_refresh, to_add, removed, to_conflict


def apply_pack_update(config, manifest: PackManifest, new_buttons: list[CommandButton],
                      delete_removed: bool = False) -> dict:
    """Update an installed pack in place, applying the silent refreshes and additions.

    Matched buttons keep the user's **machine targets, category, grid position and
    runtime id**; the pack-defined fields are refreshed. The command is taken from
    the new pack **only when the pack actually changed it** — a command the user
    edited but the pack left alone is preserved. New buttons are added with the same
    targets/category/marker as the existing set; removed buttons are deleted only when
    ``delete_removed``.

    Returns a summary dict. ``conflicts`` is the list of unresolved ``(old, new)``
    pairs (user edited the command AND the pack changed it) for the UI to resolve via
    :func:`resolve_conflict`; they are left untouched here."""
    to_refresh, to_add, removed, to_conflict = plan_pack_update(config, manifest, new_buttons)
    existing = existing_pack_buttons(config, manifest.pack_id)
    ref = existing[0] if existing else None
    marker = ref.source_pack if ref else manifest.pack_id
    category = ref.category if ref else manifest.category
    machine_ids = list(ref.machine_ids) if ref else []

    buttons = config.load_buttons()
    by_id = {b.id: b for b in buttons}
    for old, nb in to_refresh:
        cur = by_id.get(old.id)
        if cur is None:
            continue
        _refresh_pack_fields(cur, nb)
        base = cur.pack_base_command
        # Take the pack's command unless the user edited it while the pack didn't
        # change it (base set, new == base, current != base → keep the user's).
        if not base or nb.command != base:
            cur.command = nb.command
        cur.pack_base_command = nb.command  # new baseline
    config.save_buttons(buttons)

    for nb in to_add:
        nb.machine_ids = list(machine_ids)
        nb.category = category
        nb.source_pack = marker
        nb.pack_base_command = nb.command
        config.add_button(nb)

    deleted = 0
    if delete_removed:
        for b in removed:
            config.delete_button(b.id)
            deleted += 1

    config.record_installed_pack(manifest.pack_id, manifest.pack_ver)
    return {"updated": len(to_refresh), "added": len(to_add),
            "removed": len(removed), "deleted": deleted, "conflicts": to_conflict}


def resolve_conflict(config, old: CommandButton, new: CommandButton, choice: str) -> None:
    """Resolve one update conflict (the user edited the command, the pack changed it).

    ``choice``:
      * ``"overwrite"`` — adopt the pack's new button (command + all pack fields),
        discarding the user's edit; the new command becomes the baseline.
      * ``"duplicate"`` — keep the user's edited button as a standalone custom button
        (detached from the pack) AND add the pack's new button alongside it.
    """
    buttons = config.load_buttons()
    cur = next((b for b in buttons if b.id == old.id), None)
    if cur is None:
        return
    if choice == "overwrite":
        _refresh_pack_fields(cur, new)
        cur.command = new.command
        cur.pack_base_command = new.command
        config.save_buttons(buttons)
    elif choice == "duplicate":
        # Detach the user's edited copy → a plain custom button.
        cur.source_pack = ""
        cur.pack_button_id = ""
        cur.pack_base_command = ""
        cur.is_default = False
        config.save_buttons(buttons)
        # Add the pack's new button with the same targets/category/marker.
        new.machine_ids = list(old.machine_ids)
        new.category = old.category
        new.source_pack = old.source_pack
        new.pack_base_command = new.command
        config.add_button(new)


def updates_available(config, index_entries) -> list[str]:
    """pack_ids whose installed version differs from the repo index (→ update offer).
    ``index_entries`` = objects exposing ``pack_id`` and ``pack_ver``."""
    installed = config.get_installed_packs()
    out = []
    for e in index_entries:
        cur = installed.get(e.pack_id)
        if cur is not None and cur != e.pack_ver:
            out.append(e.pack_id)
    return out


# ── Batch install / update orchestration (shared by desktop Qt + mobile WebView) ──
# The UIs only fetch packs (pack_repo.fetch_packs), render, collect the machine target,
# and resolve conflicts. Partitioning + applying live here so both front-ends behave
# identically and never drift.
@dataclass
class BatchPlan:
    """How a set of selected packs splits for a batch action. ``to_update`` /
    ``to_install`` hold index entries (objects with ``.pack_id``); ``skipped`` is
    ``[(entry, reason)]`` for packs that can't be acted on (unsigned / failed to load)."""
    to_update: list
    to_install: list
    skipped: list


def plan_batch(config, entries, cache) -> BatchPlan:
    """Partition ``entries`` for a batch install/update using ``cache``
    (``{pack_id: (manifest, buttons, verified)}`` from pack_repo.fetch_packs / preview).

    Only signature-verified packs are actionable — same gate as a single install:
      * not in cache → skipped (couldn't load);
      * cached but unsigned → skipped (refused);
      * verified + already installed → ``to_update``;
      * verified + not installed → ``to_install``."""
    installed = installed_pack_ids(config)
    to_update, to_install, skipped = [], [], []
    for e in entries:
        c = cache.get(e.pack_id)
        if c is None:
            skipped.append((e, _("couldn't be loaded")))
        elif not c[2]:
            skipped.append((e, _("not signed by Commandeck")))
        elif e.pack_id in installed:
            to_update.append(e)
        else:
            to_install.append(e)
    return BatchPlan(to_update, to_install, skipped)


def apply_batch(config, plan: BatchPlan, cache, machine_ids: list[str]) -> dict:
    """Apply a :class:`BatchPlan`: update the installed packs in place (preserving their
    own targets) then install the fresh ones onto ``machine_ids`` (each pack keeps its
    own category). Updates run before installs, matching the single-pack flows.

    Returns ``{"added", "updated", "conflicts"}`` where ``conflicts`` is
    ``[(manifest, [(old, new)])]`` — unresolved per-pack edit/pack conflicts for the UI
    to resolve via :func:`resolve_conflict` (same contract as :func:`apply_pack_update`)."""
    added = updated = 0
    conflicts: list = []
    for e in plan.to_update:
        manifest, buttons, _v = cache[e.pack_id]
        summary = apply_pack_update(config, manifest, buttons)
        updated += summary["updated"] + summary["added"]
        if summary["conflicts"]:
            conflicts.append((manifest, summary["conflicts"]))
            updated += len(summary["conflicts"])
    for e in plan.to_install:
        manifest, buttons, _v = cache[e.pack_id]
        done = install_pack(config, manifest, buttons, machine_ids, None, "first")
        added += len(done)
    return {"added": added, "updated": updated, "conflicts": conflicts}


def summarize_batch(added: int, updated: int) -> str:
    """One-line i18n summary of a batch result (shared toast/result text)."""
    if added and updated:
        return _("Installed {a} and updated {u} buttons").format(a=added, u=updated)
    if added:
        return _("Installed {n} buttons").format(n=added)
    if updated:
        return _("Updated {n} buttons").format(n=updated)
    return _("No changes")


# ── Export (the inverse of pack_format.parse_pack) ───────────────────────────────
def _slug(name: str, taken: set[str]) -> str:
    """A stable, file-safe button id from a name, unique within the pack."""
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "btn"
    sid, n = base, 2
    while sid in taken:
        sid, n = f"{base}-{n}", n + 1
    taken.add(sid)
    return sid


def serialize_pack(meta: dict, buttons: list[CommandButton]) -> bytes:
    """Serialise ``buttons`` into shareable ``pack.toml`` bytes (a community pack —
    UNSIGNED; only the maintainer signs official packs). Inverse of
    ``pack_format.parse_pack``: keeps only the pack-relevant fields and strips
    everything install-/machine-/secret-specific so the file is generic and PII-free.

    ``meta`` keys: pack_id, name, pack_ver, os, category, description, tags (list).
    """
    pack = {
        "pack_id": meta.get("pack_id", "").strip(),
        "name": meta.get("name", "").strip(),
        "pack_ver": meta.get("pack_ver", "1.0.0").strip() or "1.0.0",
        "os": meta.get("os", ""),
        "category": meta.get("category", ""),
        "description": meta.get("description", ""),
        "tags": list(meta.get("tags", [])),
    }
    pack_os, pack_cat = pack["os"], pack["category"]
    taken: set[str] = set()
    entries = []
    for b in buttons:
        sid = (b.pack_button_id or "").strip() or _slug(b.name, taken)
        if b.pack_button_id:
            taken.add(sid)
        e: dict = {"id": sid, "name": b.name, "command": b.command}
        # Keep only meaningful, non-default fields (mirrors the hand-authored packs).
        if b.icon_name:
            e["icon_name"] = b.icon_name
        if b.color:
            e["color"] = b.color
        if b.text_color:
            e["text_color"] = b.text_color
        if b.tooltip:
            e["tooltip"] = b.tooltip
        if b.show_output:
            e["show_output"] = True
        if b.confirm_before_run:
            e["confirm_before_run"] = True
        if b.hide_label:
            e["hide_label"] = True
        if b.hide_icon:
            e["hide_icon"] = True
        if b.execution_mode:
            e["execution_mode"] = b.execution_mode
        if b.os and b.os != pack_os:
            e["os"] = b.os
        if b.category and b.category != pack_cat:
            e["category"] = b.category
        # Stripped on purpose: machine_ids, profile_id, run_as_user, sudo secrets,
        # position, is_default, source_pack, mcp_executable.
        entries.append(e)
    data = {"version": PACK_FORMAT_VERSION, "pack": pack, "button": entries}
    return tomli_w.dumps(data).encode("utf-8")
