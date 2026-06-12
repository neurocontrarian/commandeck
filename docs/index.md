---
description: Commandeck is a desktop app for Windows, macOS and Linux that turns your server and shell commands into clickable buttons — run them locally or over SSH, no terminal required.
---

# Welcome to Commandeck

**Your AI gives you the commands. Commandeck remembers them.**

Commandeck is a desktop app for Windows, macOS and Linux that turns commands into a grid
of clickable buttons. Click one — it runs on your machine, or on your home server over
SSH, and shows the output. No terminal required.

<video controls preload="metadata" style="width:100%;max-width:570px;border-radius:8px;">
  <source src="/assets/Commandeck-Demo-01.mp4" type="video/mp4">
  Your browser can't play embedded video — <a href="/assets/Commandeck-Demo-01.mp4">download the demo</a>.
</video>

[Download Commandeck](https://github.com/neurocontrarian/commandeck/releases/latest){ .md-button .md-button--primary }
[Pro & pricing](pro.md){ .md-button }

---

## Who is Commandeck for?

<div class="grid cards" markdown>

-   :material-robot-happy:{ .lg .middle } **Built your server with an AI's help?**

    ---

    A NAS, Jellyfin, Docker on a mini-PC — and dozens of commands collected from
    chats and guides that you re-hunt every time something needs attention.
    Commandeck is where they become buttons: one click from your Windows or Mac
    desktop, the command runs on your server over SSH.

    [:octicons-arrow-right-24: Home server guide](use-cases/home-server.md)

-   :material-cursor-default-click:{ .lg .middle } **New to the command line?**

    ---

    No memorizing anything. Commandeck ships with dozens of ready-to-use buttons —
    check disk usage, update your system, reboot — and creating your own takes
    30 seconds.

    [:octicons-arrow-right-24: Beginner guide](use-cases/beginner.md)

-   :material-server-network:{ .lg .middle } **Managing several machines?**

    ---

    A visual SSH command launcher: assign a button to one or more hosts, run it
    everywhere in a single click — and drive it all from an AI assistant via the
    [MCP server](pro/mcp.md).

    [:octicons-arrow-right-24: SSH & multi-machine](pro/ssh.md)

</div>

---

## What makes Commandeck different

- **Install and go — nothing to host.** No server, no Docker, no YAML, no port to
  expose. Commandeck is a native desktop app: open it and click.
- **SSH built in.** Add a machine once, then pick the target at click time — and one
  button can run on several machines at once.
- **Your commands, visible and organized.** Labeled buttons in categories — no
  memorizing aliases, no digging through old AI chats or notes files. Edit everything
  visually; no config files to hand-edit.
- **AI-friendly.** An AI assistant can create buttons for you via the built-in
  [MCP server](pro/mcp.md) — "add a button that restarts nginx" → it appears in your grid.
- **Local and private.** Your buttons are plain-text files on your own machine. No
  cloud, no account, no telemetry.

It works *alongside* your terminal, not instead of it — Commandeck handles the
repetitive clicks; you keep the terminal for interactive work.

---

## Quick start

1. [Install Commandeck](installation.md)
2. Launch the app — dozens of default buttons are ready to use
3. Follow the [Quick Start guide](quick-start.md) to create your first custom button
4. Got a server? [Add it as an SSH machine](pro/ssh.md) and point buttons at it

!!! tip "Try Pro free for 14 days"
    The Pro build includes an automatic [14-day trial](pro.md#14-day-free-trial) — every
    feature unlocked, no card, no email. Just download the Pro build and launch it.

---

## What's in the box

| Feature | Available in |
|---------|-------------|
| Ready-to-use default buttons, organised by category | Free |
| Unlimited local command execution | Free |
| Custom buttons | Free (unlimited) |
| Categories, icons, colors, tooltips | Free |
| SSH machines | [Pro](pro.md) |
| Multi-machine buttons | [Pro](pro.md) |
| Multi-select + group actions | [Pro](pro.md) |
| Button themes | [Pro](pro.md) |
| Config backup / restore | [Pro](pro.md) |
| Execution profiles (run-as-user + sudo password) | [Pro](pro.md) |
| MCP server (AI assistant integration) | [Pro](pro.md) |
