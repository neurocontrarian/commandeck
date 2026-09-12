---
title: Plex Not Showing New Movies? Make It Look Again
description: You copied a film into the folder and Plex ignores it. Here is how to make Plex look through your libraries again - from a button on your desktop, without opening a terminal.
---

# Plex Not Showing New Movies? Make It Look Again

You copied a film into your movies folder. You open Plex. It isn't there.

Nothing is broken. Plex only knows about the files it has *looked at*, and it doesn't watch your folders every second — especially when the folder lives on a NAS, a network share, or inside Docker, where the signal that says "a new file arrived" often never reaches it.

The fix is to tell Plex to look again. On a server, the usual advice is to SSH in and run a command with a library number you have to find first. Here is the version without any of that.

---

## The one-click fix

Commandeck ships a **free button pack for Plex**. Install it once and you get a button that tells Plex to go through every library again — your films, your series, your music — and names each one as it goes.

1. Open Commandeck and add your server as a machine (its address, your user name, your password or SSH key).
2. Menu **☰ → Button Packs → Linux → Plex (Docker)** → *Install*, and pick that machine. (Plex installed straight on the machine rather than in a container? Take **Plex (system install)** instead - same buttons, different commands underneath.)
3. Click **Look for new films and episodes**.

```
Films... looked through.
Series... looked through.
Music... looked through.

Plex reads the new files in the background; they appear as it goes.
```

Nothing to type, no library number to look up. The new film shows up in Plex a few seconds later — a big library takes a few minutes.

---

## If it still doesn't appear

Three reasons account for almost every case, and the same pack answers all three.

**The disk is full.** Plex needs room to write what it learns about a file. When the drive is at 100%, a scan can finish without adding anything — and in the worst case it damages Plex's catalogue. Click **Space & conversion cache**: it reads every folder Plex can see and warns you in plain words if one is nearly full.

**Plex cannot read the file.** A film copied from another machine often keeps that machine's permissions. Click **What Plex reported** — if Plex could not open something, it says so there, once, instead of buried in thousands of lines of its own housekeeping.

**The catalogue itself is damaged.** Rare, but it explains a Plex that forgets films or loses watched marks. Click **Is the database healthy?** — it checks a *copy* of Plex's database, so it changes nothing, and tells you what it found.

---

## The rest of the pack

The pack is free and has fifteen buttons. The ones people click most:

| Button | Answers |
|---|---|
| **Is Plex running?** | Is it up, and if it stopped, why |
| **Why is Plex busy?** | Converting a video, scanning a library, or neither |
| **What Plex reported** | Every message Plex wrote, each one once, with how many times it repeated |
| **Why is the graphics chip not used?** | The four reasons Plex converts video the slow way |
| **Restart Plex** | The first move when something is stuck |
| **Clear the conversion cache** | Deletes temporary converted video only — never your films |

Every command is visible before you install, and you can edit any of them afterwards.

---

## Running on your server means SSH

Your Plex server is a different machine from the computer you're sitting at, so these buttons reach it over SSH. That part is [Commandeck Pro](../pro.md) — **$29 once, for good, with a 14-day trial that asks for no card and no account**. The pack itself, like every pack, is free.

Nothing leaves your computer: no account, no cloud, no server of ours in the middle. Your machines and passwords stay on your device.

---

**Related:** [Restart Jellyfin or Plex Without the Terminal](restart-jellyfin-plex-without-terminal.md) · [Check Disk Space on Your NAS in One Click](check-disk-space-nas.md) · new here? Start with the [Beginner Guide](../use-cases/beginner.md).
