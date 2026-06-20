"""Export the lasso-selected buttons as a shareable button pack (a `.zip`).

A community pack is **unsigned** (only the maintainer signs official packs). The file is a
plain **`.zip`** holding `pack.toml` — GitHub accepts `.zip` attachments, so it drops
straight into the "Submit a pack" issue form (a `.cdpack` would be refused as an unknown
type). Submitting it to the official gallery is a separate, deliberate GitHub step (link in
the window) — there is no in-app one-tap submit.
"""
from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QLineEdit, QDialogButtonBox,
    QFileDialog, QMessageBox, QFrame,
)

from commandeck_core.models.config import ConfigManager
from commandeck_core.models.pack_format import write_cdpack
from commandeck_core.services.pack_service import serialize_pack
from commandeck_core.i18n import _

# The packs GitHub (catalogue + how to contribute + the submission issue form).
_PACKS_URL = "https://github.com/neurocontrarian/commandeck-packs"
_CONTRIB_URL = "https://github.com/neurocontrarian/commandeck-packs/blob/main/CONTRIBUTING.md"
_SUBMIT_URL = "https://github.com/neurocontrarian/commandeck-packs/issues/new?template=submit-pack.yml"


def show_pack_export_dialog(config: ConfigManager, buttons: list, parent=None) -> bool:
    """Modal. ``buttons`` = the selected buttons to pack. Returns True if written."""
    return _PackExportDialog(config, buttons, main_window=parent).exec() == QDialog.Accepted


class _PackExportDialog(QDialog):
    def __init__(self, config: ConfigManager, buttons: list, main_window=None):
        # No parent → a free-floating top-level window (detached from the main window),
        # still application-modal.
        super().__init__(None)
        self.setWindowModality(Qt.ApplicationModal)
        self._config = config
        self._buttons = buttons
        self._main_window = main_window
        self.setWindowTitle(_("Export as pack"))
        self.resize(500, 380)

        vbox = QVBoxLayout(self)

        form = QFormLayout()
        self._f_id = QLineEdit()
        self._f_id.setPlaceholderText("my-pack")
        self._f_name = QLineEdit()
        self._f_desc = QLineEdit()
        self._f_cat = QLineEdit()
        self._f_tags = QLineEdit()
        self._f_tags.setPlaceholderText(_("comma,separated"))
        self._f_ver = QLineEdit("1.0.0")
        form.addRow(_("Pack id"), self._f_id)
        form.addRow(_("Name"), self._f_name)
        form.addRow(_("Description"), self._f_desc)
        form.addRow(_("Category"), self._f_cat)
        form.addRow(_("Tags"), self._f_tags)
        form.addRow(_("Version"), self._f_ver)
        vbox.addLayout(form)

        included = QLabel(_("Including {n} button(s): {names}").format(
            n=len(buttons), names=", ".join(b.name for b in buttons)))
        included.setWordWrap(True)
        included.setFrameShape(QFrame.StyledPanel)
        vbox.addWidget(included)

        # Real-looking hyperlinks (so it's clear they're clickable). linkActivated is
        # routed through the platform browser opener — never QDesktopServices/xdg-open.
        links = QLabel(
            _("Share it, or add it to the gallery:") + "  "
            + f'<a href="{_SUBMIT_URL}">' + _("Submit a pack") + "</a>"
            + "  ·  " + f'<a href="{_PACKS_URL}">' + _("Packs on GitHub") + "</a>"
            + "  ·  " + f'<a href="{_CONTRIB_URL}">' + _("Contribution guide") + "</a>")
        links.setTextFormat(Qt.RichText)
        links.setOpenExternalLinks(False)
        links.setWordWrap(True)
        links.linkActivated.connect(self._open)
        vbox.addWidget(links)

        bb = QDialogButtonBox()
        export = bb.addButton(_("Export…"), QDialogButtonBox.AcceptRole)
        bb.addButton(_("Cancel"), QDialogButtonBox.RejectRole)
        export.clicked.connect(self._on_export)
        bb.rejected.connect(self.reject)
        vbox.addWidget(bb)

    def _open(self, url: str):
        try:
            self._main_window._platform.open_browser(url)
        except Exception:
            pass

    def _on_export(self):
        pack_id = self._f_id.text().strip()
        name = self._f_name.text().strip()
        if not pack_id or not name:
            QMessageBox.warning(self, _("Export as pack"),
                                _("Please enter a pack id and a name."))
            return
        meta = {
            "pack_id": pack_id, "name": name, "pack_ver": self._f_ver.text().strip() or "1.0.0",
            "category": self._f_cat.text().strip(), "description": self._f_desc.text().strip(),
            "tags": [t.strip() for t in self._f_tags.text().split(",") if t.strip()],
        }
        path, _filter = QFileDialog.getSaveFileName(
            self, _("Export as pack"), f"{pack_id}.zip",
            _("Zip archive (*.zip)"))
        if not path:
            return
        try:
            Path(path).write_bytes(write_cdpack(serialize_pack(meta, self._buttons)))
        except OSError as e:
            QMessageBox.critical(self, _("Export as pack"),
                                 _("Could not write the file:\n{error}").format(error=e))
            return
        box = QMessageBox(self)
        box.setWindowTitle(_("Export as pack"))
        box.setText(_("Pack exported as a .zip. Share the file, or submit it to the "
                      "official gallery (opens the submission form on GitHub)."))
        submit = box.addButton(_("Submit this pack…"), QMessageBox.ActionRole)
        box.addButton(_("Done"), QMessageBox.AcceptRole)
        box.exec()
        if box.clickedButton() is submit:
            self._open(_SUBMIT_URL)
        self.accept()
