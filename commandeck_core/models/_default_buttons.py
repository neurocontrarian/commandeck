"""Default buttons seeded on first run — published as one pack PER CATEGORY GROUP.

`get_default_buttons()` seeds the host-OS set at first run. Each button is stamped as
belonging to the pack for **its own grid category** (`source_pack` = e.g.
`linux-hardware` / `linux-network` / `linux-essentials`), with a stable
`pack_button_id` and `pack_base_command` = the command as shipped, and kept
`is_default=True` (so the free-tier visibility + mobile-rendering logic that keys off
defaults still works). One pack ↔ one grid group keeps the gallery and the grid in
1:1 step (no single "essentials" pack spanning Hardware/Network/etc.). Because the
defaults are tracked packs, a later fix to a default command reaches existing installs
through the ordinary pack-update path (`pack_service.apply_pack_update`), not a Reset.

The same builders (`_linux_essentials`/`_windows_essentials`) are the single content
source: `dev/packs/gen_essentials.py` generates the matching published `pack.toml`
(one per group) from them, so the bundled seed and the gallery's update copy never drift.
"""

import re
import sys

from .command_button import CommandButton

# Bumped whenever a default command/button changes; the generated pack.toml files carry
# the same string, so the published gallery versions stay in lock-step. This is what
# `record_installed_pack` stores at first run and what an "update available" check
# compares against the repo index.
DEFAULTS_VERSION = "1.0.0"

# A button's grid category → its pack-id suffix. The pack id is "{os_tag}-{suffix}"
# and the pack's display name is the category itself, so each grid group maps 1:1 to
# a pack of the same name.
_CATEGORY_PACK_SUFFIX = {
    "Hardware": "hardware",
    "Network": "network",
    "Linux Essentials": "essentials",
    "Windows Essentials": "essentials",
}


def _os_tag(target_os: str | None = None) -> str:
    plat = (target_os or sys.platform).lower()
    if plat.startswith("win"):
        return "windows"
    if plat.startswith(("darwin", "mac")):
        return "macos"
    return "linux"


def category_pack_id(os_tag: str, category: str) -> str:
    """Pack id for a default button's category, e.g. ``("linux","Hardware")`` →
    ``"linux-hardware"``. Unknown categories fall back to a slug."""
    suffix = _CATEGORY_PACK_SUFFIX.get(category)
    if suffix is None:
        suffix = re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-") or "misc"
    return f"{os_tag}-{suffix}"


def default_pack_ids(target_os: str | None = None) -> list[str]:
    """The default pack ids seeded for an OS, in grid order (deduplicated)."""
    return list(dict.fromkeys(b.source_pack for b in get_default_buttons(target_os)))


def get_default_buttons(target_os: str | None = None) -> list[CommandButton]:
    """Seed buttons for an OS. ``target_os`` (``"linux"``/``"macos"``/``"darwin"``/
    ``"windows"``) overrides the host platform — used by mobile, where the phone is
    Android but the SSH target OS is chosen by the user. macOS uses the Linux
    (POSIX) set; only Windows differs. Default = the host's own ``sys.platform``."""
    plat = (target_os or sys.platform).lower()
    if plat.startswith("win"):
        buttons = _windows_essentials()
    else:  # linux, macos/darwin → POSIX set
        buttons = _linux_essentials()
    os_tag = _os_tag(target_os)
    for i, btn in enumerate(buttons):
        btn.position = i
        btn.is_default = True
        btn.os = os_tag  # provenance: which OS this command set is written for
        # Each default belongs to the pack for its own grid category.
        btn.source_pack = category_pack_id(os_tag, btn.category)
        btn.pack_base_command = btn.command  # baseline for "user edited?" on update
    return buttons


