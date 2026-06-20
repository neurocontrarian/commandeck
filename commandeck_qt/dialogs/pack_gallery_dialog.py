"""Browse + install downloadable button packs (the gallery).

Thin Qt front-end over the shared core: `commandeck_core.services.pack_repo`
(fetch index + files) + `pack_format` (parse + verify) + `pack_service`
(install/update). The mobile screen reuses the same core calls.

Gating (option 1, 2026-06-15): opening + installing is FREE; the machine picker
only offers Local for a free user (no configured machines), and a trial nudge
points at the Pro/SSH value. The remote target is the Pro boundary, enforced
structurally (free builds have no machines), not by blocking this dialog.
"""
from __future__ import annotations

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QTreeWidget, QTreeWidgetItem,
    QTextEdit, QPushButton, QDialogButtonBox, QCheckBox, QScrollArea, QWidget,
    QLineEdit, QMessageBox, QSplitter,
)

from commandeck_core.i18n import _
from commandeck_core.models.config import ConfigManager
from commandeck_core.models import pack_format as pf
from commandeck_core.services import pack_repo, pack_service
from commandeck_core.utils.threading import run_in_thread


def _host_os() -> str:
    p = sys.platform.lower()
    if p.startswith("win"):
        return "windows"
    if p.startswith(("darwin", "mac")):
        return "macos"
    return "linux"


# Gallery is grouped under OS section headers so packs that share a name across
# OSes (e.g. "Hardware" for linux/macos/windows) are never ambiguous. Ordering lives
# in the shared core (pack_repo.group_by_os); the UI only maps os → a label.
def _os_label(os: str) -> str:
    return {"linux": _("Linux"), "macos": _("macOS"), "windows": _("Windows"),
            "": _("Cross-platform")}.get(os, os)


def show_pack_gallery_dialog(config: ConfigManager, parent=None) -> bool:
    """Modal. Returns True if at least one pack was installed/updated."""
    # The dialog is built parentless (see _GalleryDialog): a modal dialog with a
    # transient parent gets glued to the main window on GNOME/Wayland ("attached
    # modal dialog"). Parentless → floats as its own window, still modal via exec().
    # `parent` is kept only as the main-window handle for post-install refresh.
    dlg = _GalleryDialog(config, main_window=parent)
    dlg.exec()
    return dlg.changed


