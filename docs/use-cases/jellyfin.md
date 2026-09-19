---
description: Turn the Jellyfin commands you keep looking up into buttons - why it stutters, what fills the disk, the log support asks for, restart and update - on Docker or on a system install.
---

# Keep Jellyfin Healthy Without Learning Docker

Jellyfin is the part of a home server people notice, because it is the part the household
uses. When a film stutters, when a new folder does not appear, or when the disk quietly fills
up, the answer online is always a command — and it is never the same one twice.

Commandeck keeps those commands as **buttons**. Install the pack, point it at your server, and
the questions become one tap each.

!!! tip "Pro feature"
    Talking to your server over SSH needs [Commandeck Pro](../pro.md) — included in the 14-day
    trial, no account required. The packs themselves are free.

---

## First: Docker or a system install?

There are two Jellyfin packs, because there are two ways people run it. Pick the wrong one and
every button answers "not found".

| You installed Jellyfin… | Your pack |
|---|---|
| with **Docker** or **docker compose** (a Portainer stack, a NAS app store) | **Jellyfin (Docker)** |
| from your distribution's **packages** (`apt install jellyfin`, an .deb, a script) | **Jellyfin (systemd)** |

If you are unsure, install the Docker one and press **Is Jellyfin running?**. If it says no
container by that name exists, you have the system install.

---

## Setting up

1. **Menu ☰ → Manage Machines → Add** — name, the server's IP, your SSH user, port 22.
   Choose **Password** or **SSH Key** for authentication, then press **Test**.
2. **Menu ☰ → Button Packs → Linux → Jellyfin (Docker or systemd) → Install**, and pick that
   machine.

That is the whole setup. Nothing is installed on the server.

---

## What the buttons answer

| Button | Answers |
|---|---|
| **Is Jellyfin running?** | Up, stopped, or restarting in a loop |
| **Why is Jellyfin busy?** | What it is doing right now — usually a transcode |
| **Resources right now** | CPU and memory, so you know if the box is the limit |
| **Recent errors** | The error lines only, pulled out of a long log |
| **Full recent log** | The last 60 lines raw, for when the errors are not enough |
| **Follow the log live** † | The log printing as you press play |
| **Who is using the drives?** | Which process is hammering the disk |
| **Space & transcode cache** | How full the disk is, and how much the cache eats |
| **Hardware acceleration** | Whether your GPU is actually being used |
| **Installed plugins** | What is loaded, and what failed to load |
| **Restart Jellyfin** | The fix for half the problems |
| **Update Jellyfin** | Pull and restart, cleanly |
| **Clear the transcode cache** | Reclaims space without touching your media |
| **Shell inside the container** † | Docker only — for answers that start with "run this inside the container" |

† Opens a terminal on your computer, so these two are desktop-only.

---

## The three evenings you will use it

### "It keeps buffering"

Press **Why is Jellyfin busy?**. If it is transcoding, the film is being converted on the fly —
that is what heats the server and empties the buffer. **Hardware acceleration** then tells you
whether the GPU is doing that work or whether the processor is doing it alone, which is the
difference between a smooth film and a stuttering one.

If you want to watch it happen, **Follow the log live** keeps printing while someone presses
play, so you see the transcode start in real time.

### "It won't start" / "the library is empty"

**Is Jellyfin running?** first — a container restarting in a loop looks identical to a server
that is down. Then **Recent errors**, which pulls the error lines out of a log too long to
read. Nine times out of ten, **Restart Jellyfin** is the end of the story.

### "The disk is full"

**Space & transcode cache** shows how full the disk is and how much of it the temporary
transcoding files are holding. **Clear the transcode cache** deletes those files and nothing
else — never your media, never your settings. Do not press it while someone is watching.

---

## From the sofa, too

The same buttons work on the phone: Commandeck for Android is
[in closed testing](../android-beta.md) and reads the same packs, over your home network or
your own VPN.

---

## Related

- [Restart Jellyfin or Plex Without the Terminal](../how-to/restart-jellyfin-plex-without-terminal.md)
  — the one-button version, and the Plex equivalent
- [Button Packs](../packs.md) — what a pack is, and how installing one works
- [Home Server Management](home-server.md) — the same idea across the rest of your server
