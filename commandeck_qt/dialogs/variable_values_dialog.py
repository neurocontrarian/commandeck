"""Manage saved values for command `{{variables}}` (desktop).

Like "Manage Machines", but for variable choices: e.g. service → [jellyfin, sonarr].
These choices are offered when you insert a variable into a button (you can freeze one)
and at run time (a dropdown + manual entry). Stored via ConfigManager.save_variable_values.
"""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QListWidget, QPushButton,
    QDialogButtonBox, QInputDialog,
)

from commandeck_core.models.config import ConfigManager
from commandeck_core.models.pack_variables import standard_keys
from commandeck_core.i18n import _


def show_variable_values_dialog(config: ConfigManager, parent=None) -> None:
    _VariableValuesDialog(config, parent).exec()


class _VariableValuesDialog(QDialog):
    def __init__(self, config: ConfigManager, parent=None):
        super().__init__(parent)
        self._config = config
        self.setWindowTitle(_("Variable Values"))
        self.resize(420, 420)
        # Working copy: variable key → list of values.
        self._values: dict[str, list[str]] = config.load_variable_values()

        vbox = QVBoxLayout(self)
        vbox.addWidget(QLabel(_("Saved values offered when you use a variable in a "
                                "button (and at run time).")))

        row = QHBoxLayout()
        row.addWidget(QLabel(_("Variable")))
        self._combo = QComboBox()
        # Only the authorized (standard) variables — no creating arbitrary keys.
        self._combo.addItems(standard_keys())
        self._combo.currentTextChanged.connect(self._refresh_list)
        row.addWidget(self._combo, 1)
        vbox.addLayout(row)

        self._list = QListWidget()
        vbox.addWidget(self._list, 1)

        btns = QHBoxLayout()
        add = QPushButton(_("Add value"))
        add.clicked.connect(self._on_add)
        rem = QPushButton(_("Remove"))
        rem.clicked.connect(self._on_remove)
        btns.addWidget(add)
        btns.addWidget(rem)
        btns.addStretch(1)
        vbox.addLayout(btns)

        bb = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        bb.accepted.connect(self._on_save)
        bb.rejected.connect(self.reject)
        vbox.addWidget(bb)

        self._refresh_list()

    def _key(self) -> str:
        return self._combo.currentText().strip()

    def _refresh_list(self):
        self._list.clear()
        for v in self._values.get(self._key(), []):
            self._list.addItem(v)

    def _on_add(self):
        key = self._key()
        if not key:
            return
        text, ok = QInputDialog.getText(self, _("Add value"),
                                        _("Value for {key}").format(key=key))
        text = text.strip()
        if ok and text:
            self._values.setdefault(key, [])
            if text not in self._values[key]:
                self._values[key].append(text)
            self._refresh_list()

    def _on_remove(self):
        item = self._list.currentItem()
        if item is None:
            return
        key = self._key()
        if key in self._values and item.text() in self._values[key]:
            self._values[key].remove(item.text())
        self._refresh_list()

    def _on_save(self):
        self._config.save_variable_values(self._values)
        self.accept()