class _GalleryDialog(QDialog):
    def __init__(self, config: ConfigManager, main_window=None):
        super().__init__(None)
        # Main window kept for grid refresh / toast — NOT used as the Qt parent
        # (parentless = floats instead of gluing to it on GNOME/Wayland).
        self._main = main_window
        self._config = config
        self._host_os = _host_os()
        self._base_url = pack_repo.DEFAULT_BASE_URL
        self._entries: list[pack_repo.PackEntry] = []
        self._updates: set[str] = set()
        # Fetched pack files cached by pack_id (PackEntry is frozen — can't attach).
        self._cache: dict[str, tuple] = {}
        self.changed = False

        self.setWindowTitle(_("Button Pack Gallery"))
        self.setMinimumSize(720, 460)
        self._build_ui()
        self._load_index()

    def _build_ui(self):
        vbox = QVBoxLayout(self)
        self._status = QLabel(_("Loading packs…"))
        self._status.setStyleSheet("color: palette(mid);")
        vbox.addWidget(self._status)

        split = QSplitter(Qt.Horizontal)
        self._tree = QTreeWidget()
        self._tree.setHeaderHidden(True)
        self._tree.currentItemChanged.connect(self._on_select)
        # Tick boxes select several packs for one batch action; the highlighted row
        # still drives the preview. itemChanged fires on every check toggle.
        self._tree.itemChanged.connect(self._on_item_changed)
        split.addWidget(self._tree)

        right = QWidget()
        rv = QVBoxLayout(right)
        self._title = QLabel()
        self._title.setStyleSheet("font-weight: bold; font-size: 14px;")
        self._title.setWordWrap(True)
        self._meta = QLabel()
        self._meta.setWordWrap(True)
        self._meta.setStyleSheet("color: palette(mid);")
        rv.addWidget(self._title)
        rv.addWidget(self._meta)
        rv.addWidget(QLabel(_("Commands this pack will create:")))
        self._preview = QTextEdit()
        self._preview.setReadOnly(True)
        rv.addWidget(self._preview, 1)
        split.addWidget(right)
        split.setSizes([260, 460])
        vbox.addWidget(split, 1)

        hint = QLabel(_("Tip: tick several packs to install, update or remove them together."))
        hint.setWordWrap(True)
        hint.setStyleSheet("color: palette(mid); font-style: italic;")
        vbox.addWidget(hint)

        bb = QDialogButtonBox()
        self._install_btn = bb.addButton(_("Install…"), QDialogButtonBox.AcceptRole)
        self._install_btn.setEnabled(False)
        self._install_btn.clicked.connect(self._on_install_clicked)
        self._uninstall_btn = bb.addButton(_("Uninstall"), QDialogButtonBox.DestructiveRole)
        self._uninstall_btn.setEnabled(False)
        self._uninstall_btn.clicked.connect(self._on_uninstall_clicked)
        bb.addButton(QDialogButtonBox.Close).clicked.connect(self.reject)
        vbox.addWidget(bb)

    # ── Index loading ──────────────────────────────────────────────────────

    def _load_index(self):
        run_in_thread(lambda: pack_repo.fetch_index(), self._on_index_loaded)

    def _on_index_loaded(self, result, select_pack_id=None):
        if isinstance(result, Exception):
            self._status.setText(
                _("Couldn't reach the pack gallery. Check your connection and reopen.\n{err}")
                .format(err=result))
            return
        self._base_url, all_entries = result
        # Show ALL OSes: the desktop manages remote machines of any OS over SSH, so
        # a Windows pack is useful from a Linux box. Packs are grouped under
        # collapsible OS sections (the host OS opens by default).
        self._entries = list(all_entries)
        # "Installed" = the pack's buttons are actually present (not just a recorded
        # version), so a stale record never shows a phantom ✓ / ⬆.
        installed = pack_service.installed_pack_ids(self._config)
        self._updates = {pid for pid in pack_service.updates_available(self._config, self._entries)
                         if pid in installed}

        # Repopulating sets check states, which would fire itemChanged for every row;
        # block while rebuilding and unblock before restoring the current selection.
        self._tree.blockSignals(True)
        self._tree.clear()
        first_child = target_child = None
        for os, members in pack_repo.group_by_os(self._entries):
            section = QTreeWidgetItem(self._tree,
                                      [f"{_os_label(os)}  ({len(members)})"])
            section.setFlags(Qt.ItemIsEnabled)  # expandable header, not selectable
            f = section.font(0)
            f.setBold(True)
            section.setFont(0, f)
            for e in members:
                label = e.name
                if e.pack_id in self._updates:
                    label += "  ⬆"
                elif e.pack_id in installed:
                    label += "  ✓"
                child = QTreeWidgetItem(section, [label])
                child.setData(0, Qt.UserRole, e)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setCheckState(0, Qt.Unchecked)
                if first_child is None:
                    first_child = child
                if e.pack_id == select_pack_id:
                    target_child = child
                    section.setExpanded(True)  # keep the reselected pack visible
            # Open the host-OS and cross-platform sections; collapse the rest so the
            # list stays short as more packs land.
            if not section.isExpanded():
                section.setExpanded(os in (self._host_os, ""))
        self._tree.blockSignals(False)
        if self._entries:
            self._status.setText(_("{n} packs available.").format(n=len(self._entries)))
            pick = target_child or first_child
            if pick is not None:
                self._tree.setCurrentItem(pick)
                self._on_select(pick)  # ensure action buttons match even if selection didn't change
        else:
            self._status.setText(_("No packs available yet."))

    def _on_select(self, item, _previous=None):
        e = item.data(0, Qt.UserRole) if item else None
        if e is None:  # section header or empty
            self._update_action_buttons()
            return
        self._title.setText(e.name + (f"  ·  v{e.pack_ver}" if e.pack_ver else ""))
        bits = []
        if e.os:
            bits.append(e.os)
        if e.tags:
            bits.append(", ".join(e.tags))
        if e.pack_id in self._updates:
            bits.append(_("update available"))
        self._meta.setText("  ·  ".join(bits) + ("\n\n" + e.description if e.description else ""))
        self._preview.setPlainText(_("Loading…"))
        self._update_action_buttons()
        # Fetch the pack to preview its commands (and cache for install).
        run_in_thread(lambda: pack_repo.fetch_pack_files(e, self._base_url),
                      lambda r, e=e: self._on_pack_fetched(r, e))

    def _on_item_changed(self, item, _col):
        # A checkbox toggle changes which packs the action buttons target.
        self._update_action_buttons()

    # ── Selection → action targets ───────────────────────────────────────────

    def _all_pack_items(self):
        items = []
        for i in range(self._tree.topLevelItemCount()):
            section = self._tree.topLevelItem(i)
            for j in range(section.childCount()):
                items.append(section.child(j))
        return items

    def _checked_entries(self):
        return [it.data(0, Qt.UserRole) for it in self._all_pack_items()
                if it.checkState(0) == Qt.Checked]

    def _action_entries(self):
        """Packs a batch action targets: the ticked ones, or — if none ticked — the
        highlighted row (so the single-pack flow still works without ticking)."""
        checked = self._checked_entries()
        if checked:
            return checked
        cur = self._current_entry()
        return [cur] if cur is not None else []

    def _update_action_buttons(self):
        targets = self._action_entries()
        installed = pack_service.installed_pack_ids(self._config)

        # Install/Update: enabled if at least one target is installable — not yet
        # fetched (unknown) or fetched-and-verified. All targets unsigned → disabled.
        installable = [e for e in targets
                       if (c := self._cache.get(e.pack_id)) is None or c[2]]
        self._install_btn.setEnabled(bool(installable))
        if len(targets) <= 1:
            one_installed = bool(targets) and targets[0].pack_id in installed
            self._install_btn.setText(_("Update") if one_installed else _("Install…"))
        else:
            self._install_btn.setText(_("Install / Update ({n})").format(n=len(targets)))

        removable = [e for e in targets if e.pack_id in installed]
        self._uninstall_btn.setEnabled(bool(removable))
        self._uninstall_btn.setText(
            _("Uninstall ({n})").format(n=len(removable)) if len(removable) > 1
            else _("Uninstall"))

    def _on_pack_fetched(self, result, entry):
        if self._current_entry() is not entry:
            return  # selection moved on
        if isinstance(result, Exception):
            self._preview.setPlainText(_("Couldn't load this pack: {err}").format(err=result))
            return
        toml_bytes, sig = result
        try:
            manifest, buttons = pf.parse_pack(toml_bytes)
        except pf.PackError as ex:
            self._preview.setPlainText(_("This pack looks malformed: {err}").format(err=ex))
            return
        verified = bool(sig) and pf.verify_signature(toml_bytes, sig)
        self._cache[entry.pack_id] = (manifest, buttons, verified)
        if verified:
            badge = _("✓ Verified official pack")
        else:
            badge = _("⛔ Not signed by Commandeck — this pack can't be installed.")
        # Verification just landed → refresh enable state (disables Install if the
        # only target is this now-known-unsigned pack).
        self._update_action_buttons()
        lines = [badge, ""]
        if manifest.requires:
            lines += [_("Requires: {req}").format(req=manifest.requires), ""]
        for b in buttons:
            lines.append(f"• {b.name}")
            lines.append(f"    {b.command}")
        self._preview.setPlainText("\n".join(lines))

    def _current_entry(self):
        item = self._tree.currentItem()
        return item.data(0, Qt.UserRole) if item else None

    # ── Install ────────────────────────────────────────────────────────────

    def _on_install_clicked(self):
        targets = self._action_entries()
        if not targets:
            return
        # Ticked packs that were never previewed aren't cached → fetch + verify them all
        # via the shared core gather, then act on the gathered set.
        self._set_busy(True, _("Preparing…"))
        missing = [e for e in targets if e.pack_id not in self._cache]

        def on_fetched(cache_add, errors):
            self._cache.update(cache_add)
            self._do_batch_install(targets, errors)

        pack_repo.fetch_packs(missing, on_fetched, self._base_url)

    def _do_batch_install(self, targets, fetch_errors):
        self._set_busy(False)
        # Core decides update vs install vs skipped (verified-only gate); keep the
        # specific fetch-error message where we have one (plan reports "couldn't load").
        plan = pack_service.plan_batch(self._config, targets, self._cache)
        err_by_id = {e.pack_id: msg for e, msg in fetch_errors}
        skipped = [(e, err_by_id.get(e.pack_id, reason)) for e, reason in plan.skipped]

        if not plan.to_update and not plan.to_install:
            self._warn_skipped(skipped)
            return

        # A lone fresh install (nothing to update) keeps the richer single dialog
        # (machine targets + category override). Mixed/batch sets use one shared
        # machine picker and each pack's own category.
        if len(plan.to_install) == 1 and not plan.to_update:
            manifest, buttons, _v = self._cache[plan.to_install[0].pack_id]
            step = _InstallStep(self._config, manifest, buttons, parent=None)
            if step.exec() != QDialog.Accepted:
                return
            self._after_change(_("Installed {n} buttons").format(n=step.installed_count))
            self._warn_skipped(skipped)
            return

        machine_ids = [""]  # Local by default; only asked when there are fresh installs
        if plan.to_install:
            picker = _BatchTargetStep(self._config, parent=None)
            if picker.exec() != QDialog.Accepted:
                return
            machine_ids = picker.machine_ids

        summary = pack_service.apply_batch(self._config, plan, self._cache, machine_ids)
        for manifest, conflicts in summary["conflicts"]:
            _resolve_conflicts_dialog(self._config, manifest, conflicts, self)
        self._after_change(
            pack_service.summarize_batch(summary["added"], summary["updated"]))
        self._warn_skipped(skipped)

    def _warn_skipped(self, skipped):
        if not skipped:
            return
        names = "\n".join(f"• {e.name} — {why}" for e, why in skipped)
        QMessageBox.warning(
            self, _("Some packs were skipped"),
            _("These packs couldn't be installed:\n\n{names}").format(names=names))

    def _set_busy(self, busy: bool, text: str | None = None):
        self._install_btn.setEnabled(not busy)
        self._uninstall_btn.setEnabled(not busy)
        if text is not None:
            self._status.setText(text)
        elif not busy and self._entries:
            self._status.setText(_("{n} packs available.").format(n=len(self._entries)))
        if not busy:
            self._update_action_buttons()

    def _on_uninstall_clicked(self):
        targets = [e for e in self._action_entries()
                   if e.pack_id in pack_service.installed_pack_ids(self._config)]
        if not targets:
            return
        total = sum(len(pack_service.existing_pack_buttons(self._config, e.pack_id))
                    for e in targets)
        if len(targets) == 1:
            prompt = _("Remove the {n} buttons installed from this pack?").format(n=total)
            title = _("Uninstall {name}").format(name=targets[0].name)
        else:
            prompt = _("Remove the {n} buttons installed from these {p} packs?").format(
                n=total, p=len(targets))
            title = _("Uninstall packs")
        if QMessageBox.question(
            self, title, prompt,
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No) != QMessageBox.Yes:
            return
        n = sum(pack_service.uninstall_pack(self._config, e.pack_id) for e in targets)
        self._after_change(_("Removed {n} buttons").format(n=n))

    def _after_change(self, toast: str, keep_pack_id: str | None = None):
        """Refresh badges + the main grid and toast after an install/uninstall.
        ``keep_pack_id`` keeps that pack selected so its Install/Update + Uninstall
        buttons reflect the new state instead of jumping to the top of the list."""
        self.changed = True
        # reflect new "installed/update" state (recomputes the ✓ / ⬆ badges)
        self._on_index_loaded((self._base_url, self._entries + []), keep_pack_id)
        if self._main is not None and hasattr(self._main, "populate_grid"):
            self._main.populate_grid()
        if self._main is not None and hasattr(self._main, "show_toast"):
            self._main.show_toast(toast)


