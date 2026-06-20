"""Ask for a command's runtime `{{variables}}` just before it runs (desktop).

Values are used for this run only — never stored. If the user has saved choices for a
variable (ConfigManager.load_variable_values, managed via "Variable Values…"), the field
is an editable dropdown of those choices; otherwise a plain text box. Manual entry is
always possible.
"""
from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QComboBox, QDialogButtonBox,
)

from commandeck_core.models.pack_variables import spec_for
from commandeck_core.i18n import _


def prompt_variables(parent, keys: list[str], config=None) -> dict | None:
    """Modal. Returns {key: value} for ``keys``, or None if cancelled."""
    saved = {}
    if config is not None:
        try:
            saved = config.load_variable_values()
        except Exception:
            saved = {}

    dlg = QDialog(parent)
    dlg.setWindowTitle(_("Fill in the command"))
    vbox = QVBoxLayout(dlg)
    vbox.addWidget(QLabel(_("This button needs a few values before it runs:")))

    form = QFormLayout()
    getters: dict[str, callable] = {}
    first = None
    for key in keys:
        spec = spec_for(key)
        values = saved.get(key, [])
        if values:
            combo = QComboBox()
            combo.setEditable(True)              # editable → manual entry still works
            combo.addItems(values)
            combo.setCurrentText("")
            form.addRow(_(spec["label"]), combo)
            getters[key] = (lambda c=combo: c.currentText().strip())
            widget = combo
        else:
            edit = QLineEdit()
            edit.setPlaceholderText(_(spec["prompt"]))
            form.addRow(_(spec["label"]), edit)
            getters[key] = (lambda e=edit: e.text())
            widget = edit
        if first is None:
            first = widget
    vbox.addLayout(form)

    bb = QDialogButtonBox()
    run = bb.addButton(_("Run"), QDialogButtonBox.AcceptRole)
    bb.addButton(_("Cancel"), QDialogButtonBox.RejectRole)
    run.clicked.connect(dlg.accept)
    bb.rejected.connect(dlg.reject)
    vbox.addWidget(bb)

    if first is not None:
        first.setFocus()
    if dlg.exec() != QDialog.Accepted:
        return None
    return {key: getter() for key, getter in getters.items()}