def _install_or_run(binary: str, run: str, pkg: str = "") -> str:
    """Shell snippet for a *terminal-mode* button: run ``run`` if ``binary`` is
    present, otherwise detect the package manager and offer to install ``pkg``
    (defaults to ``binary``), then run it on success.

    Interactive (a y/N prompt + sudo password), so this only works on buttons
    with ``execution_mode="terminal"`` — never on a plain show-output button.
    Covers apt/dnf/pacman/zypper/apk so it behaves sensibly across distros.
    """
    pkg = pkg or binary
    return (
        f'if command -v {binary} >/dev/null; then {run}; else '
        f'echo "{binary} is not installed."; '
        f'if command -v apt-get >/dev/null; then PM="sudo apt-get install -y {pkg}"; '
        f'elif command -v dnf >/dev/null; then PM="sudo dnf install -y {pkg}"; '
        f'elif command -v pacman >/dev/null; then PM="sudo pacman -S --noconfirm {pkg}"; '
        f'elif command -v zypper >/dev/null; then PM="sudo zypper install -y {pkg}"; '
        f'elif command -v apk >/dev/null; then PM="sudo apk add {pkg}"; '
        'else PM=""; fi; '
        'if [ -n "$PM" ]; then '
        f'read -rp "Install {pkg} now? [y/N] " a; '
        f'case "$a" in [yY]*) eval "$PM" && {run};; *) echo "Skipped.";; esac; '
        f'else echo "Please install {pkg} with your package manager."; fi; fi'
    )


# Stable per-button ids for the essentials packs — the pack-update matching keys.
# NEVER reorder, rename or remove an entry (it would orphan an installed button on
# the next update); only append. They must line up 1:1 with the builder lists below.
_LINUX_ESSENTIAL_IDS = [
    "disk-usage", "memory-usage", "cpu-load", "temperature", "running-processes",
    "network-interfaces", "active-connections", "open-ports", "block-devices",
    "largest-directories", "nvidia-gpu", "amd-gpu", "ncdu", "btop", "nvidia-settings",
    "hardware-info", "system-info", "logged-in-users", "last-logins", "failed-services",
    "system-journal", "kernel-messages", "clear-trash", "system-update", "reboot",
    "shutdown", "disk-io", "tail-syslog", "listening-services",
]

_WINDOWS_ESSENTIAL_IDS = [
    "disk-usage", "memory-usage", "cpu-load", "network-interfaces", "open-ports",
    "active-connections", "ping", "system-info", "running-services", "system-events",
    "restart-explorer", "empty-recycle-bin", "reboot", "shutdown",
]


def _assign_pack_ids(buttons: list[CommandButton], ids: list[str]) -> list[CommandButton]:
    """Stamp the stable per-pack button ids onto the freshly-built buttons."""
    if len(buttons) != len(ids):
        raise AssertionError(
            f"essentials id list out of sync: {len(buttons)} buttons, {len(ids)} ids")
    for b, sid in zip(buttons, ids):
        b.pack_button_id = sid
    return buttons


