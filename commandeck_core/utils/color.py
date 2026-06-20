"""Tiny colour helpers shared by the desktop (Qt) and mobile (Toga) UIs.

Pure stdlib, zero UI deps — safe to import from commandeck_core. Keeps the
"hex parsing + readable-text" logic in one place instead of three.
"""
from __future__ import annotations

import re

_HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")


def is_hex_color(value: str) -> bool:
    """True for a `#rrggbb` string (the form the app stores button colours in)."""
    return bool(value) and bool(_HEX_RE.match(value.strip()))


def contrast_text(hex_color: str, dark: str = "#1a1a1a", light: str = "#ffffff") -> str:
    """Return `dark` or `light` — whichever reads better on ``hex_color`` — using the
    WCAG relative-luminance threshold. Returns "" if ``hex_color`` isn't a #rrggbb."""
    if not is_hex_color(hex_color):
        return ""
    h = hex_color.strip()
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))

    def _lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    lum = 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)
    # ~0.179 is the WCAG crossover where black vs white text give equal contrast;
    # above it dark text wins. (A higher threshold wrongly puts white text on
    # medium-light pastels, which reads washed-out / "fade".)
    return dark if lum > 0.179 else light