class _BatchTargetStep(QDialog):
    """Pick the machine target(s) once for a batch of fresh pack installs. Each pack
    keeps its own category (no override), so this only collects ``machine_ids``."""

    def __init__(self, config, parent=None):
        super().__init__(parent)
        self._machines = config.load_machines()
        self._checks: list[tuple[str, QCheckBox]] = []
        self.machine_ids: list[str] = []

        self.setWindowTitle(_("Install packs"))
        self.setMinimumWidth(420)
        v = QVBoxLayout(self)
        v.addWidget(QLabel(_("Run the new packs on:")))
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        inner = QWidget()
        iv = QVBoxLayout(inner)
        local = QCheckBox(_("Local"))
        local.setChecked(True)
        iv.addWidget(local)
        self._checks.append(("", local))
        for m in self._machines:
            cb = QCheckBox(f"{m.name}  —  {m.label}")
            iv.addWidget(cb)
            self._checks.append((m.id, cb))
        iv.addStretch()
        scroll.setWidget(inner)
        v.addWidget(scroll, 1)

        if not self._machines:
            nudge = QLabel(_("Want to run this on your server over SSH? "
                             "Start the free 14-day Pro trial — no card."))
            nudge.setWordWrap(True)
            nudge.setStyleSheet("color: palette(mid); font-style: italic;")
            v.addWidget(nudge)

        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(self._accept)
        bb.rejected.connect(self.reject)
        v.addWidget(bb)

    def _accept(self):
        ids = [mid for mid, cb in self._checks if cb.isChecked()]
        if not ids:
            QMessageBox.information(self, _("Pick a target"),
                                    _("Choose at least Local or a machine."))
            return
        self.machine_ids = ids
        self.accept()