def _linux_essentials() -> list[CommandButton]:
    return _assign_pack_ids([
        CommandButton(
            name="Disk Usage",
            command="df -h",
            icon_name="hdd",
            color="#99c1f1",
            show_output=True,
            tooltip="Show disk space usage for all mounted filesystems",
            category="Hardware",
        ),
        CommandButton(
            name="Memory Usage",
            command="free -h",
            icon_name="memory",
            color="#8ff0a4",
            show_output=True,
            tooltip="Show total, used and free RAM and swap memory",
            category="Hardware",
        ),
        CommandButton(
            name="CPU Load",
            command="uptime && echo && top -bn1 | head -15",
            icon_name="cpu",
            color="#ffbe6f",
            show_output=True,
            tooltip="Show system uptime, load averages and top CPU processes",
            category="Hardware",
        ),
        CommandButton(
            name="Temperature",
            command="sensors 2>/dev/null || echo 'lm-sensors is not installed.\nTo install: sudo apt install lm-sensors && sudo sensors-detect'",
            icon_name="thermometer-half",
            color="#ff7800",
            show_output=True,
            tooltip="Show CPU and GPU temperatures (requires lm-sensors)",
            category="Hardware",
        ),
        CommandButton(
            name="Running Processes",
            command="ps aux --sort=-%cpu | head -20",
            icon_name="activity",
            color="#dc8add",
            show_output=True,
            tooltip="List top 20 processes sorted by CPU usage",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Network Interfaces",
            command="ip addr",
            icon_name="ethernet",
            color="#62a0ea",
            show_output=True,
            tooltip="Show all network interfaces and their IP addresses",
            category="Network",
        ),
        CommandButton(
            name="Active Connections",
            command="ss -tp state established",
            icon_name="plug",
            color="#57e389",
            show_output=True,
            tooltip="Show all active TCP connections and the processes using them",
            category="Network",
        ),
        CommandButton(
            name="Open Ports",
            command="ss -tulpn",
            icon_name="broadcast",
            color="#57e389",
            show_output=True,
            tooltip="List all open TCP/UDP ports and the processes using them",
            category="Network",
        ),
        CommandButton(
            name="Block Devices",
            command="lsblk",
            icon_name="stack",
            color="#cdab8f",
            show_output=True,
            tooltip="List all block devices (disks, partitions, loop devices)",
            category="Hardware",
        ),
        CommandButton(
            name="Largest Directories",
            # -x stays on the root filesystem: skips /proc, /sys and mounted
            # filesystems (snap squashfs, network mounts) that otherwise make
            # this hang and balloon the numbers.
            command="du -shx /* 2>/dev/null | sort -rh | head -15",
            icon_name="folder2",
            color="#e5a50a",
            show_output=True,
            timeout=120,
            tooltip="Show the 15 largest top-level directories by disk usage",
            category="Hardware",
        ),
        CommandButton(
            name="NVIDIA GPU",
            command="nvidia-smi 2>/dev/null || echo 'nvidia-smi not found. Install the NVIDIA proprietary driver.'",
            icon_name="pc-display",
            color="#76b900",
            show_output=True,
            tooltip="Show NVIDIA GPU activity, memory and processes (requires nvidia-smi)",
            category="Hardware",
        ),
        CommandButton(
            name="AMD GPU",
            command=(
                'echo "=== AMD GPU ==="; '
                'lspci 2>/dev/null | grep -iE "vga|3d|display" | grep -iE "amd|radeon" '
                '|| echo "(no AMD GPU detected via lspci)"; '
                'echo; echo "=== Activity ==="; '
                'found=0; for f in /sys/class/drm/card*/device/gpu_busy_percent; do '
                '[ -f "$f" ] && echo "$(echo $f | awk -F/ \'{print $5}\'): $(cat $f)%" && found=1; '
                'done; [ "$found" = "0" ] && echo "(activity counters not exposed by driver)"; '
                'echo; echo "=== Temperature & power ==="; '
                'sensors 2>/dev/null | awk \'/amdgpu/{p=1} p; /^$/{p=0}\' '
                '|| echo "(install lm-sensors for temperature: sudo apt install lm-sensors)"'
            ),
            icon_name="pc-display-horizontal",
            color="#ed1c24",
            show_output=True,
            tooltip="Show AMD GPU model, activity (sysfs) and temperature (sensors) — no extra packages required",
            category="Hardware",
        ),
        CommandButton(
            name="NCDU",
            command=_install_or_run("ncdu", "ncdu /"),
            icon_name="hdd",
            color="#3584e4",
            execution_mode="terminal",
            tooltip="Interactive disk usage analyzer (requires ncdu)",
            category="Hardware",
        ),
        CommandButton(
            name="btop",
            command=_install_or_run("btop", "btop"),
            icon_name="activity",
            color="#5e5c64",
            execution_mode="terminal",
            tooltip="Interactive resource monitor (requires btop)",
            category="Hardware",
        ),
        CommandButton(
            name="NVIDIA Settings",
            command="(nvidia-settings >/dev/null 2>&1 & disown) && echo 'nvidia-settings launched.' || echo 'nvidia-settings not found. Install: sudo apt install nvidia-settings'",
            icon_name="pc-display",
            color="#76b900",
            show_output=True,
            tooltip="Open the NVIDIA control panel to tune power limit, fan curves, clocks, etc.",
            category="Hardware",
        ),
        CommandButton(
            name="Hardware Info",
            command=(
                'if command -v inxi >/dev/null 2>&1; then '
                '  inxi -Fxz; '
                'else '
                '  echo "Tip: install inxi for a one-shot report — sudo apt install inxi"; echo; '
                '  echo "=== CPU ==="; lscpu | head -20; echo; '
                '  echo "=== Memory ==="; free -h; echo; '
                '  echo "=== Block devices ==="; lsblk; echo; '
                '  echo "=== PCI devices ==="; lspci | grep -iE "vga|3d|audio|network|ethernet"; echo; '
                '  echo "=== Motherboard / BIOS ==="; '
                '  (sudo -n dmidecode -t baseboard -t bios 2>/dev/null '
                '   || cat /sys/devices/virtual/dmi/id/board_{vendor,name,version} 2>/dev/null); '
                'fi'
            ),
            icon_name="cpu",
            color="#3584e4",
            show_output=True,
            timeout=60,
            tooltip="Show CPU, memory, motherboard, GPU, network and storage in one report (uses inxi if installed)",
            category="Hardware",
        ),
        CommandButton(
            name="System Info",
            command="uname -a && echo && lsb_release -a 2>/dev/null || cat /etc/os-release",
            icon_name="info-circle",
            color="#f9f06b",
            show_output=True,
            tooltip="Show kernel version and Linux distribution information",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Logged-in Users",
            command="w",
            icon_name="people",
            color="#c061cb",
            show_output=True,
            tooltip="Show who is logged in and what they are doing",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Last Logins",
            # `last` (wtmp) is no longer installed by default on systemd distros
            # like recent Ubuntu/Fedora. Fall back to the journal's logind session
            # events (readable without root for adm/systemd-journal users).
            command=("last -n 20 2>/dev/null "
                     "|| journalctl --no-pager -n 50 _COMM=systemd-logind 2>/dev/null "
                     "|| echo 'No login history available "
                     "(install the util-linux-extra or wtmpdb package for last).'"),
            icon_name="person-check",
            color="#9141ac",
            show_output=True,
            tooltip="Show recent login/session activity (last, or the systemd journal)",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Failed Services",
            command="systemctl --failed",
            icon_name="exclamation-triangle",
            color="#f66151",
            show_output=True,
            tooltip="List all systemd services that have failed — useful for diagnosing broken features",
            category="Linux Essentials",
        ),
        CommandButton(
            name="System Journal",
            command="journalctl -n 50 --no-pager",
            icon_name="journal-text",
            color="#ffa348",
            show_output=True,
            tooltip="Show the last 50 lines of the system journal (all services, cross-distro)",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Kernel Messages",
            # `dmesg` needs root on modern kernels (kernel.dmesg_restrict=1).
            # `journalctl -k` reads the same kernel log without root for users in
            # the adm/systemd-journal group (the desktop default); fall back to
            # dmesg, then to a helpful hint if both are denied.
            command=("journalctl -k -n 30 --no-pager 2>/dev/null "
                     "|| dmesg 2>/dev/null | tail -30 "
                     "|| echo 'Kernel log needs elevated privileges "
                     "(try sudo, or add your user to the systemd-journal group).'"),
            icon_name="cpu",
            color="#ffa348",
            show_output=True,
            tooltip="Show the last 30 kernel ring buffer messages (hardware, boot events)",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Clear Trash",
            command="rm -rf ~/.local/share/Trash/files/* ~/.local/share/Trash/info/* 2>/dev/null && echo 'Trash cleared.'",
            icon_name="trash",
            color="#865e3c",
            confirm_before_run=True,
            tooltip="Permanently delete all files in the Trash",
            category="Linux Essentials",
        ),
        CommandButton(
            name="System Update",
            command="bash -c 'if command -v apt >/dev/null 2>&1; then sudo apt update && sudo apt upgrade -y; elif command -v dnf >/dev/null 2>&1; then sudo dnf upgrade -y; elif command -v pacman >/dev/null 2>&1; then sudo pacman -Syu --noconfirm; else echo \"Unknown package manager\"; fi'",
            icon_name="cloud-download",
            color="#62a0ea",
            show_output=True,
            confirm_before_run=True,
            tooltip="Refresh package lists and upgrade all installed packages (apt / dnf / pacman)",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Reboot",
            command="systemctl reboot",
            icon_name="arrow-clockwise",
            color="#f8e45c",
            confirm_before_run=True,
            tooltip="Reboot the system immediately",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Shutdown",
            command="systemctl poweroff",
            icon_name="power",
            color="#f66151",
            confirm_before_run=True,
            tooltip="Power off the system immediately",
            category="Linux Essentials",
        ),
        # Relocated from the former "Development" set (2026-06-15 slim): these are
        # system/maintenance buttons, so they stay in the bundled OS defaults while
        # the dev-tooling and Docker buttons move out to downloadable packs.
        CommandButton(
            name="Disk I/O",
            command="iostat -x 1 3 2>/dev/null || vmstat -d 1 3 2>/dev/null || cat /proc/diskstats",
            icon_name="hdd",
            color="#cdab8f",
            show_output=True,
            tooltip="Show disk I/O statistics — uses iostat, vmstat or /proc/diskstats (whichever is available)",
            category="Hardware",
        ),
        CommandButton(
            name="Tail Syslog",
            command="tail -n 50 /var/log/syslog 2>/dev/null || journalctl -n 50 --no-pager",
            icon_name="file-text",
            color="#ffa348",
            show_output=True,
            tooltip="Show the last 50 lines of the system log (syslog or journald)",
            category="Linux Essentials",
        ),
        CommandButton(
            name="Listening Services",
            command="ss -tlnp",
            icon_name="broadcast",
            color="#57e389",
            show_output=True,
            tooltip="List all services listening on TCP ports",
            category="Network",
        ),
    ], _LINUX_ESSENTIAL_IDS)


