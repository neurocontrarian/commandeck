"""Single source of truth for the button-tile themes (Qt).

Each theme used to be spread across `window._THEME_QSS` plus four dicts in
`button_tile` (shadows, icon tints, label colours, the "full bg" set) plus a
`if theme == "neon"` special-case in three methods. This registry folds all of
that into one `ThemeSpec` per theme, keyed by name, so adding/changing a theme
means editing one entry.

`color_role` says what a button's own colour does under the theme:
  - "bg"     → it is the tile background (bold)
  - "border" → it is the border (+ glow), tile bg comes from `bg` (neon)
  - "full"   → the theme owns the background; per-button colour is ignored
               (cards / phone / retro / tron)
"""
from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtGui import QColor


@dataclass(frozen=True)
class ThemeSpec:
    qss: str                       # widget-level QSS for the tile
    color_role: str                # "bg" | "border" | "full"
    label_color: str = ""          # explicit label colour; "" → derive (contrast for "bg")
    icon_tint: QColor | None = None
    # shadow: (x, y, blur, QColor) fixed glow | "button" (glow in the button's colour) | None
    shadow: object = None
    bg: str = ""                   # immersive background for "border" themes (e.g. neon)
    border_px: int = 0             # tile border width per side (must mirror the qss) —
                                   # subtracted from the label's available width so a
                                   # name is elided, never clipped, under thick borders


_BOLD_QSS = """
QFrame#ButtonTile {
    background-color: palette(highlight);
    border: none;
    border-radius: 10px;
}
QFrame#ButtonTile:hover {
    background-color: palette(dark);
}
QFrame#ButtonTile QLabel#TileLabel {
    color: palette(highlighted-text);
    font-weight: bold;
}
"""

_CARDS_QSS = """
QFrame#ButtonTile {
    background-color: palette(base);
    border: 2px solid rgba(53,132,228,71);
    border-radius: 12px;
}
QFrame#ButtonTile:hover {
    border-color: rgba(53,132,228,165);
}
"""

_PHONE_QSS = """
QFrame#ButtonTile {
    background: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #f5f5f5,stop:1 #d8d8d8);
    border: 1px solid rgba(0,0,0,38);
    border-bottom: 4px solid rgba(0,0,0,64);
    border-radius: 8px;
}
QFrame#ButtonTile:hover {
    background: qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #ffffff,stop:1 #e8e8e8);
}
"""

_NEON_QSS = """
QFrame#ButtonTile {
    background-color: #0d0d0d;
    border: 1px solid #00c8ff;
    border-radius: 8px;
}
QFrame#ButtonTile:hover {
    border-color: #66e0ff;
}
QFrame#ButtonTile QLabel#TileLabel {
    color: #00c8ff;
    font-weight: bold;
}
"""

_TRON_QSS = """
QFrame#ButtonTile {
    background-color: #000000;
    border: 1px solid #ffffff;
    border-radius: 2px;
}
QFrame#ButtonTile:hover {
    border-color: #ffffff;
    background-color: #060a10;
}
QFrame#ButtonTile QLabel#TileLabel {
    color: #1e90ff;
    font-weight: bold;
}
"""

_RETRO_QSS = """
QFrame#ButtonTile {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #e8622a,stop:1 #f0981a);
    border: 3px solid #993300;
    border-radius: 4px;
}
QFrame#ButtonTile:hover {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 #ff7a3d,stop:1 #ffb030);
}
QFrame#ButtonTile QLabel#TileLabel {
    color: #ffffff;
    font-weight: bold;
}
"""


THEMES: dict[str, ThemeSpec] = {
    "bold":  ThemeSpec(_BOLD_QSS,  "bg",     shadow=(0, 3, 10, QColor(0, 0, 0, 71))),
    "cards": ThemeSpec(_CARDS_QSS, "full",   border_px=2, shadow=(0, 4, 12, QColor(0, 0, 0, 51))),
    "phone": ThemeSpec(_PHONE_QSS, "full",   label_color="#1a1a1a", border_px=1,
                       shadow=(0, 4, 6, QColor(0, 0, 0, 64))),
    "neon":  ThemeSpec(_NEON_QSS,  "border", label_color="#00c8ff", border_px=1,
                       icon_tint=QColor(0, 200, 255), shadow="button", bg="#0d0d0d"),
    "tron":  ThemeSpec(_TRON_QSS,  "full",   label_color="#1e90ff", border_px=1,
                       icon_tint=QColor(30, 144, 255), shadow=(0, 0, 14, QColor(30, 144, 255, 110))),
    "retro": ThemeSpec(_RETRO_QSS, "full",   label_color="#ffffff", border_px=3,
                       shadow=(4, 4, 0, QColor(0, 0, 0, 220))),
}

DEFAULT_THEME = "bold"


def get_theme(name: str) -> ThemeSpec:
    return THEMES.get(name, THEMES[DEFAULT_THEME])