class _InstallStep(QDialog):
    """Machine target + category, then install via the shared core service."""

    def __init__(self, config, manifest, buttons, parent=None):
        super().__init__(parent)
        self._config = config
        self._manifest = manifest
        self._buttons = buttons
        self._machines = config.load_machines()
        self._checks: list[tuple[str, QCheckBox]] = []
        self.installed_count = 0

        self.setWindowTitle(_("Install {name}").format(name=manifest.name))
        self.setMinimumWidth(420)
        self._build_ui()

    def _build_ui(self):
        v = QVBoxLayout(self)
        v.addWidget(QLabel(_("Run on:")))
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        inner = QWidget()
        iv = QVBoxLayout(inner)
        local = QCheckBox(_("Local"))
        local.setChecked(True)
        iv.addWidget(local)
        self._checks.append(("", local))
        for m in self._machines:
            cb = QCheckBox(f"{m.name}  —  {m.label}")
            iv.addWidget(cb)
            self._checks.append((m.id, cb))
        iv.addStretch()
        scroll.setWidget(inner)
        v.addWidget(scroll, 1)

        if not self._machines:
            nudge = QLabel(_("Want to run this on your server over SSH? "
                             "Start the free 14-day Pro trial — no card."))
            nudge.setWordWrap(True)
            nudge.setStyleSheet("color: palette(mid); font-style: italic;")
            v.addWidget(nudge)

        cat_row = QHBoxLayout()
        cat_row.addWidget(QLabel(_("Category:")))
        self._cat = QLineEdit(self._manifest.category)
        cat_row.addWidget(self._cat, 1)
        v.addLayout(cat_row)

        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(self._do_install)
        bb.rejected.connect(self.reject)
        v.addWidget(bb)

    def _do_install(self):
        machine_ids = [mid for mid, cb in self._checks if cb.isChecked()]
        if not machine_ids:
            QMessageBox.information(self, _("Pick a target"),
                                    _("Choose at least Local or a machine."))
            return
        category = self._cat.text().strip() or self._manifest.category

        mode = "first"
        existing = pack_service.existing_pack_buttons(self._config, self._manifest.pack_id)
        if existing:
            mode = self._ask_conflict(len(existing))
            if mode == "cancel":
                return

        installed = pack_service.install_pack(
            self._config, self._manifest, self._buttons, machine_ids, category, mode)
        self.installed_count = len(installed)
        self.accept()

    def _ask_conflict(self, n: int) -> str:
        box = QMessageBox(self)
        box.setWindowTitle(_("Already installed"))
        box.setIcon(QMessageBox.Question)
        box.setText(_("{name} is already installed ({n} buttons).").format(
            name=self._manifest.name, n=n))
        box.setInformativeText(_("Update it to this version, or add a second copy?"))
        upd = box.addButton(_("Update"), QMessageBox.AcceptRole)
        dup = box.addButton(_("Add as duplicate"), QMessageBox.ActionRole)
        box.addButton(_("Cancel"), QMessageBox.RejectRole)
        box.setDefaultButton(upd)
        box.exec()
        clicked = box.clickedButton()
        if clicked is upd:
            # An update keeps machine targets; reuse apply_pack_update via "replace"
            # semantics is wrong (loses targets), so do a real update instead.
            self._apply_update()
            return "cancel"  # update already applied; skip install
        if clicked is dup:
            return "duplicate"
        return "cancel"

    def _apply_update(self):
        summary = pack_service.apply_pack_update(self._config, self._manifest, self._buttons)
        conflicts = summary.get("conflicts", [])
        if conflicts:
            _resolve_conflicts_dialog(self._config, self._manifest, conflicts, self)
        self.installed_count = summary["updated"] + summary["added"] + len(conflicts)
        self.accept()


