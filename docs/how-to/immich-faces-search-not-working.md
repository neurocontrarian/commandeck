---
title: Immich Faces or Search Not Working? Find Out Why in One Click
description: Faces are not grouped, smart search finds nothing. Here is how to check the three usual reasons from a button on your desktop - without opening a terminal on your server.
---

# Immich Faces or Search Not Working? Find Out Why in One Click

You uploaded a few hundred photos. Days later, the faces are still not grouped, and searching for "beach" finds nothing.

Nothing is lost. Your photos are safe — what stopped is the part of Immich that *looks at* them. Immich is four programs working together, and faces and smart search come from one of them: the machine-learning part. When it stops, or the app cannot reach it, Immich keeps working… it just stops recognising anything.

The usual advice is to SSH into the server, list the containers and read their logs. Here is the version without any of that.

---

## The one-click check

Commandeck has a **free button pack for Immich**. Install it once and you get a button that checks the three usual reasons, one after the other, and tells you which one it is.

1. Open Commandeck and add your server as a machine (its address, your user name, your password or SSH key).
2. Menu **☰ → Button Packs → Linux → Immich (Docker)** → *Install*, and pick that machine.
3. Click **Why are faces or search not working?**

It checks, in plain words:

- **Is the faces-and-search part running?** If it is stopped, that is the reason, and it says so.
- **Can the app reach it?** Both can be running and still not talk to each other. If they don't, it tells you where to set the right address in Immich's settings.
- **What did it report in the last 24 hours?** Its recent errors and warnings — including the ones that mean it ran out of memory.

Nothing to type, no container name to look up: the pack finds Immich's containers by their image, whatever you called them.

---

## Faces are fine, but something else is wrong?

The same pack answers the other questions people SSH in for.

**The disk is filling up.** Immich keeps more than your photos: previews, converted copies of your videos, database backups. Click **Where did the disk space go?** — it measures each one, says what it is, and warns you when a disk is nearly full.

**Are my backups really happening?** Immich can copy its database every night — if the setting is on and nothing broke. Click **Are the backups happening?**: it finds the newest copy and tells you how old it is, instead of letting you assume.

**Should I update?** Click **Is there a newer version?** — it compares your version with the newest one and warns you when the jump is a big one, the kind where the phone app must follow. **Update Immich** refuses to start without a database copy from the last 24 hours, because an update cannot be undone.

---

## The rest of the pack

The pack is free and has thirteen buttons. The ones people click most:

| Button | Answers |
|---|---|
| **Is Immich running?** | Each of its four parts, what it is for, and why one stopped |
| **Recent errors** | What went wrong in the last 24 hours, each message once — ready to paste into a forum post or your AI assistant |
| **Restart Immich** | The first move when it is stuck: restarts every part and waits until the app is ready |
| **Resources right now** | Why the server is busy — usually face recognition after a big upload |
| **List the users** | Every account, with its e-mail and whether it is an administrator |

Every command is visible before you install, and you can edit any of them afterwards. The pack is for **Immich running with Docker** (compose or Portainer). Installed it as an Unraid template, a TrueNAS app or a snap? Some buttons will not find it.

---

## Running on your server means SSH

Your Immich server is a different machine from the computer you're sitting at, so these buttons reach it over SSH. That part is [Commandeck Pro](../pro.md) — **$29 once, for good, with a 14-day trial that asks for no card and no account**. The pack itself, like every pack, is free.

Nothing leaves your computer: no account, no cloud, no server of ours in the middle. Your machines and passwords stay on your device.

---

**Related:** [Check Disk Space on Your NAS in One Click](check-disk-space-nas.md) · [Update Your Server Without SSH-ing In](update-server-without-ssh.md) · new here? Start with the [Beginner Guide](../use-cases/beginner.md).
