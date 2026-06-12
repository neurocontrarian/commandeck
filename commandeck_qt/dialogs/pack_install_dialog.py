"""Install Button Pack dialog (Pro feature).

Lets a Pro user install one of the built-in packs (linux-defaults,
macos-defaults, windows-defaults) onto any combination of configured
machines (or local). Detects re-installs of the same pack and offers
Replace vs Add-as-duplicate.

The pack registry lives in commandeck_core.models._default_buttons.PACKS.
"""
from __future__ import annotations

import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit,
    QCheckBox, QDialogButtonBox, QPushButton, QScrollArea, QWidget,
    QMessageBox,
)

from commandeck_core.i18n import _
from commandeck_core.models.config import ConfigManager
from commandeck_core.models._default_buttons import PACKS, get_pack


def show_pack_install_dialog(config: ConfigManager, parent=None) -> bool:
    """Modal. Returns True if a pack was installed."""
    dlg = _PackInstallDialog(config, parent)
    return dlg.exec() == QDialog.Accepted


class _PackInstallDialog(QDialog):
    def __init__(self, config: ConfigManager, parent=None):
        super().__init__(parent)
        self._config = config
        self._machine_checks: list[tuple[str, QCheckBox]] = []  # ("" = local)
        self._machines = config.load_machines()

        self.setWindowTitle(_("Install Button Pack"))
        self.setMinimumWidth(480)
        self.setMinimumHeight(440)
        self._build_ui()
        self._refresh_description()
        self._refresh_category_suggestion()

    def _build_ui(self):
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(16, 16, 16, 12)
        vbox.setSpacing(10)

        # Pack chooser
        pack_row = QHBoxLayout()
        pack_row.addWidget(QLabel(_("Pack:")))
        self._pack_combo = QComboBox()
        self._pack_ids = list(PACKS.keys())
        for pid in self._pack_ids:
            self._pack_combo.addItem(_(PACKS[pid].name_key))
        self._pack_combo.currentIndexChanged.connect(self._on_pack_changed)
        pack_row.addWidget(self._pack_combo, 1)
        vbox.addLayout(pack_row)

        # Description
        self._desc_label = QLabel()
        self._desc_label.setWordWrap(True)
        self._desc_label.setStyleSheet("color: palette(mid);")
        vbox.addWidget(self._desc_label)

        # Machine multi-select
        vbox.addWidget(QLabel(_("Run on:")))
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        inner = QWidget()
        inner_vbox = QVBoxLayout(inner)
        inner_vbox.setContentsMargins(0, 0, 0, 0)

        # Local first
        local_cb = QCheckBox(_("Local"))
        local_cb.toggled.connect(self._on_selection_changed)
        inner_vbox.addWidget(local_cb)
        self._machine_checks.append(("", local_cb))

        for machine in self._machines:
            cb = QCheckBox(f"{machine.name}  —  {machine.user}@{machine.host}")
            cb.toggled.connect(self._on_selection_changed)
            inner_vbox.addWidget(cb)
            self._machine_checks.append((machine.id, cb))

        inner_vbox.addStretch()
        scroll.setWidget(inner)
        vbox.addWidget(scroll, 1)

        # Select all / deselect all
        self._toggle_all_btn = QPushButton(_("Select all"))
        self._toggle_all_btn.setFlat(True)
        self._toggle_all_btn.clicked.connect(self._on_toggle_all)
        vbox.addWidget(self._toggle_all_btn, alignment=Qt.AlignLeft)

        # Category field
        cat_row = QHBoxLayout()
        cat_row.addWidget(QLabel(_("Category:")))
        self._cat_edit = QLineEdit()
        cat_row.addWidget(self._cat_edit, 1)
        vbox.addLayout(cat_row)

        # Buttons
        bb = QDialogButtonBox()
        self._install_btn = bb.addButton(_("Install"), QDialogButtonBox.AcceptRole)
        self._install_btn.setEnabled(False)
        bb.addButton(QDialogButtonBox.Cancel)
        bb.accepted.connect(self._on_install)
        bb.rejected.connect(self.reject)
        vbox.addWidget(bb)

    # ── Helpers ───────────────────────────────────────────────────────────

    def _current_pack_id(self) -> str:
        return self._pack_ids[self._pack_combo.currentIndex()]

    def _selected_machine_ids(self) -> list[str]:
        return [mid for mid, cb in self._machine_checks if cb.isChecked()]

    def _refresh_description(self):
        pid = self._current_pack_id()
        n_buttons = len(PACKS[pid].builder())
        desc = _(PACKS[pid].description_key)
        self._desc_label.setText(
            _("{n} buttons. {desc}").format(n=n_buttons, desc=desc)
        )

    def _refresh_category_suggestion(self):
        """Pre-fill the category field based on pack + selection. Only auto-fills
        when the user hasn't manually edited it (we treat 'matches the last
        suggestion' as 'still default')."""
        pid = self._current_pack_id()
        pack_name = _(PACKS[pid].name_key)
        selected = self._selected_machine_ids()
        # If exactly one non-local machine is selected, suffix with its name.
        if len(selected) == 1 and selected[0] != "":
            machine = next((m for m in self._machines if m.id == selected[0]), None)
            if machine is not None:
                suggestion = f"{pack_name} – {machine.name}"
            else:
                suggestion = pack_name
        else:
            suggestion = pack_name
        # Avoid clobbering user input: only update if field is empty OR matches a
        # prior auto-suggestion we recorded.
        previous = getattr(self, "_last_suggestion", "")
        if not self._cat_edit.text() or self._cat_edit.text() == previous:
            self._cat_edit.setText(suggestion)
        self._last_suggestion = suggestion

    def _on_pack_changed(self):
        self._refresh_description()
        self._refresh_category_suggestion()

    def _on_selection_changed(self):
        count = sum(1 for _, cb in self._machine_checks if cb.isChecked())
        total = len(self._machine_checks)
        self._install_btn.setEnabled(count > 0)
        self._toggle_all_btn.setText(
            _("Deselect all") if count == total else _("Select all")
        )
        self._refresh_category_suggestion()

    def _on_toggle_all(self):
        count = sum(1 for _, cb in self._machine_checks if cb.isChecked())
        select = count < len(self._machine_checks)
        for _, cb in self._machine_checks:
            cb.blockSignals(True)
            cb.setChecked(select)
            cb.blockSignals(False)
        self._on_selection_changed()

    # ── Install ───────────────────────────────────────────────────────────

    def _existing_pack_buttons(self, pack_id: str) -> list:
        """All buttons whose source_pack starts with pack_id (covers
        'linux-defaults', 'linux-defaults#2', etc.)."""
        prefix = pack_id
        return [b for b in self._config.load_buttons()
                if b.source_pack == prefix or b.source_pack.startswith(prefix + "#")]

    def _next_duplicate_marker(self, pack_id: str) -> str:
        """Return the next free 'pack_id#N' suffix. If nothing exists, returns
        'pack_id#2' (the first install is the bare pack_id, the second is #2)."""
        existing_markers = {b.source_pack for b in self._existing_pack_buttons(pack_id)}
        # Highest N found
        max_n = 1  # the bare pack_id counts as #1
        for marker in existing_markers:
            m = re.match(rf"^{re.escape(pack_id)}#(\d+)$", marker)
            if m:
                max_n = max(max_n, int(m.group(1)))
        return f"{pack_id}#{max_n + 1}"

    def _on_install(self):
        pack_id = self._current_pack_id()
        machine_ids = self._selected_machine_ids()
        category = self._cat_edit.text().strip()

        existing = self._existing_pack_buttons(pack_id)
        if existing:
            mode = self._ask_conflict_choice(pack_id, len(existing))
            if mode == "cancel":
                return
        else:
            mode = "first"

        if mode == "replace":
            for btn in existing:
                self._config.delete_button(btn.id)
            marker = pack_id
        elif mode == "duplicate":
            marker = self._next_duplicate_marker(pack_id)
            # Suffix the category for visual separation when both sets coexist.
            m = re.match(r"^(.*)#(\d+)$", marker)
            n = m.group(2) if m else "2"
            category = f"{category} ({n})"
        else:  # first install
            marker = pack_id

        new_buttons = get_pack(pack_id, machine_ids, category, marker)
        for btn in new_buttons:
            self._config.add_button(btn)

        # Refresh main window's grid
        if self.parent() is not None:
            if hasattr(self.parent(), "populate_grid"):
                self.parent().populate_grid()
            if hasattr(self.parent(), "show_toast"):
                self.parent().show_toast(
                    _("Installed {n} buttons").format(n=len(new_buttons))
                )
        self.accept()

    def _ask_conflict_choice(self, pack_id: str, existing_count: int) -> str:
        pack_name = _(PACKS[pack_id].name_key)
        box = QMessageBox(self)
        box.setWindowTitle(_("Pack already installed"))
        box.setIcon(QMessageBox.Question)
        box.setText(_("{name} is already installed.").format(name=pack_name))
        box.setInformativeText(
            _("Replace the existing buttons from this pack ({n}), "
              "or add a second copy with a numbered category?").format(n=existing_count)
        )
        replace_btn = box.addButton(_("Replace existing"), QMessageBox.AcceptRole)
        dup_btn = box.addButton(_("Add as duplicate"), QMessageBox.ActionRole)
        box.addButton(_("Cancel"), QMessageBox.RejectRole)
        box.setDefaultButton(replace_btn)
        box.exec()
        clicked = box.clickedButton()
        if clicked is replace_btn:
            return "replace"
        if clicked is dup_btn:
            return "duplicate"
        return "cancel"
