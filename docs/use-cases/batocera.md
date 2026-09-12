---
description: Turn Batocera SSH commands into buttons. Find out why a game will not start, close a frozen emulator, fix a black screen and see what fills the disk - without plugging a keyboard into the box under the TV.
---

# Manage Your Batocera Box Without a Keyboard

A Batocera machine lives under the TV. It has a controller, no keyboard, and no window that
tells you what went wrong. So the day a game refuses to launch, the emulator freezes, or the
screen stays black, the answer you find online is always the same: *"SSH into the box and run
this command."*

That advice works. It is just a poor fit for a machine you use from the couch — you end up
looking for the IP address, opening a terminal on another computer, and re-typing commands you
looked up three months ago.

Commandeck keeps those commands as **buttons**. You set them up once, then answer the question
with one click, from your desk.

!!! tip "Pro feature"
    Talking to another machine over SSH needs [Commandeck Pro](../pro.md) — included in the
    14-day trial, no account required. Batocera itself is free and needs nothing installed on it.

---

## What you need

- A **Batocera box on your network**, powered on, with its **IP address** (Batocera shows it in
  the main menu under *Network Settings*).
- SSH is **already enabled** on Batocera — there is nothing to install or configure on the box.
- Commandeck on your Windows, Mac or Linux computer.

Batocera logs you in as **root**, so nothing here involves `sudo` or an administrator password.

---

## Step 1 — Add the box as a machine

**Menu ☰ → Manage Machines → Add**, then fill in:

| Field | Value |
|-------|-------|
| Name | `Batocera` |
| Host | your box's IP, for example `192.168.1.42` |
| SSH User | `root` |
| Port | `22` |
| Authentication | **Password** |
| SSH Password | `linux` |

`linux` is Batocera's factory password for the `root` user — you already have it, and there is
nothing to set up on the box itself. (If you changed it in Batocera's settings, use yours.)

Click **Test**. It should come back green, and you are done.

!!! note "Where the password is kept"
    Commandeck never writes it into a readable file: it goes into your own computer's keychain —
    Credential Manager on Windows, Keychain on macOS, the system secret service on Linux. It is
    typed once, here, and never again.

---

## Step 2 — Install the Batocera pack

Instead of writing the commands yourself, install the ready-made set.

**Menu ☰ → Button Packs → Linux → Batocera → Install**, and pick the machine you just added.

You get seventeen buttons, already worded as questions rather than commands:

| Button | Answers |
|--------|---------|
| **Batocera system info** | What is this box, and how long has it been up? |
| **Is a game running right now?** | Which game, on which console — by name, not a process number |
| **Debug (es_launch_stderr.log)** | Why the last game did — or did not — start |
| **Debug (es_log.txt)** | What the menu itself is doing: scraping, themes, slow starts |
| **Watch a game launch live** † | The same log, printing as the game starts |
| **Free space** | How full the disk is, and which folders take the room |
| **Which systems eat my disk?** | The size of each console's ROM folder, biggest first |
| **Browse the disk (ncdu)** † | Walk /userdata folder by folder and delete as you go |
| **My controllers** | Which pads are seen, plus battery level on a wireless one |
| **Disconnect the wireless pads** | Switches off every Bluetooth device — stops pads draining overnight |
| **What is my screen doing?** | The resolution being sent, and the modes your TV accepts |
| **Set the display mode** | Forces a resolution — the black-screen rescue |
| **Close the running game** | Kills a frozen emulator and puts you back in the menu |
| **Restart the menu** | Restarts EmulationStation without rebooting |
| **Live monitor (htop)** † | CPU, memory and processes updating while a game runs |
| **Reboot the box** / **Shut down the box** | Cleanly, from your desk |

† Opens a terminal on your computer, so these three are desktop-only.

All packs are free. Only the SSH connection is a Pro feature.

---

## The four moments you will actually use it

### "This game won't start"

You press A, the screen flickers, and you are back in the menu. Batocera wrote down what
happened, but the file is on the box.

Click **Debug (es_launch_stderr.log)**. It pulls the suspicious lines out of the last launch
first — a missing BIOS file, an unsupported ROM format, a permission problem — and tells you
plainly when there is nothing wrong in there. Then click **Copy**: that is exactly what the
Batocera forums ask you to paste when you ask for help.

If the problem is the menu rather than a game — a system that will not appear, a theme that
broke, scraping that stalls — use **Debug (es_log.txt)** instead. That is the second file
support asks for.

EmulationStation only writes that second log once its log level is turned up, so if it is
off the button tells you where to switch it on and lists the logs that do exist instead.

### "It's frozen"

The controller does nothing and the emulator is stuck on screen. **Close the running game**
names the game it is closing, kills it, and checks afterwards that you really are back in the
menu. If that is not enough, **Restart the menu** rebuilds the interface without a full reboot.

### "The screen is black" or "the picture is cut off"

**What is my screen doing?** shows the resolution currently being sent and the list of modes
your TV actually accepts. **Set the display mode** then forces one of them — you type the mode
name, and if you get it wrong the button refuses to change anything and shows you the valid
list instead.

### "The pads are flat again"

A wireless pad left on the rug keeps its radio awake and is empty by the morning.
**Disconnect the wireless pads** drops every Bluetooth connection on the box, and a pad
powers itself off a few seconds later. It is also the polite way to make a pad let go
when a game has frozen with it. Turn one back on with its home button.

---

### "I'm out of space"

**Free space** shows how full the disk is and the biggest folders in plain GB or TB.
**Which systems eat my disk?** breaks it down console by console, so you can see that one
system is taking half the drive before you start deleting anything.

---

## From the sofa, too

The same buttons exist on the phone: Commandeck for Android is
[in closed testing](../android-beta.md) and reads the same packs. It works over your home
network — or through your own VPN, if you have one. Nothing goes through a cloud service,
because there is no cloud service.

---

## Good to know about Batocera

Batocera is not a normal Linux server, and it changes what commands make sense:

- **You are root.** No `sudo`, no admin password anywhere.
- **The system is read-only outside `/userdata`.** Anything you change elsewhere is gone at
  the next reboot.
- **There is no `systemctl` and no `journalctl`.** Logs are plain files; that is why the two
  debug buttons read files instead of asking a service.
- **Full-screen tools** (`htop`, `ncdu`, a live log) need a real terminal to draw themselves in.
  A button gives them one: its mode is **Open in terminal**, and Commandeck opens `ssh -t` to
  the box in a terminal window on your computer. The pack ships three of those —
  *Watch a game launch live*, *Browse the disk (ncdu)*, *Live monitor (htop)*.
- Those three are **desktop-only**: a phone has no terminal to open, so they do not appear in
  the grid on Android. Every other button in the pack works on both.
- Anything that could **wipe a disk** is left out of the pack on purpose.

---

## Related

- [Button Packs](../packs.md) — what a pack is, and how installing one works
- [SSH Machines](../reference/ssh-machines.md) — adding machines, ports and troubleshooting
- [Manage a Homelab Fleet](homelab.md) — the same idea across several machines
- [Quick Start](../quick-start.md) — if this is your first button
