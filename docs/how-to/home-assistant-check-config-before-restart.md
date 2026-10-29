---
title: Check Your Home Assistant Configuration Before You Restart
description: One typo in a YAML file and Home Assistant does not come back after a restart. Here is a restart button that checks the configuration first - and refuses if it is broken.
---

# Check Your Home Assistant Configuration Before You Restart

You copied an automation from a forum into `configuration.yaml`. You restart Home Assistant. It doesn't come back.

This is the most common way to lose Home Assistant for an evening: one wrong indent, one missing quote, and it refuses to start. Home Assistant has its own configuration checker — the trick is to run it *every time*, before every restart, including the day you are in a hurry.

The usual advice is to SSH into the server and run the checker inside the container by hand. Here is the version without any of that.

---

## The one-click check

Commandeck has a **free button pack for Home Assistant**. Install it once and you get two buttons that do the remembering for you.

1. Open Commandeck and add your server as a machine (its address, your user name, your password or SSH key).
2. Menu **☰ → Button Packs → Linux → Home Assistant (Docker)** → *Install*, and pick that machine.
3. After editing a file, click **Is my configuration valid?**

It runs Home Assistant's own checker, shows its report, and ends with a verdict in one line:

- **Valid** — restarting is safe.
- **Problems found** — do not restart until they are fixed; the report above shows what is wrong.
- **It will start, but some parts will be ignored** — restarting is safe, the parts listed stay off until you fix them.

Then, instead of restarting from the Home Assistant page, click **Restart Home Assistant**. It checks the configuration first and **refuses to restart if it is broken**. If it is fine, it restarts Home Assistant and waits until its page answers again.

Nothing to type, no container name to look up: the pack finds Home Assistant by its image, whatever you called it.

---

## It restarted, but something is missing?

The same pack answers the questions that come next.

**An integration did not come back.** Click **What failed to start?** — it lists the integrations that did not load, and points out the custom ones, which are the usual cause after an update.

**The Zigbee or Z-Wave stick is not found.** Click **Is my Zigbee or Z-Wave stick seen?** It checks both ends — does the server see the stick, is it handed to the container — and prints the exact line to add if it is not.

**Something keeps failing.** Click **Recent errors**: everything that went wrong since the last start, each message once instead of the same warning 300 times — ready to paste into a forum post or your AI assistant.

---

## The rest of the pack

The pack is free and has thirteen buttons. The ones people click most:

| Button | Answers |
|---|---|
| **Is Home Assistant running?** | The version it runs, whether Docker had to restart it after crashes |
| **Is there a newer version?** | How many monthly releases you are behind, and which notes to read before jumping |
| **Are the backups happening?** | The newest backup and how old it is |
| **Update Home Assistant** | Refuses to start without a backup from the last 24 hours, then updates and waits until it answers |
| **Database & disk space** | How big the history database has grown, and whether the disk is close to full |

Every command is visible before you install, and you can edit any of them afterwards. The pack is for **Home Assistant Container** — the Docker install. Running Home Assistant OS (the Green, the Yellow, a Raspberry Pi image, a virtual machine)? This pack is not for you: Home Assistant OS has no Docker you can reach.

---

## Running on your server means SSH

Your Home Assistant server is a different machine from the computer you're sitting at, so these buttons reach it over SSH. That part is [Commandeck Pro](../pro.md) — **$29 once, for good, with a 14-day trial that asks for no card and no account**. The pack itself, like every pack, is free.

Nothing leaves your computer: no account, no cloud, no server of ours in the middle. Your machines and passwords stay on your device.

---

**Related:** [Update Your Server Without SSH-ing In](update-server-without-ssh.md) · [Run Docker Commands as One-Click Buttons](docker-commands-one-click-buttons.md) · new here? Start with the [Beginner Guide](../use-cases/beginner.md).
