---
title: Plex Using All Your Processor? Here Is Why
description: Your server gets hot and the film stutters. Plex is converting the video instead of sending it as it is. Find out in one click why, and what to change - no terminal.
---

# Plex Using All Your Processor? Here Is Why

The film stutters. The fan spins up. The server that sat quiet all week is suddenly at 100%.

Almost always, the same thing is happening: **Plex is rebuilding the video, frame by frame, instead of sending the file as it is.** Plex calls it transcoding. It happens when the device you are watching on cannot read the original file — the wrong format, too big a picture, or a subtitle that has to be burned in.

Your server can do that job two ways. The graphics chip does it while barely warming up. The processor does it at 100%, and struggles. Most home servers are on the slow path without their owner ever being told.

---

## Find out in one click

Commandeck has a **free button pack for Plex** — one for Plex in Docker, one for Plex installed on the machine itself. Install it, point it at your server, and two buttons answer the question.

**1. "Why is Plex busy?"** — tells you whether a conversion is running right now, on which file, and what it is costing:

```
=== Converting a video right now? ===
Yes - Plex is converting a video right now.
  File: Sintel
  CPU:  98.0% for that one process
```

**2. "Why is the graphics chip not used?"** — checks, one by one, the four reasons Plex quietly falls back to the processor:

```
=== 1. Is there a graphics chip to use? ===
No /dev/dri/renderD* on this machine.

=== 2. Is Plex allowed to open it? ===
The device belongs to group: render
The plex user is NOT in that group. Fix it with: sudo usermod -aG render plex

=== 3. Is the setting ticked? ===
Plex has never been given the setting.
Settings > Transcoder > Use hardware acceleration when available.

=== 4. What the log says the last time it converted ===
Nothing about hardware in the recent log.
```

It also says the thing no command can check: hardware conversion needs an active **Plex Pass**. Without one, Plex uses the processor and never mentions it.

---

## The four causes, and what to do about each

**The chip is not there, or not shared.** On a mini-PC or a NAS, it is there — nearly every Intel processor of the last ten years has one. If your Plex runs in a Docker container, the container has to be handed the device: add `devices: - /dev/dri:/dev/dri` to your compose file, or tick the equivalent box in your container manager. If Plex runs inside a Proxmox container, the device has to be passed in from the host.

**Plex is not allowed to open it.** The chip belongs to a group, usually `render` or `video`, and the account Plex runs under has to be a member. The button prints the exact command for your machine.

**The setting is off.** Plex does not turn it on by itself: *Settings → Transcoder → Use hardware acceleration when available*.

**No Plex Pass.** Hardware conversion is a paid feature. This one is not a bug and no command can work around it.

---

## Sometimes the answer is: stop converting at all

The fastest conversion is the one that never happens. Two things to try before buying anything:

- **Lower the quality on the device that is watching.** If the player asks for "Original", Plex sends the file untouched and does nothing at all.
- **Look at what is being converted.** If the button says the video is "copied as-is" and only the sound is being changed, your server is barely working — that is the good case, and nothing needs fixing.

And one trap worth knowing: a disk that is nearly full makes everything slow, conversions included. The pack's **Space & conversion cache** button warns you in plain words when one of your drives is running out.

---

## Getting the buttons

Menu **☰ → Button Packs → Linux → Plex (Docker)** or **Plex (system install)** — free, like every pack. Pick the one that matches how Plex is installed on your server; the two use completely different commands.

Reaching your server over SSH is [Commandeck Pro](../pro.md) — **$29 once, for good, 14-day trial with no card and no account**. Nothing leaves your computer: no account, no cloud, no server of ours in between.

---

**Related:** [Plex Not Showing New Movies?](plex-not-showing-new-movies.md) · [Check Disk Space on Your NAS in One Click](check-disk-space-nas.md) · new here? Start with the [Beginner Guide](../use-cases/beginner.md).
