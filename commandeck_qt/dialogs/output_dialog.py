"""Output dialog — displays stdout/stderr of a completed command.

Two flavours:
- ``show_output_dialog`` — a single window for one (button, machine) result.
- ``MultiOutputDialog`` — one window aggregating several machines for a
  multi-machine run, paged with a machine selector + ◀ ▶ arrows (mirrors the
  Android single-window behaviour instead of one popup per machine).
"""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPlainTextEdit,
    QLabel, QDialogButtonBox, QFrame, QStackedWidget, QComboBox,
    QToolButton, QWidget,
)

from commandeck_core.services.executor import ExecutionResult, combined_output
from commandeck_core.i18n import _


def _format_output(result: ExecutionResult) -> str:
    """stdout + (optionally) a translated stderr separator + stderr."""
    return combined_output(result)


def _status_text(result: ExecutionResult) -> str:
    icon = "✓" if result.success else "✗"
    return f"{icon}  " + _("Exit code {code} — {ms} ms").format(
        code=result.return_code, ms=result.duration_ms)


def _make_output_view() -> QPlainTextEdit:
    text_edit = QPlainTextEdit()
    text_edit.setReadOnly(True)
    # "Monospace" is an X11/fontconfig alias that does not exist on Windows or
    # macOS, where it silently falls back to a proportional font and breaks
    # column alignment of Format-Table / df output. Use the platform's real
    # fixed-pitch font (Consolas, Menlo, DejaVu Sans Mono, …).
    mono = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    mono.setPointSize(10)
    mono.setStyleHint(QFont.Monospace)
    text_edit.setFont(mono)
    # Never word-wrap fixed-width tables — let the user scroll horizontally.
    text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
    return text_edit


def show_output_dialog(parent, button_name: str, result: ExecutionResult,
                       machine_name: str = "") -> None:
    dlg = QDialog(parent)
    # Show which machine the command ran on, both in the title bar and as a
    # header inside the window (empty machine_name = no header / plain title).
    title = _(button_name)
    if machine_name:
        title = f"{title} — {machine_name}"
    dlg.setWindowTitle(title)
    dlg.resize(640, 440)
    dlg.setAttribute(Qt.WA_DeleteOnClose)

    vbox = QVBoxLayout(dlg)
    vbox.setContentsMargins(12, 12, 12, 8)
    vbox.setSpacing(8)

    if machine_name:
        machine_lbl = QLabel(machine_name)
        mf = machine_lbl.font()
        mf.setBold(True)
        mf.setPointSize(mf.pointSize() + 1)
        machine_lbl.setFont(mf)
        vbox.addWidget(machine_lbl)

    text_edit = _make_output_view()
    text_edit.setPlainText(_format_output(result))
    vbox.addWidget(text_edit)

    sep = QFrame()
    sep.setFrameShape(QFrame.HLine)
    sep.setFrameShadow(QFrame.Sunken)
    vbox.addWidget(sep)

    vbox.addWidget(QLabel(_status_text(result)))

    bb = QDialogButtonBox(QDialogButtonBox.Close)
    bb.rejected.connect(dlg.accept)
    vbox.addWidget(bb)

    dlg.show()


class MultiOutputDialog(QDialog):
    """One window holding the results of running a button on several machines.

    Built up-front with one page per target (each showing "Running…"); each
    page is filled in as its execution finishes via :meth:`set_result`. The
    user moves between machines with the combo selector or the ◀ ▶ arrows.
    """

    def __init__(self, parent, button_name: str,
                 targets: list[tuple[str, str]]):
        super().__init__(parent)
        self.setWindowTitle(_(button_name))
        self.resize(660, 480)

        self._machine_ids: list[str] = []
        self._pages: list[dict] = []
        self._names: list[str] = []

        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(12, 12, 12, 8)
        vbox.setSpacing(8)

        # Header: ◀  [machine selector]  ▶
        header = QHBoxLayout()
        header.setSpacing(6)
        self._prev_btn = QToolButton()
        self._prev_btn.setText("◀")
        self._prev_btn.setAutoRaise(True)
        self._prev_btn.clicked.connect(lambda: self._step(-1))
        self._next_btn = QToolButton()
        self._next_btn.setText("▶")
        self._next_btn.setAutoRaise(True)
        self._next_btn.clicked.connect(lambda: self._step(1))
        self._combo = QComboBox()
        self._combo.currentIndexChanged.connect(self._on_combo_changed)
        header.addWidget(self._prev_btn)
        header.addWidget(self._combo, 1)
        header.addWidget(self._next_btn)
        vbox.addLayout(header)

        self._stack = QStackedWidget()
        vbox.addWidget(self._stack, 1)

        for machine_id, name in targets:
            self._add_page(machine_id, name)

        bb = QDialogButtonBox(QDialogButtonBox.Close)
        bb.rejected.connect(self.accept)
        vbox.addWidget(bb)

        self._sync_nav()

    def _add_page(self, machine_id: str, name: str) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        text_edit = _make_output_view()
        text_edit.setPlainText(_("Running…"))
        layout.addWidget(text_edit)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)
        layout.addWidget(sep)

        status_lbl = QLabel("…  " + _("Running…"))
        layout.addWidget(status_lbl)

        self._stack.addWidget(page)
        self._machine_ids.append(machine_id)
        self._names.append(name)
        self._pages.append({"text": text_edit, "status": status_lbl})
        self._combo.addItem(f"…  {name}")

    def set_result(self, machine_id: str, result) -> None:
        """Fill the page for ``machine_id`` with its result (or an Exception)."""
        try:
            index = self._machine_ids.index(machine_id)
        except ValueError:
            return
        page = self._pages[index]
        name = self._names[index]
        if isinstance(result, Exception):
            glyph = "✗"
            page["text"].setPlainText(f"{_('Error')}: {result}")
            page["status"].setText(f"✗  {_('Error')}")
        else:
            glyph = "✓" if result.success else "✗"
            page["text"].setPlainText(_format_output(result))
            page["status"].setText(_status_text(result))
        self._combo.setItemText(index, f"{glyph}  {name}")

    # ── Navigation ──────────────────────────────────────────────────────────

    def _on_combo_changed(self, index: int) -> None:
        if 0 <= index < self._stack.count():
            self._stack.setCurrentIndex(index)
            self._sync_nav()

    def _step(self, delta: int) -> None:
        self._combo.setCurrentIndex(
            max(0, min(self._combo.count() - 1, self._combo.currentIndex() + delta)))

    def _sync_nav(self) -> None:
        index = self._combo.currentIndex()
        self._prev_btn.setEnabled(index > 0)
        self._next_btn.setEnabled(index < self._combo.count() - 1)
