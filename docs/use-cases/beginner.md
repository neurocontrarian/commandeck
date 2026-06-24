# Use Case: Linux Beginner Guide

You just installed Commandeck and you're not sure where to start. This guide is for you. You don't need to know any commands — Commandeck already includes dozens of ready-to-use buttons.

---

## You already have 29 buttons

The first time Commandeck launches, it populates your grid with three categories of pre-built buttons:

- **Hardware** (13 buttons) — disk, memory, CPU, temperature, GPU, and disk-space tools
- **Linux Essentials** (12 buttons) — system info, users, logs, updates, and basic maintenance
- **Network** (4 buttons) — interfaces, connections, ports, and listening services

These buttons are ready to use right now. No setup needed.

Want more? **Development** tools (git, Docker, Python, Node) and other sets are available as free, one-tap [button packs](../packs.md). Open the hamburger menu → **Button Packs** to browse and install them.

---

## What each default button does

### Hardware

| Button | What it shows you |
|--------|-------------------|
| **Disk Usage** | How full each partition is (`df -h`) |
| **Memory Usage** | RAM and swap usage (`free -h`) |
| **CPU Load** | Current load and the busiest processes |
| **Temperature** | CPU/sensor temperatures if `lm-sensors` is installed |
| **Block Devices** | Hard drives, USB drives, partitions (`lsblk`) |
| **Largest Directories** | The biggest folders under `/` |
| **NVIDIA GPU** | NVIDIA GPU status (`nvidia-smi`) |
| **AMD GPU** | AMD GPU detection, activity and temperature |
| **NCDU** | Interactive disk-usage explorer (offers to install `ncdu` if missing) |
| **btop** | Live system monitor (offers to install `btop` if missing) |
| **NVIDIA Settings** | Opens the NVIDIA control panel |
| **Hardware Info** | One-shot hardware report — CPU, memory, devices |
| **Disk I/O** | Disk read/write statistics |

### Linux Essentials

| Button | What it shows you |
|--------|-------------------|
| **Running Processes** | All processes, sorted by CPU usage |
| **System Info** | Kernel version and Linux distribution |
| **Logged-in Users** | Who is currently logged in (`w`) |
| **Last Logins** | Login history |
| **Failed Services** | Services that have crashed or failed to start |
| **System Journal** | Last 50 lines of the system log |
| **Kernel Messages** | Hardware and driver messages |
| **Clear Trash** | Empties your Trash folder |
| **System Update** | Updates your system (works on Ubuntu, Fedora, Arch) |
| **Reboot** | Reboots the computer |
| **Shutdown** | Powers off the computer |
| **Tail Syslog** | Last 50 lines of the system log |

!!! warning
    **Reboot** and **Shutdown** have **Confirm before running** enabled — a dialog will ask you to confirm before anything happens.

### Network

| Button | What it shows you |
|--------|-------------------|
| **Network Interfaces** | Your IP addresses and network cards (`ip addr`) |
| **Active Connections** | Established TCP connections |
| **Open Ports** | Services listening on your machine |
| **Listening Services** | Services listening on TCP ports |

---

## Start by clicking things

Click **Disk Usage**. A small dialog pops up with your filesystem information. Click **Memory Usage**. Try a few more.

You cannot break anything by clicking these buttons — they only read information. The two buttons that actually do something (Reboot and Shutdown) ask for confirmation first.

---

## Declutter: uninstall a pack, or hide a category

The default buttons come as **button packs**. If a whole set isn't useful to you, the cleanest way to declutter is to **uninstall the pack**: open the hamburger menu → **Button Packs**, find it, and click **Uninstall**. Its buttons are removed — and you can reinstall the pack any time with one tap.

If you'd rather just tuck a category out of sight for now (without removing anything), you can hide it instead:

1. Open **Preferences → Categories**
2. Toggle the category off

A hidden category and its buttons disappear from view but aren't deleted — bring them back any time from the same place.

---

## Customise a button name or color

The default button names are functional but generic. You can rename or recolor them to suit your style — this is **free for everyone**, no Pro needed.

Right-click any button → **Edit**:

- Change the **Label** to something friendlier (`Disk Usage` → `How full is my disk?`)
- Pick a **Color** to make important buttons stand out
- Change the **Icon** to one that makes sense to you

---

## Create your first custom button

Custom buttons are **free and unlimited**. Here is an easy one to start:

1. Press `Ctrl+N` (or click **+**)
2. **Label:** `My IP address`
3. **Command:** `hostname -I`
4. **Execution mode:** `Show output`
5. Click **Save**

Now you have a one-click way to see your local IP address.

---

## What if a button shows an error?

Some buttons require software that may not be installed:

- **Temperature** — needs `lm-sensors` (`sudo apt install lm-sensors`)
- **NCDU** and **btop** — offer to install themselves the first time you run them
- If you install the **Development** pack, its Docker/Python/Node buttons need those tools installed

If a command fails, an output dialog opens showing the exact error. Usually it is a missing package — copy the package name and install it.

---

## Getting more out of Commandeck

Once you are comfortable with the defaults:

- [Create custom buttons](../quick-start.md#3-create-your-first-custom-button) for your own frequent commands
- [Organise with categories](../reference/main-window.md#category-filter) to group related buttons
- [Adjust the grid layout](../reference/preferences.md#button-grid-layout) to fit your screen
- Consider [Commandeck Pro](../pro.md) when you want to manage a remote server
