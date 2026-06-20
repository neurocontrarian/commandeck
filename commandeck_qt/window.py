"""Main application window — PySide6 equivalent of GTK CommandeckWindow."""
from __future__ import annotations

from PySide6.QtCore import Qt, QTimer, QSize, QPoint, QRect, QCoreApplication
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow, QToolBar, QLineEdit, QWidget, QHBoxLayout,
    QScrollArea, QStackedWidget, QLabel, QPushButton,
    QVBoxLayout, QStatusBar, QMenu, QMessageBox,
    QComboBox, QToolButton, QFrame, QRubberBand, QApplication,
)

from commandeck_core.models.config import ConfigManager
from commandeck_core.models.command_button import CommandButton
from commandeck_core.services.executor import ExecutionResult
from commandeck_core.i18n import _
from commandeck_core.utils.exec_log import log as _exec_log, get_log_path as _exec_log_path
from commandeck_core.utils.os_match import os_compatible

from commandeck_qt.button_tile import ButtonTile
from commandeck_qt.flow_layout import FlowLayout
from commandeck_qt.settings import Settings

import os as _os
_QSS_BASE_PATH = _os.path.join(_os.path.dirname(__file__), "resources", "style", "base.qss")

# Theme appearance now lives in commandeck_qt/themes.py (one ThemeSpec per theme).

def _load_base_stylesheet() -> str:
    return open(_QSS_BASE_PATH).read() if _os.path.isfile(_QSS_BASE_PATH) else ""


class _GridWidget(QWidget):
    """Grid container that supports rubber-band drag selection."""

    def __init__(self, window: "CommandeckWindow"):
        super().__init__()
        self._window = window
        self._rubber_band: QRubberBand | None = None
        self._drag_start: QPoint | None = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.childAt(event.position().toPoint()) is None:
            self._drag_start = event.position().toPoint()
            if self._rubber_band is None:
                self._rubber_band = QRubberBand(QRubberBand.Rectangle, self)
            self._rubber_band.setGeometry(QRect(self._drag_start, QSize()))
            self._rubber_band.show()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_start is not None and self._rubber_band:
            self._rubber_band.setGeometry(
                QRect(self._drag_start, event.position().toPoint()).normalized()
            )
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._drag_start is not None and self._rubber_band:
            rect = QRect(self._drag_start, event.position().toPoint()).normalized()
            self._rubber_band.hide()
            self._drag_start = None
            if rect.width() > 5 and rect.height() > 5:
                self._window._on_rubber_band_select(rect)
        super().mouseReleaseEvent(event)


