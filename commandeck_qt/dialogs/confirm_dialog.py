"""Confirmation dialog before running a command."""
from __future__ import annotations

from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QSpacerItem, QSizePolicy, QGridLayout

from commandeck_core.models.command_button import CommandButton
from commandeck_core.i18n import _


def show_confirm_dialog(parent, button: CommandButton, on_confirm: Callable) -> None:
    # No parent → a free-floating top-level window (detached from the main window),
    # still application-modal so it blocks input until answered.
    box = QMessageBox(None)
    box.setWindowModality(Qt.ApplicationModal)
    box.setWindowTitle(_("Run command?"))
    box.setText(f'{_("Run")} "{_(button.name)}"?')
    box.setInformativeText(button.command)
    # Force a comfortable minimum width so a long name/command isn't truncated
    # (QMessageBox otherwise sizes to its short default). The spacer in the last
    # grid row is the standard Qt way to widen a QMessageBox.
    layout = box.layout()
    if isinstance(layout, QGridLayout):
        layout.addItem(
            QSpacerItem(460, 0, QSizePolicy.Minimum, QSizePolicy.Expanding),
            layout.rowCount(), 0, 1, layout.columnCount())
    # Verb buttons (Apple HIG: avoid Yes/No) — matches the mobile dialog.
    run_btn = box.addButton(_("Run"), QMessageBox.AcceptRole)
    box.addButton(_("Cancel"), QMessageBox.RejectRole)
    box.setDefaultButton(run_btn)
    box.exec()
    if box.clickedButton() is run_btn:
        on_confirm()
