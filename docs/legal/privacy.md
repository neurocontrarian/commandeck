---
description: Commandeck privacy policy — no account, no telemetry, no cloud. Your configuration stays on your device. Covers desktop (Linux/macOS/Windows) and Android.
---

# Privacy Policy

*Last updated: September 2026*

Commandeck is a command-launcher app available on **Linux, macOS, Windows and Android**. This
policy explains what data is — and is not — involved when you use it. The short version:
**Commandeck has no user accounts, runs no data-collecting server, and your configuration stays
on your own device.**

## The short version

- No account, no sign-up.
- **The apps** contain no analytics, no telemetry and no usage tracking — they never report
  what you do back to us.
- **This website** carries no analytics script. The only thing counted is a click on a download
  button, with no cookie and nothing that identifies you — see *This website* below.
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
  identity), used as the activation's name so the license stays tied to that device.

The purchase email you type is compared on your device with the one LemonSqueezy returns; it is
not sent. Afterwards, at most about once every 30 days and only when the app starts, the license
key and the activation's identifier are sent to confirm the license is still valid. Nothing else
is sent, and the app works fully offline between checks — a check that cannot connect is skipped.

### Android (Google Play)

On Android, the paid app (a one-time purchase) is sold and processed by **Google Play**. Google is the
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

## This website (commandeck.app)

The website — the pages you are reading right now — carries **no analytics script at all**: no
Umami, no Google Analytics, nothing that loads in your browser to watch what you do.

One thing is counted, and only one. A **download button** sends you through
`commandeck.app/get/…`, which records four things before redirecting you to the file:

- which file was asked for and whether it is the free or the Pro edition,
- your country,
- which page or post the link came from, when the link says so (for example a link we posted in a
  forum thread).

That is the whole record. **No cookie is set, no IP address is stored, no browser fingerprint, no
identifier of any kind** — nothing that could be traced back to you, and nothing that is kept about
people who simply read the pages. We do it to know whether the site does its job; we count the
click, not the person.

None of this reaches the app you install. Using Commandeck is not tracked.

## What we do not collect

- No analytics or usage data **in the apps**; we do not track which commands you run.
- No access to your SSH credentials or private keys.
- No cookies, on the website or in the apps.
- No advertising, no advertising identifiers, and no tracking of you across other websites.
- The apps contain **no third-party advertising or analytics SDKs**.

## Third-party services

- [LemonSqueezy](https://www.lemonsqueezy.com) — desktop license and payment processing; their
  privacy policy applies to the data they process.
- **Google Play** — Android paid-app purchase processing; Google's privacy policy applies.
- [Cloudflare](https://www.cloudflare.com) — serves this website and handles the download links; as with any web host, it processes the traffic needed to deliver the pages.

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
