# Activating your license

Welcome to Commandeck Pro! This guide walks you through activating your license for the first time.

!!! tip "What you'll need"
    - Your **license key** (sent in your purchase email from LemonSqueezy)
    - The **email address** you used when buying
    - An **internet connection** (required for the first activation only)

---

## Download and install

Your purchase email from LemonSqueezy has a **Files** link and a download button. You can also grab the newest build any time from the [releases page](https://github.com/neurocontrarian/commandeck/releases/latest) — Linux, macOS and Windows are all there. Pick the file for your system and follow the matching tab below.

=== "Linux"
    Download `Commandeck-Pro-…-x86_64.AppImage` (or the `-ARM64` file on a Raspberry Pi or other ARM machine).

    **The easy way — no terminal:** right-click the downloaded file → **Properties** → **Permissions** tab → tick **"Allow executing file as program"** (some desktops label it **"Is executable"**). Close the window, then **double-click** the file to launch Commandeck.

    Prefer the terminal? The same thing in one line:
    ```bash
    chmod +x Commandeck-Pro-*.AppImage && ./Commandeck-Pro-*.AppImage
    ```

    !!! info "If it won't start"
        The AppImage is self-contained — Python, Qt and every SSH library (Paramiko,
        cryptography…) are bundled, so there's no `pip install` to do. If your
        distribution reports a missing Qt platform plugin, install `libxcb-cursor0`:
        ```bash
        sudo apt install libxcb-cursor0     # Ubuntu / Mint / Debian
        sudo dnf install xcb-util-cursor    # Fedora
        ```

=== "macOS"
    Open the downloaded `.dmg`, then drag the **Commandeck** icon onto the **Applications** folder shown beside it.

    On the **first launch only**, open Commandeck from Applications with a **right-click → Open → Open**. This clears the one-time "unidentified developer" warning macOS shows for apps installed outside the App Store. After that, launch it normally.

=== "Windows"
    Run the downloaded `.exe` installer and follow the prompts.

    If Windows SmartScreen shows a blue **"Windows protected your PC"** box, click **More info → Run anyway**. It appears for brand-new apps Microsoft hasn't yet seen downloaded many times — expected for a fresh release.

---

## Step-by-step activation

1. **Open Commandeck** — make sure you're running the **Pro build**, not the Free build. ([What's the difference?](../pro.md#free-vs-pro))

2. **Open Preferences** with `Ctrl + ,` or via the hamburger menu → *Preferences*.

3. **Scroll to the *License* section.**

    ![License section in Preferences](../assets/license-section.png)

4. **Paste your license key** in the *License key* field.

5. **Enter the email** you used at purchase in the *Email* field.

    !!! warning "Email must match exactly"
        We compare what you type against the email LemonSqueezy has on file for the purchase. If it doesn't match, activation is refused — no slot is consumed.

6. Click **Activate Pro**.

7. Within a few seconds, the dialog refreshes and shows:
    - Your license **type**
    - The **renewal date** (for a yearly subscription)
    - Your **activation count** (e.g. *1 / 3*)

That's it — every Pro feature is now unlocked. SSH machines, multi-machine buttons, themes, backup, MCP server, all available.

---

## What happens next

| When | What happens |
|---|---|
| Right after activation | All Pro features unlock immediately |
| About once a month, at startup | Commandeck quietly confirms your license is still active. Nothing to do — and being offline never locks you out. |
| 30 days before expiry | A toast warns you that your subscription is about to renew |
| Day of expiry | LemonSqueezy renews your subscription automatically — nothing to do |
| If renewal fails | A 3-day grace period kicks in before Pro features lock |

If your subscription lapses, **your data is never deleted**. Buttons, machines, settings — all preserved. Re-activate any time and everything comes back.

---

## Troubleshooting

### *"This license key is registered to a different email."*

The email you typed doesn't match the one on the LemonSqueezy purchase. Double-check the receipt email you got from LemonSqueezy and use that exact address (case doesn't matter, but typos do).

### *"You have reached the maximum of 3 activations."*

You've used all 3 device slots for this license. Open Commandeck on one of your active devices, go to **Preferences → License → Deactivate**, then come back and activate here.

Lost access to a device you activated (lost laptop, OS reinstalled without deactivating)? [Email support](mailto:neurocontrarian@gmail.com) and we'll sort it out with you.

See the full [License & Devices guide](license-devices.md) for every scenario.

### *"Network error — could not reach the license server."*

The first activation **requires** an internet connection (we check the key against LemonSqueezy). Make sure Commandeck can reach `api.lemonsqueezy.com` — corporate proxies and strict firewalls may block it.

After the first activation, Commandeck works **offline indefinitely** — being disconnected never locks you out. It only re-checks your license about **once a month**, on startup, and if that check can't reach the internet it's simply skipped until next time.

### *I don't see a "License" section in Preferences*

You're running the **Free build**. The Free build has no license system — there's nothing to activate. To use Pro, [download the Pro build](../pro.md#download) and run it instead. Your buttons, machines and settings will be picked up automatically (same config directory).

---

## Where to go from here

- **[Add your first SSH machine](../reference/ssh-machines.md)** — the Pro feature most people start with
- **[Create a multi-machine button](../reference/ssh-machines.md#assigning-machines-to-a-button)** — run one command on a fleet
- **[License & Devices](license-devices.md)** — everything about the 3-device limit, OS reinstalls, migrations
- **[Refund policy](../legal/refund.md)** — 14 days, no questions asked

Need anything else? [Email support](mailto:neurocontrarian@gmail.com) — we read every message.
