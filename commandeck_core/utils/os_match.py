"""OS tagging helpers shared by import dedup and machine propagation.

A button carries the OS its *command* is written for (``CommandButton.os``); a
machine carries its host OS (``Machine.os``). Both use the canonical values
``""`` (cross-platform / unknown), ``"linux"``, ``"macos"`` and ``"windows"``.

Two responsibilities live here so the rules stay in one place:

* ``identity_os(os)`` — the value used in the import-dedup identity key. Buttons
  are deduped by ``(command, identity_os)``, so a Linux variant and a Windows
  variant of the same action coexist on import (the whole point), while a
  re-import of the same set adds nothing.
* ``os_compatible(button_os, target_os)`` — may this machine run this button?
  Used when propagating a machine onto buttons: a machine is only attached to
  buttons it can actually execute. POSIX (linux/macos) are mutually compatible
  because Commandeck seeds them the same shared command set.
"""

_POSIX = {"linux", "macos"}

_OS_DISPLAY = {"linux": "Linux", "macos": "macOS", "windows": "Windows"}


def os_label(value: str) -> str:
    """Human display name for an OS value ('' / unknown -> ''). OS names are
    brand names, identical in every language, so they are not translated."""
    return _OS_DISPLAY.get(normalize_os(value), "")


def normalize_os(value: str) -> str:
    """Canonicalize an OS string to ""/"linux"/"macos"/"windows"."""
    s = (value or "").strip().lower()
    if s.startswith("win"):
        return "windows"
    if s.startswith(("darwin", "mac")):
        return "macos"
    if s.startswith("linux"):
        return "linux"
    return ""  # unknown / cross-platform


def identity_os(value: str) -> str:
    """OS component of a button's import-dedup identity (normalized)."""
    return normalize_os(value)


def os_compatible(button_os: str, target_os: str) -> bool:
    """True if a button written for ``button_os`` can run on a ``target_os`` host.

    Permissive by design: a cross-platform button (``""``) runs anywhere, and an
    unknown machine OS (``""``) never blocks (preserves behaviour for machines
    saved before the OS field existed). linux⇄macos are compatible (shared set).
    """
    b = normalize_os(button_os)
    t = normalize_os(target_os)
    if not b or not t:
        return True
    if b == t:
        return True
    return b in _POSIX and t in _POSIX