class _ConflictDialog(QDialog):
    """Resolve pack-update conflicts: the user edited a button's command AND the new
    pack version also changed it. One row per conflicted button — Overwrite (take the
    pack's command) or Keep both (the user's edit becomes a standalone custom button
    and the pack's new button is added alongside). "Apply to all" mirrors the first
    row's choice onto the rest."""

    def __init__(self, manifest, conflicts, parent=None):
        super().__init__(parent)
        self.setWindowTitle(_("Resolve update conflicts"))
        self.setMinimumWidth(560)
        self._conflicts = conflicts
        self._choices: dict[str, str] = {}  # pack_button_id -> "overwrite"|"duplicate"

        v = QVBoxLayout(self)
        intro = QLabel(_(
            "You edited these {name} buttons, and the update changes them too. "
            "Choose what to keep for each.").format(name=manifest.name))
        intro.setWordWrap(True)
        v.addWidget(intro)

        self._groups = []
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        iv = QVBoxLayout(inner)
        for old, new in conflicts:
            iv.addWidget(self._make_row(old, new))
        iv.addStretch(1)
        scroll.setWidget(inner)
        v.addWidget(scroll, 1)

        if len(conflicts) > 1:
            allrow = QHBoxLayout()
            allrow.addStretch(1)
            ov = QPushButton(_("Overwrite all"))
            ka = QPushButton(_("Keep both for all"))
            ov.clicked.connect(lambda: self._apply_all("overwrite"))
            ka.clicked.connect(lambda: self._apply_all("duplicate"))
            allrow.addWidget(ov)
            allrow.addWidget(ka)
            v.addLayout(allrow)

        bb = QDialogButtonBox(QDialogButtonBox.Ok)
        bb.accepted.connect(self.accept)
        v.addWidget(bb)

    def _make_row(self, old, new):
        from PySide6.QtWidgets import QGroupBox, QRadioButton, QButtonGroup
        box = QGroupBox(old.name)
        bv = QVBoxLayout(box)
        yours = QLabel(_("Your command:") + f"  {old.command}")
        yours.setWordWrap(True)
        yours.setStyleSheet("color: palette(mid);")
        theirs = QLabel(_("New command:") + f"  {new.command}")
        theirs.setWordWrap(True)
        theirs.setStyleSheet("color: palette(mid);")
        bv.addWidget(yours)
        bv.addWidget(theirs)
        grp = QButtonGroup(box)
        rb_over = QRadioButton(_("Overwrite with the new command"))
        rb_dup = QRadioButton(_("Keep both (mine + the new one)"))
        rb_dup.setChecked(True)
        grp.addButton(rb_over)
        grp.addButton(rb_dup)
        bv.addWidget(rb_over)
        bv.addWidget(rb_dup)
        self._groups.append((old, rb_over, rb_dup))
        return box

    def _apply_all(self, choice: str):
        for _old, rb_over, rb_dup in self._groups:
            (rb_over if choice == "overwrite" else rb_dup).setChecked(True)

    def choices(self) -> list[tuple]:
        """[(old, new, choice)] in the dialog's order."""
        out = []
        for (old, new), (_o, rb_over, _d) in zip(self._conflicts, self._groups):
            out.append((old, new, "overwrite" if rb_over.isChecked() else "duplicate"))
        return out


def _resolve_conflicts_dialog(config, manifest, conflicts, parent=None) -> None:
    """Show the conflict resolver and apply the user's per-button choices."""
    dlg = _ConflictDialog(manifest, conflicts, parent)
    dlg.exec()  # OK-only; default = "Keep both", a safe non-destructive choice
    for old, new, choice in dlg.choices():
        pack_service.resolve_conflict(config, old, new, choice)