class CommandeckWindow(QMainWindow):
    def __init__(self, config: ConfigManager, platform, parent=None):
        super().__init__(parent)
        self._config = config
        self._platform = platform
        self._settings = Settings()
        self._tiles: dict[str, ButtonTile] = {}
        self._search_text = ""
        self._active_category: str | None = None  # None = All
        self._selected_ids: set[str] = set()
        # None = no free-tier restriction (Pro/trial). Otherwise the set of
        # non-default custom button ids that stay visible under the free limit.
        self._free_visible_ids: set[str] | None = None
        self._current_theme_name = "bold"

        self.setWindowTitle("Commandeck")
        # Re-apply persisted "always on top" before the first show. The menu only
        # reflected the saved setting's checkbox; the flag itself was never applied
        # at startup, so the window wasn't actually on top until toggled.
        if self._settings.get_bool("always-on-top") \
                and self._platform.supports_always_on_top()[0]:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self._restore_size()
        self._build_ui()
        # _apply_theme() stores _current_theme_name; populate_grid() passes it to
        # each tile at construction. Order matters — theme must be set first.
        self._apply_theme()
        self.populate_grid()

        # Defer license/trial checks
        QTimer.singleShot(200, self._check_license_state)

    # ── Window state ───────────────────────────────────────────────────────────

    def _restore_size(self):
        w = self._settings.get_int("window-width")
        h = self._settings.get_int("window-height")
        self.resize(w, h)
        if self._settings.get_bool("window-maximized"):
            self.showMaximized()

    def closeEvent(self, event):
        self._settings.set_bool("window-maximized", self.isMaximized())
        if not self.isMaximized():
            self._settings.set_int("window-width", self.width())
            self._settings.set_int("window-height", self.height())
        super().closeEvent(event)

    # ── UI construction ────────────────────────────────────────────────────────

    def _build_ui(self):
        self._build_toolbar()
        self._build_search_bar()

        # Central stack: grid | empty
        self._stack = QStackedWidget()
        self._build_grid_page()
        self._build_empty_page()

        self._build_selection_bar()

        # Trial banner (hidden until _check_license_state runs)
        self._trial_banner = QLabel()
        self._trial_banner.setAlignment(Qt.AlignCenter)
        self._trial_banner.setStyleSheet(
            "background:#e5a50a; color:#000; padding:4px; font-weight:bold;"
        )
        self._trial_banner.hide()

        # Wrap everything in a vertical layout
        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        vbox.addWidget(self._trial_banner)
        vbox.addWidget(self._search_bar_widget)
        vbox.addWidget(self._stack)
        vbox.addWidget(self._sel_bar)
        self.setCentralWidget(container)

        # Status bar for toasts
        self.statusBar().setSizeGripEnabled(False)

    def _build_toolbar(self):
        tb = QToolBar("Main")
        tb.setMovable(False)
        tb.setFloatable(False)
        self.addToolBar(Qt.TopToolBarArea, tb)

        # Add button
        self._act_add = QAction(_("Add"), self)
        self._act_add.setShortcut(QKeySequence("Ctrl+N"))
        self._act_add.triggered.connect(self._on_add)
        tb.addAction(self._act_add)

        tb.addSeparator()

        # Search toggle
        self._act_search = QAction(_("Search"), self)
        self._act_search.setCheckable(True)
        self._act_search.setShortcut(QKeySequence("Ctrl+F"))
        self._act_search.toggled.connect(self._on_search_toggle)
        tb.addAction(self._act_search)

        # Category filter — a compact dropdown living on the toolbar, on the same
        # line as Search. It replaces the old horizontal pill row, which forced a
        # minimum window width (the row couldn't wrap) and grew ridiculously wide
        # with many categories. The dropdown keeps a constant footprint no matter
        # how many categories exist and lets the window shrink to one column.
        # Hidden until at least one (non-hidden) category exists.
        tb.addSeparator()
        self._cat_combo = QComboBox()
        self._cat_combo.setToolTip(_("Filter by category"))
        self._cat_combo.setMinimumContentsLength(10)
        self._cat_combo.currentIndexChanged.connect(self._on_cat_combo_changed)
        self._cat_combo_action = tb.addWidget(self._cat_combo)
        self._cat_combo_action.setVisible(False)

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(
            spacer.sizePolicy().horizontalPolicy(),
            spacer.sizePolicy().verticalPolicy(),
        )
        from PySide6.QtWidgets import QSizePolicy
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        tb.addWidget(spacer)

        # Hamburger menu
        menu_btn = QToolButton()
        menu_btn.setText("☰")
        menu_btn.setPopupMode(QToolButton.InstantPopup)
        menu = QMenu(self)
        # Refresh: reload the grid from disk without restarting — useful after an
        # AI (MCP) or another process edits buttons.toml. F5 works window-wide
        # (the action is added to the window), and it's also in the menu.
        self._act_refresh = QAction(_("Refresh Buttons"), self)
        self._act_refresh.setShortcut(QKeySequence("F5"))
        self._act_refresh.triggered.connect(self._on_refresh)
        self.addAction(self._act_refresh)
        menu.addAction(self._act_refresh)
        menu.addSeparator()
        menu.addAction(_("Preferences"), self._on_preferences, QKeySequence("Ctrl+,"))
        menu.addAction(_("Manage Machines"), self._on_manage_machines)
        menu.addAction(_("Execution Profiles"), self._on_manage_profiles)
        menu.addAction(_("Variable Values"), self._on_manage_variable_values)
        menu.addAction(_("Button Packs"), self._on_browse_packs)
        menu.addSeparator()
        from commandeck_core.platform import get_platform
        aot_ok, aot_reason = get_platform().supports_always_on_top()
        self._act_always_on_top = QAction(_("Always on Top"), self)
        self._act_always_on_top.setCheckable(True)
        self._act_always_on_top.setChecked(self._settings.get_bool("always-on-top") and aot_ok)
        self._act_always_on_top.setEnabled(aot_ok)
        if not aot_ok:
            # e.g. GNOME/Wayland: the compositor forbids apps from forcing
            # stay-on-top. Disable + explain rather than silently do nothing.
            self._act_always_on_top.setToolTip(aot_reason)
        self._act_always_on_top.toggled.connect(self._on_always_on_top)
        menu.addAction(self._act_always_on_top)
        menu.addSeparator()
        menu.addAction(_("Reset to Defaults"), self._on_reset_to_defaults)
        menu.addAction(_("Restore previous buttons"), self._on_restore_previous_buttons)
        menu.addSeparator()
        menu.addAction(_("Show Execution Log"), self._on_show_execution_log)
        menu.addAction(_("About"), self._on_about)
        menu.addAction(_("Quit"), self.close, QKeySequence("Ctrl+Q"))
        menu_btn.setMenu(menu)
        tb.addWidget(menu_btn)

    def _build_search_bar(self):
        self._search_bar_widget = QWidget()
        self._search_bar_widget.setVisible(False)
        layout = QHBoxLayout(self._search_bar_widget)
        layout.setContentsMargins(8, 4, 8, 4)
        self._search_entry = QLineEdit()
        self._search_entry.setPlaceholderText(_("Search buttons…"))
        self._search_entry.textChanged.connect(self._on_search_changed)
        layout.addWidget(self._search_entry)

    def _build_selection_bar(self):
        from PySide6.QtWidgets import QSizePolicy as SP
        self._sel_bar = QFrame()
        self._sel_bar.setFrameShape(QFrame.StyledPanel)
        self._sel_bar.setVisible(False)
        hbox = QHBoxLayout(self._sel_bar)
        hbox.setContentsMargins(12, 6, 12, 6)
        self._sel_count_lbl = QLabel()
        hbox.addWidget(self._sel_count_lbl)
        hbox.addStretch()
        cat_btn = QPushButton(_("Change category"))
        cat_btn.clicked.connect(self._on_sel_change_category)
        hbox.addWidget(cat_btn)
        machine_btn = QPushButton(_("Change machine"))
        machine_btn.clicked.connect(self._on_sel_change_machine)
        hbox.addWidget(machine_btn)
        export_btn = QPushButton(_("Export as pack"))
        export_btn.clicked.connect(self._on_sel_export_pack)
        hbox.addWidget(export_btn)
        del_btn = QPushButton(_("Delete"))
        del_btn.clicked.connect(self._on_sel_delete)
        hbox.addWidget(del_btn)
        clear_btn = QPushButton("✕")
        clear_btn.setFixedWidth(32)
        clear_btn.clicked.connect(self._clear_selection)
        hbox.addWidget(clear_btn)

    def _build_grid_page(self):
        self._grid_widget = _GridWidget(self)
        self._flow = FlowLayout(self._grid_widget,
                                h_spacing=8, v_spacing=8)
        self._grid_widget.setLayout(self._flow)

        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._grid_widget)
        self._scroll.setFrameShape(QFrame.NoFrame)
        self._stack.addWidget(self._scroll)

    def _build_empty_page(self):
        empty = QWidget()
        vbox = QVBoxLayout(empty)
        vbox.setAlignment(Qt.AlignCenter)
        lbl = QLabel(_("No buttons yet"))
        lbl.setAlignment(Qt.AlignCenter)
        vbox.addWidget(lbl)
        btn = QPushButton(_("Add a button"))
        btn.clicked.connect(self._on_add)
        vbox.addWidget(btn, alignment=Qt.AlignCenter)
        self._stack.addWidget(empty)

    # ── Grid population ────────────────────────────────────────────────────────

    def populate_grid(self):
        # Clear selection before rebuilding tiles
        self._selected_ids.clear()
        self._sel_bar.setVisible(False)
        # Clear existing tiles
        while self._flow.count():
            item = self._flow.takeAt(0)
            if item and item.widget():
                item.widget().deleteLater()
        self._tiles.clear()

        buttons = sorted(self._config.load_buttons(), key=lambda b: b.position)
        size = self._settings.get_str("button-size")

        # Local custom buttons are unlimited for everyone, free included. The
        # Pro gate is on features (SSH, themes, backup, AI…) and on editing the
        # seeded default buttons — never on how many local buttons you create.
        self._free_visible_ids = None

        hidden_cats = self._get_hidden_categories()
        for btn in buttons:
            if not self._matches_filter(btn, hidden_cats):
                continue
            tile = ButtonTile(btn, size=size)
            tile.clicked.connect(lambda b=btn, t=tile: self._on_tile_clicked(b, t))
            tile.rightClicked.connect(lambda pos, b=btn: self._on_tile_right_click(b, pos))
            tile.reordered.connect(self._on_reorder)
            # Add to layout BEFORE apply_theme so any post-attach polish from
            # macOS Cocoa happens first; apply_theme then sets icon tint /
            # shadow on a fully-attached widget.
            self._flow.addWidget(tile)
            tile.apply_theme(self._current_theme_name)
            self._tiles[btn.id] = tile

        has_tiles = bool(self._tiles)
        self._stack.setCurrentIndex(0 if has_tiles else 1)
        self._update_category_bar(buttons, hidden_cats)

    def _matches_filter(self, btn: CommandButton, hidden_cats: set) -> bool:
        # Free-tier: hide custom buttons beyond the limit (defaults always shown).
        if (self._free_visible_ids is not None and not btn.is_default
                and btn.id not in self._free_visible_ids):
            return False
        if btn.category and btn.category in hidden_cats:
            return False
        if self._active_category is not None and btn.category != self._active_category:
            return False
        if self._search_text:
            text = self._search_text.lower()
            if text not in btn.name.lower() and text not in btn.command.lower():
                return False
        return True

    def _get_hidden_categories(self) -> set[str]:
        return set(self._settings.get_strv("hidden-categories"))

    # ── Category bar ──────────────────────────────────────────────────────────

    def _update_category_bar(self, buttons: list[CommandButton], hidden_cats: set):
        cats = sorted({b.category for b in buttons
                       if b.category and b.category not in hidden_cats})

        # Buttons with no category (category == "") get their own "Uncategorized"
        # filter entry instead of only ever hiding inside "All". userData "" targets
        # them without rewriting the button's stored (empty) category.
        has_uncategorized = any(not b.category for b in buttons)

        combo = self._cat_combo
        combo.blockSignals(True)
        combo.clear()
        combo.addItem(_("All"), None)            # userData None = no filter
        for cat in cats:
            combo.addItem(_(cat), cat)            # userData = raw category key
        if has_uncategorized:
            # Same label as the mobile grid's group for cross-platform consistency.
            combo.addItem(_("Uncategorized"), "")  # userData "" = uncategorized only

        # Restore the active selection. If its category vanished (deleted, or
        # hidden via Preferences → Categories), fall back to "All".
        idx = 0
        if self._active_category is not None:
            found = combo.findData(self._active_category)
            if found >= 0:
                idx = found
            else:
                self._active_category = None
        combo.setCurrentIndex(idx)
        combo.blockSignals(False)

        # Only surface the filter when there is something to filter by.
        self._cat_combo_action.setVisible(bool(cats) or has_uncategorized)

    def _on_cat_combo_changed(self, index: int):
        # userData carries the raw (untranslated) category key, None for "All".
        self._active_category = self._cat_combo.itemData(index)
        self.populate_grid()

    # ── Execution ─────────────────────────────────────────────────────────────

    def _on_tile_clicked(self, btn: CommandButton, tile: ButtonTile):
        _exec_log(f"_on_tile_clicked: btn={btn.name!r} id={btn.id}")
        if QApplication.keyboardModifiers() & Qt.ControlModifier:
            _exec_log("  ctrl held -> selection toggle (no execute)")
            if self._is_pro():
                self._toggle_tile_selection(btn.id)
                self._update_selection_ui()
            return
        # Resolve runtime {{variables}} first, so the confirm dialog (and every
        # target machine) sees the real command. Cancelled prompt → abort the run.
        from commandeck_core.models.pack_variables import find_variables, resolve_command
        keys = find_variables(btn.command)
        if keys:
            from commandeck_qt.dialogs.variable_prompt_dialog import prompt_variables
            values = prompt_variables(self, keys, self._config)
            if values is None:
                _exec_log("  variable prompt cancelled")
                return
            btn = resolve_command(btn, values)
        if btn.confirm_before_run:
            from commandeck_qt.dialogs.confirm_dialog import show_confirm_dialog
            confirmed = [False]
            def _do_confirm():
                confirmed[0] = True
            show_confirm_dialog(self, btn, _do_confirm)
            if not confirmed[0]:
                _exec_log("  confirm dialog declined")
                return
        if len(btn.machine_ids) > 1:
            self._pick_machine_and_execute(btn, tile)
        else:
            self._execute(btn, tile)

    def _pick_machine_and_execute(self, btn: CommandButton, tile: ButtonTile):
        from commandeck_qt.dialogs.machine_picker_dialog import show_machine_picker
        options = []
        machines_by_id = {m.id: m for m in self._config.load_machines()}
        for mid in btn.machine_ids:
            if mid == "":
                options.append(("", _("Local"), ""))
            else:
                machine = machines_by_id.get(mid)
                if machine:
                    options.append((mid, machine.name, machine.label))
        if not options:
            self._execute(btn, tile)
            return
        def on_chosen(chosen_ids: list[str]):
            if len(chosen_ids) <= 1:
                for machine_id in chosen_ids:
                    self._execute(btn, tile, machine_id_override=machine_id)
                return
            # Several machines at once: one unified window (selector + arrows)
            # instead of one popup per machine — mirrors the Android behaviour.
            targets = [(mid, self._machine_display_name(mid)) for mid in chosen_ids]
            sink = self._show_multi_output(_(btn.name), targets)
            for machine_id in chosen_ids:
                self._execute(btn, tile, machine_id_override=machine_id,
                              output_sink=sink)
        show_machine_picker(self, options, on_chosen)

    def _get_executor(self):
        """The command executor, built once and reused across clicks (it reads
        timeout/terminal live via the injected callables, so it never goes stale).
        Pro build → CommandExecutorPro; free → CommandExecutor."""
        executor = getattr(self, "_executor", None)
        if executor is None:
            try:
                from commandeck_core.pro.services.executor_pro import CommandExecutorPro
                cls = CommandExecutorPro
            except ImportError:
                from commandeck_core.services.executor import CommandExecutor
                cls = CommandExecutor
            executor = cls(
                self._config,
                get_timeout=self._settings.get_timeout,
                get_terminal=self._settings.get_preferred_terminal,
            )
            self._executor = executor
        return executor

    def _execute(self, btn: CommandButton, tile: ButtonTile, machine_id_override: str | None = None,
                 output_sink=None):
        executor = self._get_executor()

        if machine_id_override is not None:
            machine_id = machine_id_override
        elif len(btn.machine_ids) == 1:
            machine_id = btn.machine_ids[0]
        else:
            machine_id = None
        tile.set_running(True)

        # Treat unset ("") as "output" — legacy buttons created before the default
        # was added would otherwise always run silently with no visible feedback.
        show_output = btn.execution_mode in ("output", "") or btn.show_output
        _exec_log(f"_execute: btn={btn.name!r} machine_id={machine_id!r} show_output={show_output}")

        def on_done(result):
            _exec_log(f"on_done: result_type={type(result).__name__}")
            tile.set_running(False)
            if isinstance(result, Exception):
                _exec_log(f"  exception result: {result}")
                tile.flash_result(False)
                if output_sink is not None:
                    output_sink.set_result(machine_id, result)
                    return
                self.show_toast(f"Error: {result}")
                return
            _exec_log(f"  ExecutionResult: success={result.success} rc={result.return_code} stdout_len={len(result.stdout)} stderr_len={len(result.stderr)} duration_ms={result.duration_ms}")
            tile.flash_result(result.success)
            # Multi-machine run: feed the shared window instead of opening one
            # popup per machine / showing a toast.
            if output_sink is not None:
                _exec_log("  -> routing to unified multi-output window")
                output_sink.set_result(machine_id, result)
                return
            if show_output or not result.success:
                _exec_log("  -> showing output dialog")
                self._show_output(result, _(btn.name), self._machine_display_name(machine_id))
            elif result.success:
                _exec_log("  -> showing success toast")
                self.show_toast(f"✓ {_(btn.name)}")

        # executor.execute() already dispatches to a background thread
        # and calls on_done via the core_threading dispatcher (QTimer.singleShot).
        executor.execute(btn, on_done, machine_id)

    def _machine_display_name(self, machine_id) -> str:
        """Resolve a target id to a header label for the output window.

        "" / None = the local computer (shown as "Local"). A machine UUID is
        looked up in the user's machine list and shown by its configured name.
        Returns "" when the id can't be resolved, so the dialog falls back to a
        plain (machine-less) title.
        """
        if not machine_id:
            return _("Local")
        try:
            machine = self._config.get_machine_by_id(machine_id)
        except Exception:
            machine = None
        return machine.name if machine else ""

    def _show_output(self, result: ExecutionResult, button_name: str = "",
                     machine_name: str = ""):
        from commandeck_qt.dialogs.output_dialog import show_output_dialog
        show_output_dialog(self, button_name or _("Command Output"), result, machine_name)

    def _show_multi_output(self, button_name: str, targets: list[tuple[str, str]]):
        """Open one window aggregating a multi-machine run and return it as the
        output sink. A strong reference is kept until the window closes so it is
        not garbage-collected once the spawning callbacks have run."""
        from commandeck_qt.dialogs.output_dialog import MultiOutputDialog
        if not hasattr(self, "_open_output_dialogs"):
            self._open_output_dialogs = []
        dlg = MultiOutputDialog(self, button_name, targets)
        self._open_output_dialogs.append(dlg)
        dlg.finished.connect(
            lambda _result, d=dlg: self._open_output_dialogs.remove(d)
            if d in self._open_output_dialogs else None)
        dlg.show()
        return dlg

    # ── Context menu ──────────────────────────────────────────────────────────

    def _on_tile_right_click(self, btn: CommandButton, pos: QPoint):
        menu = QMenu(self)
        menu.addAction(_("Edit"), lambda: self._on_edit(btn))
        menu.addAction(_("Duplicate"), lambda: self._on_duplicate(btn))
        # "Move to category" — quick assignment to an existing category.
        categories = sorted({b.category for b in self._config.load_buttons()
                             if b.category and b.category != btn.category})
        if categories:
            move_menu = menu.addMenu(_("Move to category"))
            for cat in categories:
                move_menu.addAction(_(cat), lambda c=cat: self._assign_category(btn, c))
        menu.addSeparator()
        menu.addAction(_("Delete"), lambda: self._on_delete(btn))
        menu.exec(pos)

    def _on_refresh(self):
        """Reload buttons (and the category bar) from disk — F5 / menu.

        populate_grid() re-reads buttons.toml on every call, so this picks up
        changes made outside the running app (e.g. by the MCP server) without a
        restart. Preserves the active category/search filter.
        """
        self.populate_grid()

    def _assign_category(self, btn: CommandButton, category: str):
        buttons = self._config.load_buttons()
        for b in buttons:
            if b.id == btn.id:
                b.category = category
                break
        self._config.save_buttons(buttons)
        self.populate_grid()

    def _on_reorder(self, dragged_id: str, target_id: str):
        """Swap the positions of two buttons (drag-and-drop reorder)."""
        buttons = self._config.load_buttons()
        dragged = next((b for b in buttons if b.id == dragged_id), None)
        target = next((b for b in buttons if b.id == target_id), None)
        if dragged is None or target is None:
            return
        dragged.position, target.position = target.position, dragged.position
        self._config.save_buttons(buttons)
        self.populate_grid()

    # ── CRUD ──────────────────────────────────────────────────────────────────

    def _on_add(self):
        from commandeck_qt.dialogs.command_dialog import show_command_dialog
        result = show_command_dialog(self._config, parent=self)
        if result:
            self.populate_grid()

    def _on_edit(self, btn: CommandButton):
        # Editing any button (defaults included) is free — custom buttons are already
        # unlimited and editable, so locking default edits was a petty, bypassable
        # gate (2026-06-18). The real Pro boundary is SSH/AI/power features.
        from commandeck_qt.dialogs.command_dialog import show_command_dialog
        result = show_command_dialog(self._config, command_button=btn, parent=self)
        if result:
            self.populate_grid()

    def _on_duplicate(self, btn: CommandButton):
        import uuid
        import dataclasses
        buttons = self._config.load_buttons()
        new_btn = dataclasses.replace(
            btn,
            id=str(uuid.uuid4()),
            name=f"{_(btn.name)} (copy)",
            position=max((b.position for b in buttons), default=0) + 1,
            is_default=False,
        )
        self._config.add_button(new_btn)
        self.populate_grid()

    def _on_delete(self, btn: CommandButton):
        answer = QMessageBox.question(
            self,
            _("Delete button"),
            f"{_('Delete')} '{_(btn.name)}'?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            self._config.delete_button(btn.id)
            self.populate_grid()

    # ── Toolbar actions ───────────────────────────────────────────────────────

    def _on_search_toggle(self, checked: bool):
        self._search_bar_widget.setVisible(checked)
        if checked:
            self._search_entry.setFocus()
        else:
            self._search_entry.clear()

    def _on_search_changed(self, text: str):
        self._search_text = text
        self.populate_grid()

    def _on_always_on_top(self, checked: bool):
        self._settings.set_bool("always-on-top", checked)
        flags = self.windowFlags()
        if checked:
            self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(flags & ~Qt.WindowStaysOnTopHint)
        self.show()

    def _show_pro_limit_dialog(self, message: str) -> None:
        QMessageBox.information(self, _("Commandeck Pro"), message)

    def _on_preferences(self):
        from commandeck_qt.dialogs.preferences_dialog import show_preferences_dialog
        # Non-modal: the dialog itself refreshes us via its finished signal
        # (see show_preferences_dialog). Calling _apply_theme/populate_grid
        # here would fire immediately after show(), before any user change.
        show_preferences_dialog(self._config, self._settings, parent=self)

    def _require_pro(self, message: str) -> bool:
        """True if Pro is active; otherwise show the upgrade dialog and return False.
        On a free build the pro module is absent (ImportError) → treat as not-Pro
        and show the upgrade dialog, so the action is blocked cleanly instead of
        proceeding into a pro-only dialog that would crash on import."""
        try:
            from commandeck_core.pro.license import is_pro_active
            if is_pro_active():
                return True
        except ImportError:
            pass
        self._show_pro_limit_dialog(message)
        return False

    def _on_manage_machines(self):
        if not self._require_pro(
            _("Manage Machines requires Commandeck Pro.\n\n"
              "Upgrade to add SSH machines and run commands remotely.")):
            return
        from commandeck_qt.dialogs.machines_list_dialog import show_machines_list_dialog
        show_machines_list_dialog(self._config, parent=self)

    def _on_manage_profiles(self):
        if not self._require_pro(
            _("Execution Profiles require Commandeck Pro.\n\n"
              "Upgrade to save reusable run-as user and working-directory settings.")):
            return
        from commandeck_qt.dialogs.profiles_list_dialog import show_profiles_list_dialog
        show_profiles_list_dialog(self._config, parent=self)

    def _on_browse_packs(self):
        # Option 1 (2026-06-15): the gallery is free to open + install (Local).
        # The SSH/remote target stays Pro, enforced structurally (free has no
        # machines) + nudged with the trial inside the install step.
        from commandeck_qt.dialogs.pack_gallery_dialog import show_pack_gallery_dialog
        show_pack_gallery_dialog(self._config, parent=self)

    def _on_manage_variable_values(self):
        from commandeck_qt.dialogs.variable_values_dialog import show_variable_values_dialog
        show_variable_values_dialog(self._config, parent=self)

    def _on_sel_export_pack(self):
        # Export the lasso-selected buttons as a community pack (the buttons are
        # chosen by the selection, so the dialog only asks for the pack metadata).
        buttons = [b for b in self._config.load_buttons() if b.id in self._selected_ids]
        if not buttons:
            return
        from commandeck_qt.dialogs.pack_export_dialog import show_pack_export_dialog
        show_pack_export_dialog(self._config, buttons, parent=self)

    def _on_about(self):
        QMessageBox.about(
            self,
            "Commandeck",
            f"<b>Commandeck {QCoreApplication.applicationVersion()}</b><br>"
            "A cross-platform graphical remote control for your local &amp; "
            "remote commands.<br><br>"
            "© 2026 neurocontrarian<br>"
            + _("Provided \"as is\", without warranty of any kind.") + "<br>"
            + _("Free software under the GNU AGPLv3.") + " "
            '<a href="https://github.com/neurocontrarian/commandeck">'
            + _("Source code") + "</a><br><br>"
            '<a href="https://commandeck.app/legal/terms/">'
            + _("Terms") + "</a> &middot; "
            '<a href="https://commandeck.app/legal/privacy/">'
            + _("Privacy") + "</a> &middot; "
            '<a href="https://commandeck.app/legal/refund/">'
            + _("Refund") + "</a><br><br>"
            '<a href="https://github.com/neurocontrarian/commandeck/blob/main/THIRD_PARTY_LICENSES.md">'
            + _("Third-party licenses") + "</a>",
        )

    def _on_reset_to_defaults(self):
        reply = QMessageBox.question(
            self,
            _("Reset to Defaults"),
            _("This will replace all buttons with the default set for your platform.\n"
              "Your current buttons will be backed up.\n\nContinue?"),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        backup = self._config.reset_buttons_to_defaults()
        self.populate_grid()
        if backup:
            QMessageBox.information(
                self, _("Reset to Defaults"),
                _("Done. Your previous buttons were backed up to:\n{path}").format(path=backup),
            )
        else:
            QMessageBox.information(self, _("Reset to Defaults"), _("Default buttons restored."))

    def _on_restore_previous_buttons(self):
        """Restore the most recent buttons backup (created on reset or import).
        Mirrors the mobile Settings → Setup action."""
        if not self._config.list_button_backups():
            QMessageBox.information(
                self, _("Restore previous buttons"),
                _("No previous buttons to restore yet. A backup is made when you "
                  "reset to defaults or import."))
            return
        reply = QMessageBox.question(
            self, _("Restore previous buttons"),
            _("Restore your buttons from the most recent backup? "
              "This replaces the current buttons."),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        if self._config.restore_last_button_backup():
            self.populate_grid()
            QMessageBox.information(
                self, _("Restore previous buttons"), _("Previous buttons restored."))

    def _on_show_execution_log(self):
        """Open a dialog with the contents of execution.log (last button-click trace)."""
        path = _exec_log_path()
        if path is None or not path.exists():
            QMessageBox.information(
                self, _("Execution Log"),
                _("No log file yet. Click a button first to generate trace output."),
            )
            return
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            QMessageBox.warning(self, _("Execution Log"), f"Cannot read log: {e}")
            return
        dlg = QMessageBox(self)
        dlg.setWindowTitle(_("Execution Log"))
        dlg.setText(str(path))
        dlg.setDetailedText(content or "(empty)")
        # QMessageBox detail viewer is small; resize the underlying text edit.
        from PySide6.QtWidgets import QTextEdit
        for child in dlg.findChildren(QTextEdit):
            child.setMinimumSize(700, 400)
            child.setLineWrapMode(QTextEdit.NoWrap)
        dlg.exec()

    # ── License / trial ───────────────────────────────────────────────────────

    def _check_license_state(self):
        """Reflect the current license/trial state in the persistent top banner."""
        try:
            from commandeck_core.pro.license import get_trial_info, get_license_info
            lic = get_license_info()
            if lic.get("key"):
                # Paid license: persistent notice on imminent expiry / once expired.
                if lic.get("is_expired"):
                    self._show_banner(_("Pro license expired — free tier limits now apply"))
                elif lic.get("expiry_warning"):
                    self._show_banner(
                        _("Pro license expires in {days} days — renew in Preferences").format(
                            days=lic.get("days_until_expiry", 0)))
                return
            info = get_trial_info()
            if info.get("active"):
                days = info.get("days_remaining", 0)
                if days <= 3:
                    self._show_banner(
                        _("Trial expires in {days} day(s) — upgrade to keep Pro access").format(
                            days=days))
                else:
                    self._show_banner(_("Pro trial — {days} day(s) remaining").format(days=days))
            elif info.get("started_at"):
                # Trial fully used and no license → free-tier limits now apply.
                self._show_banner(_("Pro trial ended — free tier limits now apply"))
        except Exception:
            pass

    def _show_banner(self, text: str) -> None:
        """Persistent top banner for license/trial state — stays until the next check."""
        self._trial_banner.setText(text)
        self._trial_banner.show()

    # ── Theme ─────────────────────────────────────────────────────────────────

    def _apply_theme(self):
        self._current_theme_name = self._settings.get_str("button-theme") or "bold"
        # Custom button themes are a Pro feature. In the free tier (or if a
        # non-default value lingers in QSettings from a prior Pro/trial run),
        # force the default "bold" theme so the rendered grid matches the
        # disabled "Bold (default)" selector in Preferences.
        if not self._is_pro():
            self._current_theme_name = "bold"
        # base.qss is the only app-level stylesheet. Theme QSS lives at widget
        # level and reaches child QLabels via AA_UseStyleSheetPropagationInWidgetStyles
        # (set in app.py before QApplication construction).
        QApplication.instance().setStyleSheet(_load_base_stylesheet())
        for tile in self._tiles.values():
            tile.apply_theme(self._current_theme_name)

    # ── Pro helpers ───────────────────────────────────────────────────────────

    def _is_pro(self) -> bool:
        try:
            from commandeck_core.pro.license import is_pro_active
            return is_pro_active()
        except ImportError:
            return False

    # ── Multi-select ──────────────────────────────────────────────────────────

    def _toggle_tile_selection(self, btn_id: str):
        tile = self._tiles.get(btn_id)
        if tile is None:
            return
        if btn_id in self._selected_ids:
            self._selected_ids.discard(btn_id)
            tile.set_selected(False)
        else:
            self._selected_ids.add(btn_id)
            tile.set_selected(True)

    def _clear_selection(self):
        for btn_id in list(self._selected_ids):
            tile = self._tiles.get(btn_id)
            if tile:
                tile.set_selected(False)
        self._selected_ids.clear()
        self._update_selection_ui()

    def _update_selection_ui(self):
        n = len(self._selected_ids)
        self._sel_bar.setVisible(n > 0)
        if n > 0:
            self._sel_count_lbl.setText(_(f"{n} selected"))

    def _on_rubber_band_select(self, rect: QRect):
        if not self._is_pro():
            return
        for btn_id, tile in self._tiles.items():
            tile_rect = QRect(tile.pos(), tile.size())
            if rect.intersects(tile_rect):
                if btn_id not in self._selected_ids:
                    self._selected_ids.add(btn_id)
                    tile.set_selected(True)
        self._update_selection_ui()

    def _on_sel_change_category(self):
        from PySide6.QtWidgets import QInputDialog
        cat, ok = QInputDialog.getText(self, _("Change category"), _("New category name:"))
        if not ok:
            return
        buttons = self._config.load_buttons()
        for btn in buttons:
            if btn.id in self._selected_ids:
                btn.category = cat
                self._config.update_button(btn)
        self._clear_selection()
        self.populate_grid()

    def _on_sel_change_machine(self):
        machines = self._config.load_machines()
        if not machines:
            self.show_toast(_("No machines configured"))
            return
        chosen = self._pick_machines_multi(machines)
        if chosen is None:
            return  # cancelled
        local = "" in chosen
        picked = [m for m in machines if m.id in chosen]
        ids = set(self._selected_ids)
        buttons = self._config.load_buttons()
        skipped = 0
        for btn in buttons:
            if btn.id not in ids:
                continue
            # Keep only OS-compatible machines (+ Local if chosen). machine_ids:
            # [] = Local only; ["",id…] = Local + machines (picker at run time).
            compat = [m.id for m in picked if os_compatible(btn.os, m.os)]
            new_ids = ([""] if local else []) + compat
            if not new_ids and not local and picked:
                skipped += 1  # all chosen machines incompatible with this button's OS
                continue
            btn.machine_ids = new_ids
        self._config.save_buttons(buttons)
        self._clear_selection()
        self.populate_grid()
        if skipped:
            self.show_toast(_("Skipped {n} button(s) not compatible with this "
                              "machine's OS.").format(n=skipped))

    def _pick_machines_multi(self, machines) -> list | None:
        """Multi-select dialog (Local + each machine). Returns the chosen ids
        ("" = Local), or None if cancelled."""
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QCheckBox, QDialogButtonBox, QLabel
        dlg = QDialog(self)
        dlg.setWindowTitle(_("Change machine"))
        v = QVBoxLayout(dlg)
        v.addWidget(QLabel(_("Assign the selected buttons to one or more machines.")))
        checks: list[tuple[str, QCheckBox]] = []
        local_cb = QCheckBox(_("Local (no machine)"))
        v.addWidget(local_cb)
        checks.append(("", local_cb))
        for m in machines:
            cb = QCheckBox(f"{m.name} ({m.label})")
            v.addWidget(cb)
            checks.append((m.id, cb))
        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(dlg.accept)
        bb.rejected.connect(dlg.reject)
        v.addWidget(bb)
        if dlg.exec() != QDialog.Accepted:
            return None
        return [mid for mid, cb in checks if cb.isChecked()]

    def _on_sel_delete(self):
        n = len(self._selected_ids)
        answer = QMessageBox.question(
            self,
            _("Delete buttons"),
            _(f"Delete {n} selected button(s)?"),
            QMessageBox.Yes | QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            for btn_id in list(self._selected_ids):
                self._config.delete_button(btn_id)
            self._clear_selection()
            self.populate_grid()

    # ── Toasts ────────────────────────────────────────────────────────────────

    def show_toast(self, message: str, duration_ms: int = 3000):
        self.statusBar().showMessage(message, duration_ms)