# --- Windows (Phase 27) ---------------------------------------------------
# Local commands run via `powershell -NoProfile -Command` (see
# services/executor.py::_run_local_windows), so these use PowerShell cmdlets.
# Constraints: statement separator is ';' (Windows PowerShell 5.1 has no '&&'),
# string literals use single quotes only (no double quotes — the whole command
# is passed as one argv element through list2cmdline), and execution_mode stays
# "" (output) because the terminal launcher is Linux-only.

def _windows_essentials() -> list[CommandButton]:
    return _assign_pack_ids([
        CommandButton(
            name="Disk Usage",
            command="Get-PSDrive -PSProvider FileSystem",
            icon_name="hdd",
            color="#99c1f1",
            show_output=True,
            tooltip="Show disk space usage for all mounted filesystems",
            category="Hardware",
        ),
        CommandButton(
            name="Memory Usage",
            command=(
                "Get-CimInstance Win32_OperatingSystem | Select-Object "
                "@{N='TotalRAM(GB)';E={[math]::Round($_.TotalVisibleMemorySize/1MB,2)}}, "
                "@{N='FreeRAM(GB)';E={[math]::Round($_.FreePhysicalMemory/1MB,2)}} | Format-List"
            ),
            icon_name="memory",
            color="#8ff0a4",
            show_output=True,
            tooltip="Show total, used and free RAM and swap memory",
            category="Hardware",
        ),
        CommandButton(
            name="CPU Load",
            command=(
                "Get-Process | Sort-Object CPU -Descending | Select-Object -First 15 "
                "Name, Id, CPU, @{N='Mem(MB)';E={[math]::Round($_.WS/1MB,1)}} | Format-Table -AutoSize"
            ),
            icon_name="cpu",
            color="#ffbe6f",
            show_output=True,
            tooltip="List the 15 processes using the most CPU",
            category="Hardware",
        ),
        CommandButton(
            name="Network Interfaces",
            command=(
                "Get-NetIPAddress | Where-Object AddressState -eq 'Preferred' | "
                "Sort-Object InterfaceAlias | Format-Table InterfaceAlias, IPAddress, "
                "AddressFamily, PrefixLength -AutoSize"
            ),
            icon_name="ethernet",
            color="#62a0ea",
            show_output=True,
            tooltip="Show all network interfaces and their IP addresses",
            category="Network",
        ),
        CommandButton(
            name="Open Ports",
            command=(
                "Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Select-Object "
                "LocalAddress, LocalPort, OwningProcess, "
                "@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name}} | "
                "Format-Table -AutoSize"
            ),
            icon_name="broadcast",
            color="#57e389",
            show_output=True,
            tooltip="List all open TCP/UDP ports and the processes using them",
            category="Network",
        ),
        CommandButton(
            name="Active Connections",
            command=(
                "Get-NetTCPConnection -State Established | Select-Object LocalAddress, LocalPort, "
                "RemoteAddress, RemotePort, "
                "@{N='Process';E={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).Name}} | "
                "Format-Table -AutoSize"
            ),
            icon_name="plug",
            color="#57e389",
            show_output=True,
            tooltip="Show all active TCP connections and the processes using them",
            category="Network",
        ),
        CommandButton(
            name="Ping",
            command="ping 8.8.8.8",
            icon_name="wifi",
            color="#62a0ea",
            show_output=True,
            tooltip="Send 4 test packets to a public server to check internet connectivity",
            category="Network",
        ),
        CommandButton(
            name="System Info",
            command=(
                "Get-ComputerInfo | Select-Object CsName, WindowsProductName, WindowsVersion, "
                "OsArchitecture, CsManufacturer, CsModel, "
                "@{N='RAM(GB)';E={[math]::Round($_.CsTotalPhysicalMemory/1GB,1)}} | Format-List"
            ),
            icon_name="info-circle",
            color="#f9f06b",
            show_output=True,
            timeout=60,
            tooltip="Show Windows edition, version, hardware model and total memory",
            category="Windows Essentials",
        ),
        CommandButton(
            name="Running Services",
            command=(
                "Get-Service | Where-Object Status -eq 'Running' | Sort-Object DisplayName | "
                "Format-Table Status, Name, DisplayName -AutoSize"
            ),
            icon_name="server",
            color="#dc8add",
            show_output=True,
            tooltip="List all Windows services that are currently running",
            category="Windows Essentials",
        ),
        CommandButton(
            name="System Events",
            command=(
                "Get-EventLog -LogName System -Newest 20 -EntryType Error, Warning | "
                "Format-Table TimeGenerated, EntryType, Source, EventID -AutoSize"
            ),
            icon_name="journal-text",
            color="#ffa348",
            show_output=True,
            tooltip="Show the 20 most recent System event-log errors and warnings",
            category="Windows Essentials",
        ),
        CommandButton(
            name="Restart Explorer",
            command=(
                "Stop-Process -Name explorer -Force; Start-Sleep -Seconds 2; "
                "if (-not (Get-Process -Name explorer -ErrorAction SilentlyContinue)) { Start-Process explorer }; "
                "Write-Output 'Explorer restarted.'"
            ),
            icon_name="arrow-clockwise",
            color="#f8e45c",
            confirm_before_run=True,
            show_output=True,
            tooltip="Restart Windows Explorer (taskbar and desktop) to clear display glitches",
            category="Windows Essentials",
        ),
        CommandButton(
            name="Empty Recycle Bin",
            command="Clear-RecycleBin -Force -ErrorAction SilentlyContinue; Write-Output 'Recycle Bin emptied.'",
            icon_name="trash",
            color="#865e3c",
            confirm_before_run=True,
            show_output=True,
            tooltip="Permanently delete all files in the Recycle Bin",
            category="Windows Essentials",
        ),
        CommandButton(
            name="Reboot",
            command="Restart-Computer -Force",
            icon_name="arrow-clockwise",
            color="#f8e45c",
            confirm_before_run=True,
            show_output=True,
            tooltip="Reboot the system immediately",
            category="Windows Essentials",
        ),
        CommandButton(
            name="Shutdown",
            command="Stop-Computer -Force",
            icon_name="power",
            color="#f66151",
            confirm_before_run=True,
            show_output=True,
            tooltip="Power off the system immediately",
            category="Windows Essentials",
        ),
    ], _WINDOWS_ESSENTIAL_IDS)
