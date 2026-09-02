# Installation

Commandeck runs on **Linux, macOS, and Windows**. Every release lists the files for all
three platforms together:
**[GitHub Releases](https://github.com/neurocontrarian/commandeck/releases/latest)** —
that link always points to the newest version, so bookmark it.

All **Pro** builds include a **14-day free trial** — no account, no card. The trial
starts automatically on first launch.

---

## Linux (AppImage)

One file, no installation. Download it, make it executable, and run it. The AppImage is
**self-contained** — it bundles Python, Qt, and every dependency, so there is nothing to
install on the host.

| File | When to use |
|------|-------------|
| `Commandeck-Linux-x86_64.AppImage` | **Free — Intel/AMD.** |
| `Commandeck-Linux-ARM64.AppImage` | **Free — ARM64** (Raspberry Pi 4+, ARM server, Apple Silicon VM). |
| `Commandeck-Pro-Linux-x86_64.AppImage` | **Pro — Intel/AMD.** 14-day trial included. |
| `Commandeck-Pro-Linux-ARM64.AppImage` | **Pro — ARM64.** 14-day trial included. |

Not sure which CPU you have? Run `uname -m` — `x86_64` for Intel/AMD, `aarch64` for ARM.

```bash
chmod +x Commandeck-*.AppImage
./Commandeck-*.AppImage
```

If your distro reports a missing Qt platform plugin on launch, install `libxcb-cursor0`:

=== "Debian / Ubuntu / Linux Mint"

    ```bash
    sudo apt install libxcb-cursor0
    ```

=== "Fedora"

    ```bash
    sudo dnf install xcb-util-cursor
    ```

=== "Arch Linux"

    ```bash
    sudo pacman -S xcb-util-cursor
    ```

---

## macOS (Apple Silicon)

| File | When to use |
|------|-------------|
| `Commandeck-macOS-AppleSilicon.dmg` | **Free.** |
| `Commandeck-Pro-macOS-AppleSilicon.dmg` | **Pro.** 14-day trial included. |

Open the `.dmg` and drag **Commandeck** into Applications.

> **Intel Macs are not supported yet** — the build is for Apple Silicon (M1 or later).

The app is **not yet code-signed**, so on first launch macOS Gatekeeper will block it.
Right-click the app → **Open** (then confirm), or run:

```bash
xattr -dr com.apple.quarantine /Applications/Commandeck.app
```

---

## Windows (x86_64)

| File | When to use |
|------|-------------|
| `Commandeck-Windows-x64.exe` | **Free** — installer (Start-menu shortcut + uninstaller). |
| `Commandeck-Pro-Windows-x64.exe` | **Pro** installer. 14-day trial included. |

Run the installer. It is **not yet code-signed**, so SmartScreen may warn you: click
**More info → Run anyway**.

---

## Updating

To update, download the latest installer from [commandeck.app](https://commandeck.app)
(or the [releases page](https://github.com/neurocontrarian/commandeck/releases/latest)) and
install it over your current version — your buttons and settings are kept.
