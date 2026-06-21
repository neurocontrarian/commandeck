---
description: Frequently asked questions about Commandeck — pricing, privacy, AI safety, platform support, and how it compares to aliases, scripts and web panels.
---

# Frequently Asked Questions

## Is Commandeck free?

The free edition is **free to use**: unlimited local commands and buttons,
no account, no expiry. **Pro** is a **$29 one-time purchase** (no subscription — buy once,
yours for good) that adds SSH machines, multi-machine buttons, themes, backup/restore,
editable default buttons and the MCP server. Every Pro build includes an automatic
**14-day trial** — no card, no email. See [Pro & pricing](pro.md).

## Why not just shell aliases or a script?

If you live in the terminal and your aliases work, you may not need Commandeck. It shines
in two cases: the commands you *don't* run often enough to remember (the once-a-month
maintenance stuff, or that command an AI gave you three weeks ago), and people who want a
button, not a prompt. Buttons are visible and organized, output opens in a window, SSH
targets are picked at click time, and risky commands get an "are you sure?" dialog —
that's the part `history | grep` doesn't do.

## How is this different from a self-hosted web panel?

Some tools solve a similar problem as a **web service you install on a server** (a
container to run, a YAML file to configure, a port to expose, a browser to reach it).
Commandeck takes the opposite shape: a **desktop app on your own machine**. Nothing to
host, no open port, no config files — you edit buttons in a GUI and they're stored as
plain TOML on your disk. The trade-off is deliberate: Commandeck is single-user by
design. If several people need to share a panel over the network, a web tool fits that
better; if you want this on your own laptop — including Windows and macOS — Commandeck
is built for exactly that.

## Does it phone home? Telemetry? Account?

No telemetry, no account, no cloud, no network listener. Buttons and machines are plain
TOML files on your disk; SSH keys stay where they are (Commandeck stores the *path*,
never the key). The only network traffic is the SSH connections *you* configure. See
[Security](reference/security.md).

## Isn't letting an AI run shell commands dangerous?

It would be if it were on by default — it isn't. AI execution sits behind **three
separate opt-ins**: a global setting (off by default), a per-button "AI may run this"
flag, and, for buttons with confirmation enabled, an explicit confirm round-trip.
Terminal-mode buttons can't be AI-run at all, and every AI execution is written to an
audit log. The MCP server is local-only (stdio) — nothing is exposed on the network.
Details in [AI Integration (MCP)](pro/mcp.md).

## Is it Electron? How heavy is it?

No — Commandeck is Python + Qt (PySide6) with native widgets, not a bundled browser.
Linux ships as an AppImage, macOS as a .dmg, Windows as an installer. SSH uses Paramiko,
so there's no dependency on a system OpenSSH.

## Does it work on Wayland?

Yes. A couple of window-manager niceties are honestly gated: always-on-top works on X11
and is disabled-with-a-reason on Wayland, because the compositor owns that decision.

## When is the Android app coming? iOS?

A native Android app (a full app with SSH and themes — not a web wrapper) is in closed
testing and headed for the Play Store. iOS follows Android (same codebase), no date yet.

## What happens if the project stops?

Your app keeps working. Pro is a one-time purchase with offline-friendly licensing — no
subscription to lapse, no server your buttons depend on. Your config is plain TOML on
your own disk — nothing is locked to a server or an account.

## Where is my configuration stored?

| Platform | Location |
|----------|----------|
| Linux | `~/.config/commandeck/` |
| macOS | `~/Library/Application Support/Commandeck/` |
| Windows | `%APPDATA%\Commandeck\` |

`buttons.toml` is human-readable — you can read, back up or version it however you like.
Pro adds one-click [backup & restore](pro/backup.md).

## Can I use it without any servers?

Absolutely — the free tier is exactly that: a local launcher for the commands you run on
your own machine. SSH only matters when you add remote machines (Pro).

## I found a bug / I have an idea. Where do I go?

[GitHub Issues](https://github.com/neurocontrarian/commandeck/issues) for bugs,
[Discussions](https://github.com/neurocontrarian/commandeck/discussions) for ideas and
for sharing useful buttons. Commandeck is built by one person — reports get read.
