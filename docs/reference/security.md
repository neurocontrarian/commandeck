# Security & how it works

🔰 **In plain terms:** Commandeck only runs the commands *you* write and click, on your own computers. It never keeps your passwords in plain text, never opens your machine up to the network during normal use, and asks you to confirm anything you've marked as important.

## Why trust this project?

- **It runs on your computer, not in the cloud.** There's no account to create and no company server holding your information. Everything Commandeck knows stays on your machine.
- **One-time purchase.** You pay once, and the version you installed keeps working. There's no subscription to cancel and no server that can quietly shut down and leave you stranded.
- **The code is open for anyone to read.** The source for the free version is public, so anyone curious — or cautious — can check exactly what the app does on their computer.
- **Available in 11 languages**, each one maintained as a real part of the app rather than an afterthought.

## Your commands, visible and editable

Every button shows its command in plain text in the [button editor](button-editor.md). Nothing is hidden or disguised — what you see is exactly what runs when you click. Commandeck never changes your commands behind your back; the only thing it ever adds is the folder or the user account you choose yourself in a profile.

## SSH authentication

When you connect Commandeck to another computer (Pro), you sign in with an **SSH key** (recommended) or a **password**. Either way, your password is never written to disk in a form anyone can read.

- A saved password is kept in your system's built-in secure storage — the same protected vault your operating system uses for its own passwords (Keychain on macOS, Credential Manager on Windows, GNOME Keyring or KWallet on Linux). It is **never copied into a backup**.
- On the rare system without that secure storage, Commandeck falls back to a scrambled local file that only your account can open, and tells you plainly that this is weaker protection.
- **The first time you connect to a new machine,** Commandeck shows you that machine's identity fingerprint and asks you to confirm it. This is the same safety check the standard `ssh` tool performs — just in a friendly dialog instead of a terminal.
- If your SSH key is protected by a passphrase, Commandeck gives you a clear message when something needs unlocking, instead of failing in silence.

## Sudo passwords

Some commands need an administrator (sudo) password to run. If you choose to save one in a [profile](execution-profiles.md), it's handled exactly like an SSH password: kept in your system's secure storage and **never written into your config files or backups** — those only note that a password exists, never the password itself. On a system without secure storage, it falls back to a scrambled file tied to that one specific computer (so it can't be copied elsewhere), with a clear warning. When a command needs it, Commandeck hands the password straight to the system, so you don't have to retype it in a terminal.

## Per-button confirmation

Any button can be set to **Confirm before running** (button editor → Behaviour). When it's on, Commandeck shows you the exact command and waits for your OK before doing anything — a good idea for restarts, deletions, and anything that needs an administrator password.

## AI / MCP access (Pro)

Commandeck can connect to an AI assistant so it can help you read and organise your buttons. This is completely optional and stays **switched off until you turn it on**. Several independent locks keep you in control:

- The assistant can only see or change your buttons after you switch on *Allow MCP access* in Preferences.
- Before it can run a button for you, **three** separate permissions all have to be on: a master switch, a per-button switch, and — for anything sensitive — a final confirmation. If even one of them is off, nothing runs.
- Every action the assistant takes is written to a log on your computer, with the time, the button, the result, and how long it took, so you can always see exactly what happened.
- When launched by a desktop assistant, the connection stays entirely on your computer and opens no network port. (One optional add-on, for a specific web-based tool, does open a local connection — if you use it, keep it inside your home network, behind your firewall.)

## What Commandeck protects against

Commandeck is a **personal desktop tool**. It assumes the person sitting at the computer is allowed to run commands on their own machines.

Its safeguards are there to prevent *accidents* and surprises: running the wrong thing by mistake, letting a saved password slip into a backup or a synced folder, or an AI assistant acting without your say-so. That's what the confirmations, the secure password storage, and the AI locks are all designed to catch.

What it does **not** try to do is protect your computer from someone who has already taken over your account or who is sitting at your unlocked machine. No desktop app can — at that point they could run those commands themselves anyway. Keeping your computer and your account secure (a screen lock, a strong login password) is the foundation Commandeck builds on.
