"""Fetch the public pack gallery (index.json + pack files) — pure core, stdlib only.

Shared by desktop (Qt) and mobile. Network calls block; the UIs run them off the
main thread (Qt ThreadPoolExecutor / mobile worker) exactly like command execution.
``parse_index`` is split out so it can be unit-tested without the network.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass

DEFAULT_BASE_URL = "https://raw.githubusercontent.com/neurocontrarian/commandeck-packs/main"
DEFAULT_INDEX_URL = f"{DEFAULT_BASE_URL}/index.json"


class PackRepoError(Exception):
    """Network failure or malformed index.json."""


@dataclass(frozen=True)
class PackEntry:
    pack_id: str
    name: str
    description: str
    os: str                 # "" = cross-platform
    tags: tuple[str, ...]
    pack_ver: str
    path: str               # pack.toml path relative to base_url
    sig: str                # pack.sig path, "" if unsigned

    def matches_os(self, target_os: str) -> bool:
        """Show in the gallery for ``target_os`` ("linux"/"macos"/"windows"). A
        cross-platform pack (os == "") shows everywhere."""
        return self.os in ("", target_os)


# Section order for the OS-grouped gallery (both desktop + mobile). "" = cross-platform.
OS_DISPLAY_ORDER = ["linux", "macos", "windows", ""]


def group_by_os(entries) -> list[tuple[str, list]]:
    """Group gallery entries into ``[(os, [entries])]`` in a stable OS order so packs
    that share a name across OSes (e.g. "Hardware") sit under clear section headers.
    Unknown OS values are appended last. Each UI maps the ``os`` string to a label."""
    out = []
    known = set(OS_DISPLAY_ORDER)
    for os in OS_DISPLAY_ORDER + sorted({e.os for e in entries} - known):
        members = [e for e in entries if e.os == os]
        if members:
            out.append((os, members))
    return out


def parse_index(data: bytes) -> tuple[str, list[PackEntry]]:
    """Parse index.json bytes → (base_url, entries). Raises PackRepoError."""
    try:
        obj = json.loads(data.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise PackRepoError(f"Invalid index.json: {e}") from e
    base = obj.get("base_url", DEFAULT_BASE_URL)
    entries: list[PackEntry] = []
    for p in obj.get("packs", []):
        try:
            entries.append(PackEntry(
                pack_id=str(p["pack_id"]),
                name=str(p.get("name", p["pack_id"])),
                description=str(p.get("description", "")),
                os=str(p.get("os", "")),
                tags=tuple(str(t) for t in p.get("tags", [])),
                pack_ver=str(p.get("pack_ver", "")),
                path=str(p["path"]),
                sig=str(p.get("sig", "")),
            ))
        except KeyError as e:
            raise PackRepoError(f"index entry missing field: {e}") from e
    return base, entries


def _get(url: str, timeout: float) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:  # noqa: S310 (https only)
            return r.read()
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise PackRepoError(f"Could not fetch {url}: {e}") from e


def fetch_index(url: str = DEFAULT_INDEX_URL, timeout: float = 10) -> tuple[str, list[PackEntry]]:
    """Download + parse the gallery index. Raises PackRepoError on any failure."""
    return parse_index(_get(url, timeout))


def fetch_pack_files(entry: PackEntry, base_url: str = DEFAULT_BASE_URL,
                     timeout: float = 10) -> tuple[bytes, bytes | None]:
    """Download a pack's ``pack.toml`` and (if present) ``pack.sig``.
    A missing/failed signature returns ``None``; the UI then refuses to install the pack
    (only signature-verified packs are installable)."""
    toml_bytes = _get(f"{base_url}/{entry.path}", timeout)
    sig: bytes | None = None
    if entry.sig:
        try:
            sig = _get(f"{base_url}/{entry.sig}", timeout)
        except PackRepoError:
            sig = None
    return toml_bytes, sig


def fetch_packs(entries, on_done, base_url: str = DEFAULT_BASE_URL) -> None:
    """Fetch + parse + verify several packs off the main thread, then call
    ``on_done(cache_add, errors)`` ON THE MAIN THREAD (via the run_in_thread dispatcher
    both UIs wire up). Shared by the desktop gallery and the mobile gallery so a batch
    action loads its packs identically on both.

      * ``cache_add`` — ``{pack_id: (manifest, buttons, verified)}`` for every pack that
        downloaded + parsed (``verified`` = Ed25519 signature checks out).
      * ``errors`` — ``[(entry, message)]`` for packs that failed to download or parse.

    Pass only the entries you still need (filter out anything already cached). Calling
    with no entries fires ``on_done({}, [])`` synchronously."""
    # Lazy imports: keep the module's top-level stdlib-only and avoid any import cycle.
    from commandeck_core.models import pack_format as pf
    from commandeck_core.utils.threading import run_in_thread

    entries = list(entries)
    if not entries:
        on_done({}, [])
        return
    state = {"left": len(entries), "cache": {}, "errors": []}

    def _make_cb(e):
        def _cb(result):
            if isinstance(result, Exception):
                state["errors"].append((e, str(result)))
            else:
                toml_bytes, sig = result
                try:
                    manifest, buttons = pf.parse_pack(toml_bytes)
                    verified = bool(sig) and pf.verify_signature(toml_bytes, sig)
                    state["cache"][e.pack_id] = (manifest, buttons, verified)
                except pf.PackError as ex:
                    state["errors"].append((e, str(ex)))
            state["left"] -= 1
            if state["left"] == 0:
                on_done(state["cache"], state["errors"])
        return _cb

    for e in entries:
        run_in_thread(lambda e=e: fetch_pack_files(e, base_url), _make_cb(e))
