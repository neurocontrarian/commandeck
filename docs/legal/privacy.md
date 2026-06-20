---
description: Commandeck privacy policy — no account, no telemetry, no cloud. Your configuration stays on your device. Covers desktop (Linux/macOS/Windows) and Android.
---

# Privacy Policy

*Last updated: June 2026*

Commandeck is a command-launcher app available on **Linux, macOS, Windows and Android**. This
policy explains what data is — and is not — involved when you use it. The short version:
**Commandeck has no user accounts, runs no data-collecting server, and your configuration stays
on your own device.**

## The short version

- No account, no sign-up.
- No analytics, no telemetry, no usage tracking, no cookies.
- Your buttons, SSH machine definitions and execution profiles stay **on your device** — they are
  never sent to us.
- We never have access to your SSH keys, your credentials, or the commands you run.
- Purchases are handled by a third-party processor (LemonSqueezy on desktop, Google Play on
  Android) — not by us.

## Provider

Commandeck is operated by **neurocontrarian**, located in Québec, Canada.
**Contact for any privacy inquiry:** [neurocontrarian@gmail.com](mailto:neurocontrarian@gmail.com)

## Purchases

### Desktop (Linux, macOS, Windows)

The Pro license is sold through [LemonSqueezy](https://www.lemonsqueezy.com), acting as Merchant
of Record — they are responsible for payment data and receive your email and payment details. We
receive only your email address (for license validation) and aggregate sales reports; we never
see your card details.

When you activate a Pro license, the following is sent to LemonSqueezy's API to validate it and
manage your activation slots (max 3 devices):

- your license key,
- an anonymous, hashed device identifier (derived from the machine ID — not linked to your
  identity),
- the activation name (your hostname, optional).

The app works fully offline between checks (at most one validation roughly every 30 days).

### Android (Google Play)

On Android, the one-time purchase is sold and processed by **Google Play Billing**. Google is the
payment processor, and your purchase is governed by Google's Privacy Policy and Google Play terms.
The Android app has **no separate license server, no account, and transmits no personal data** —
your purchase status is provided by Google Play on your device.

## Stored locally on your device

Commandeck stores your configuration **locally** — on desktop under `~/.config/commandeck/` (and
the platform equivalent on macOS/Windows), and on Android within the app's private storage:

- your button configuration,
- your SSH machine definitions (host / user / port — **private keys are never stored here and
  never transmitted**),
- your execution profiles (sudo passwords are encoded with a device-specific key and never
  transmitted anywhere).

None of these files leave your device.

## What we do not collect

- No analytics or usage data; we do not track which commands you run.
- No access to your SSH credentials or private keys.
- No cookies or web tracking.
- The apps contain **no third-party advertising or analytics SDKs**.

## Third-party services

- [LemonSqueezy](https://www.lemonsqueezy.com) — desktop license and payment processing; their
  privacy policy applies to the data they process.
- **Google Play Billing** — Android in-app purchase processing; Google's privacy policy applies.

## Data retention

We store no personal data on our servers. Your configuration remains on your device.

## Your rights

You may contact us for any data-protection request. On desktop, deactivating your license removes
the device activation record from LemonSqueezy's servers. On Android, your purchase is managed
from your Google Play account.

## Changes to this Policy

We reserve the right to update this Privacy Policy at any time, at our sole discretion. Changes
become effective immediately upon posting to this page. The "Last updated" date above reflects the
most recent revision. We encourage you to review this page periodically.

## Contact

For any question or to exercise your data-protection rights:
[neurocontrarian@gmail.com](mailto:neurocontrarian@gmail.com)
