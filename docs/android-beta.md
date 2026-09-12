---
title: Run your home server from your phone
description: Restart a container, check disk space, follow a log — from your phone, over SSH to the machines you already run. No account, no cloud. The Android app is in closed testing and needs 12 testers.
---

# Your home server, from your phone

The commands you run on your home server — restart a container, check disk space, follow a
log, update the stack — become buttons on your phone, over SSH. No agent on the server, no
web panel to host, no account, no cloud.

**It is not on Google Play yet, and that is where you come in.** Commandeck for Android is finished and sitting in Google's closed-testing queue. Google
requires new developer accounts to run a closed test with **12 testers over 14 continuous
days** before an app can be published at all. That is the only thing standing between the
phone app and release.

[Sign up (2 minutes)](https://docs.google.com/forms/d/1N3R9aRd24ZAjmTUU1x7dPLEOmA22zCIXcbT9Nda8wfM/viewform){ .md-button .md-button--primary }

## What you would be testing

Everything the desktop app does over SSH, on a phone screen: your button grid, the free
button packs, machines reached by key or by password, and a live view for the commands that
keep printing while they run. Backups move between the phone and the computer. The one thing
it does not do is run commands on the phone itself — the phone is the remote, not the machine.

## What we ask

- Stay opted in for the **full 14 days**. This is Google's rule, and one person leaving early
  resets the count for everyone.
- Open the app a few times a week — not just on day one.
- Send **at least one message** about what worked or didn't. One line is plenty.

## What you get

Testers keep the app **free for good**. Commandeck for Android is a paid app — a **$19
one-time purchase**, no subscription — and testers who see the two weeks through keep their
free access after launch.

## What you need

- An **Android phone** (not a tablet only, not an emulator).
- A machine you can reach **over SSH**: a NAS, a Raspberry Pi, a VPS, a Proxmox host, a Docker
  box — anything you already run.
- A **Gmail address**, which is what Google's test list works with.

## What happens after you sign up

We read every signup and email the people we select. That message carries your opt-in link, the
install steps, and what we would like you to try first. Nothing to do until then, and the 14
days only start once the group is complete. If you do not hear from us within a week, the group
filled up — we keep your email and tell you when the app goes live.

## What the app talks to

Worth stating plainly, since you would be pointing it at your own servers.

Commandeck opens **two** outbound connections, both only when you ask for them: the button-pack
gallery downloads from GitHub when you open that screen, and licence activation contacts the
payment provider when you enter a key. There is no telemetry, no analytics, no crash reporting,
no account, and no server of ours for anything to be sent to. Your buttons, machines and
credentials stay in the app's own storage on the phone, and SSH goes from your device straight
to your machine.

[Sign up (2 minutes)](https://docs.google.com/forms/d/1N3R9aRd24ZAjmTUU1x7dPLEOmA22zCIXcbT9Nda8wfM/viewform){ .md-button }
