"""Downloadable button-pack format (`pack.toml` + detached Ed25519 signature).

The free OS-default buttons stay bundled (`_default_buttons.py`). Everything else
(dev-tools, home-server-starter, niche + community packs) is distributed as a
`pack.toml` fetched from the public `commandeck-packs` repo, optionally paired with
a `pack.sig` (detached Ed25519 signature over the exact `pack.toml` bytes).

This module is **pure core** (zero UI deps): it parses a pack into `CommandButton`s
and verifies the signature against the embedded public key. Install/update against a
`ConfigManager` lives alongside (see `install_pack`); the gallery UI just renders.

Trust model (PACK_DESIGN.md; tightened 2026-06-18): a pack is **only installable when its
signature verifies against the embedded public key** — packs stay under Commandeck's
control. A valid signature → "✓ Verified" badge + install. Unsigned / invalid / tampered →
the gallery shows the commands but **refuses to install** (no badge, no update semantics).
Personal **backups** (`.cdbackup`) are the user's own data and import without a signature —
that exception does not apply to packs. The signing **private** key never ships and never
enters any public-mirrored repo (it lives in `dev/packs/.signing/`, gitignored); only this
public key is embedded.
"""
from __future__ import annotations

import io
import tomllib
import uuid
import zipfile
from dataclasses import dataclass, field

from .command_button import CommandButton

# Ed25519 public key (raw 32 bytes, hex). Public by design — safe to embed/mirror.
# Private counterpart: dev/packs/.signing/pack_signing_key.pem (NEVER shipped).
PACK_PUBLIC_KEY_HEX = "4bd3d888918f2b43d45b76ce3a2e4a1358befd24bcc93b04d9219674ad6302d6"

PACK_FORMAT_VERSION = 1


class PackError(ValueError):
    """Malformed pack file (bad TOML, missing required fields, wrong version)."""


@dataclass(frozen=True)
class PackManifest:
    pack_id: str            # stable across versions — the update key
    name: str
    pack_ver: str           # bumped every release → drives "update available"
    os: str                 # "linux" | "macos" | "windows" | "" (cross-platform)
    category: str           # default category applied to the pack's buttons
    description: str = ""
    requires: str = ""      # free-text prerequisites shown before install
    theme: str = ""         # recommended button theme (Pro), "" = none
    tags: tuple[str, ...] = ()  # gallery filtering (e.g. "docker", "jellyfin")


def verify_signature(pack_toml_bytes: bytes, signature: bytes) -> bool:
    """True iff ``signature`` is a valid Ed25519 signature over ``pack_toml_bytes``
    for the embedded public key. Never raises on a bad signature — returns False."""
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    from cryptography.exceptions import InvalidSignature

    try:
        pub = Ed25519PublicKey.from_public_bytes(bytes.fromhex(PACK_PUBLIC_KEY_HEX))
        pub.verify(signature, pack_toml_bytes)
        return True
    except (InvalidSignature, ValueError):
        return False


def parse_pack(pack_toml_bytes: bytes) -> tuple[PackManifest, list[CommandButton]]:
    """Parse ``pack.toml`` bytes → (manifest, buttons).

    Each button gets a **fresh runtime UUID** ``id`` (so repeated installs never
    collide), while the pack file's stable button ``id`` is kept in
    ``pack_button_id`` (the update-matching key). ``source_pack`` is stamped with
    the pack id and ``os`` with the manifest OS. Raises ``PackError`` on malformed
    input."""
    try:
        data = tomllib.loads(pack_toml_bytes.decode("utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise PackError(f"Invalid pack TOML: {e}") from e

    version = data.get("version")
    if version != PACK_FORMAT_VERSION:
        raise PackError(f"Unsupported pack version: {version!r} (expected {PACK_FORMAT_VERSION})")

    pack = data.get("pack")
    if not isinstance(pack, dict):
        raise PackError("Missing [pack] table")
    try:
        manifest = PackManifest(
            pack_id=str(pack["pack_id"]),
            name=str(pack["name"]),
            pack_ver=str(pack["pack_ver"]),
            os=str(pack.get("os", "")),
            category=str(pack.get("category", "")),
            description=str(pack.get("description", "")),
            requires=str(pack.get("requires", "")),
            theme=str(pack.get("theme", "")),
            tags=tuple(str(t) for t in pack.get("tags", [])),
        )
    except KeyError as e:
        raise PackError(f"Missing required [pack] field: {e}") from e

    raw_buttons = data.get("button", [])
    if not raw_buttons:
        raise PackError("Pack contains no [[button]] entries")

    buttons: list[CommandButton] = []
    for entry in raw_buttons:
        if "name" not in entry or "command" not in entry:
            raise PackError("Each [[button]] needs at least name and command")
        stable_id = str(entry.get("id", ""))
        d = dict(entry)
        d["id"] = str(uuid.uuid4())          # fresh runtime id
        btn = CommandButton.from_dict(d)
        btn.pack_button_id = stable_id
        btn.source_pack = manifest.pack_id
        # A button may override the pack OS (lets one cross-OS pack carry both bash
        # and PowerShell buttons, each tagged for its own targets); else inherit.
        if "os" not in entry:
            btn.os = manifest.os
        btn.is_default = False
        if not btn.category:
            btn.category = manifest.category
        buttons.append(btn)
    return manifest, buttons


def write_cdpack(pack_toml_bytes: bytes, sig: bytes | None = None) -> bytes:
    """Bundle a pack into a ``.cdpack`` (a zip with ``pack.toml`` [+ ``pack.sig``]).

    Used by Export-as-pack so a shared pack has a recognisable extension and reads back
    via :func:`read_cdpack`. Community exports are unsigned (``sig=None``)."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("pack.toml", pack_toml_bytes)
        if sig is not None:
            zf.writestr("pack.sig", sig)
    return buf.getvalue()


def read_cdpack(data: bytes) -> tuple[bytes, bytes | None]:
    """Unzip a ``.cdpack`` (used for manual file import) → (pack_toml_bytes, sig_or_None).

    The gallery downloads ``pack.toml`` + ``pack.sig`` directly and skips this."""
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            names = set(zf.namelist())
            if "pack.toml" not in names:
                raise PackError(".cdpack is missing pack.toml")
            toml_bytes = zf.read("pack.toml")
            sig = zf.read("pack.sig") if "pack.sig" in names else None
        return toml_bytes, sig
    except zipfile.BadZipFile as e:
        raise PackError(f"Not a valid .cdpack archive: {e}") from e
