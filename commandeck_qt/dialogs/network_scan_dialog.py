"""Detect SSH machines on the local network and add them.

Scans the local /24 for hosts with port 22 open (the shared, UI-agnostic
:mod:`commandeck_core.pro.services.network_scan` service), lists the ones found,
and — on selection — opens the normal Add-Machine form pre-filled with host/name.
Already-configured hosts are hidden so only new machines are proposed.
"""
from __future__ import annotations

from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem, QProgressBar,
)

from commandeck_core.models.config import ConfigManager
from commandeck_core.utils.threading import run_in_thread
from commandeck_core.i18n import _


def show_network_scan_dialog(config: ConfigManager,
                             on_machine_added: Callable | None = None,
                             parent=None) -> None:
    # parent=None: a parentless modal floats as its own window on GNOME/Wayland
    # instead of being glued to the transient parent (same as the machines list).
    dlg = NetworkScanDialog(config, on_machine_added=on_machine_added, parent=None)
    dlg.exec()


class NetworkScanDialog(QDialog):
    def __init__(self, config: ConfigManager,
                 on_machine_added: Callable | None = None, parent=None):
        super().__init__(parent)
        self._config = config
        self._on_machine_added = on_machine_added
        self._scanning = False
        self.setWindowTitle(_("Detect Machines on Network"))
        self.setMinimumSize(460, 420)
        self._build_ui()
        # Auto-start a first scan so the list is populated on open.
        self._start_scan()

    def _build_ui(self):
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(16, 16, 16, 16)
        vbox.setSpacing(10)

        intro = QLabel(_("Commandeck looks for devices on your network that "
                         "accept SSH connections (port 22)."))
        intro.setWordWrap(True)
        vbox.addWidget(intro)

        # Editable subnet — lets a user on a different range (VPN, 192.168.0.x…)
        # correct the prefix before scanning.
        row = QHBoxLayout()
        row.addWidget(QLabel(_("Subnet:")))
        from commandeck_core.pro.services.network_scan import default_subnet
        self._subnet_edit = QLineEdit(default_subnet())
        row.addWidget(self._subnet_edit, 1)
        self._scan_btn = QPushButton(_("Scan"))
        self._scan_btn.clicked.connect(self._start_scan)
        row.addWidget(self._scan_btn)
        vbox.addLayout(row)

        self._progress = QProgressBar()
        self._progress.setRange(0, 0)  # indeterminate
        self._progress.setVisible(False)
        vbox.addWidget(self._progress)

        self._status = QLabel("")
        self._status.setWordWrap(True)
        vbox.addWidget(self._status)

        self._list = QListWidget()
        self._list.setSelectionMode(QListWidget.SingleSelection)
        self._list.itemDoubleClicked.connect(lambda _i: self._add_selected())
        vbox.addWidget(self._list, 1)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self._add_btn = QPushButton(_("Add This Machine"))
        self._add_btn.clicked.connect(self._add_selected)
        self._add_btn.setEnabled(False)
        self._list.itemSelectionChanged.connect(
            lambda: self._add_btn.setEnabled(self._list.currentItem() is not None))
        close_btn = QPushButton(_("Close"))
        close_btn.clicked.connect(self.reject)
        btn_row.addWidget(self._add_btn)
        btn_row.addWidget(close_btn)
        vbox.addLayout(btn_row)

    def _start_scan(self):
        if self._scanning:
            return
        base = self._subnet_edit.text().strip()
        if not base:
            self._status.setText(_("Enter a subnet to scan."))
            return
        self._scanning = True
        self._scan_btn.setEnabled(False)
        self._add_btn.setEnabled(False)
        self._list.clear()
        self._progress.setVisible(True)
        self._status.setText(_("Scanning your network…"))

        from commandeck_core.pro.services.network_scan import (
            scan_subnet, get_local_ipv4)
        own = get_local_ipv4() or ""
        run_in_thread(scan_subnet, self._on_results, base, 22, 0.3, own)

    def _on_results(self, result):
        self._scanning = False
        self._scan_btn.setEnabled(True)
        self._progress.setVisible(False)
        if isinstance(result, Exception):
            self._status.setText(_("Network scan failed: {error}").format(error=result))
            return
        # Hide hosts already configured so only new machines are offered.
        known = {m.host for m in self._config.load_machines()}
        new_hosts = [h for h in result if h["ip"] not in known]
        if not new_hosts:
            self._status.setText(_("No new SSH devices found on your network."))
            return
        self._status.setText(
            _("Found {n} device(s). Pick one to add.").format(n=len(new_hosts)))
        for h in new_hosts:
            label = f"{h['hostname']}  ·  {h['ip']}" if h["hostname"] else h["ip"]
            item = QListWidgetItem(label)
            item.setData(Qt.UserRole, h)
            self._list.addItem(item)

    def _add_selected(self):
        item = self._list.currentItem()
        if not item:
            return
        host = item.data(Qt.UserRole)
        prefill = {
            "host": host["ip"],
            "name": host["hostname"] or host["ip"],
            "port": host.get("port", 22),
        }
        from commandeck_qt.dialogs.machine_dialog import show_machine_dialog
        show_machine_dialog(self._config, on_saved=self._on_saved_machine,
                            parent=None, prefill=prefill)

    def _on_saved_machine(self):
        # Refresh the parent machines list, then drop the just-added host from the
        # results so it isn't offered again.
        if self._on_machine_added:
            self._on_machine_added()
        item = self._list.currentItem()
        if item:
            self._list.takeItem(self._list.row(item))
        if self._list.count() == 0:
            self._status.setText(_("No new SSH devices found on your network."))
