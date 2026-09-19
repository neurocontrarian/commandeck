# SSH Machines

!!! tip "Pro feature"
    SSH machines require [Commandeck Pro](../pro.md).

Commandeck connects to remote servers over SSH. You can authenticate either with an **SSH key** (recommended) or with a **password**. When you choose password authentication, the password is kept in your operating system's secure keychain — never in plain text in a config file, and never included in a backup.

---

## Managing machines

Open **Menu → Manage Machines** to see the full machine list. From here you can add, edit, and delete machines.

![Manage Machines dialog](../assets/machines-list.png)

!!! note
    The **Manage Machines** menu item is locked on the free tier.

---

## Detecting machines on the network

Instead of typing an IP address by hand, click **Detect** in the Manage Machines dialog. Commandeck scans your local network for devices that accept SSH connections (port 22) and lists the ones it finds.

1. Commandeck fills in the **Subnet** of your network automatically (for example `192.168.1.`). If your machines are on a different range — a VPN, or a router that uses `192.168.0.` — edit this field, then click **Scan**.
2. Pick a device from the results and click **Add This Machine**. The Add Machine form opens with the IP address and name already filled in — you just set the SSH user and key, then **Test** and **Save**.

Machines you have already added are hidden from the results, so only new devices are offered.

!!! tip "Make device names show up"
    Commandeck tries to discover each device's name automatically, in this order: reverse DNS, then **mDNS / Bonjour** (the `.local` names that Macs, Raspberry Pi / avahi and most NAS announce), then **NetBIOS** (Windows and Samba). Devices that don't announce themselves — typically headless servers and Docker containers — show only their IP address.

    To get a name for those too, your router/DNS has to answer reverse lookups for your local network. On **OPNsense / pfSense with Unbound**, enable *Register DHCP leases* and *Register DHCP static mappings*. If a DNS filter such as **AdGuard Home** or Pi-hole sits in front of Unbound, point its *private reverse DNS servers* at the Unbound resolver so private `PTR` lookups are answered. Verify from a terminal with `getent hosts <ip>` — once it returns the name, re-scan and Commandeck shows it too.

!!! note
    Detection finds devices that have SSH (port 22) open. A device protected by a firewall may not appear even if it runs SSH.

---

## Add Machine dialog

Click **+** in the Machines dialog to open the Add Machine form.

![Add Machine dialog](../assets/machine-dialog.png)

### Name

A display name used only inside Commandeck. Choose something descriptive — you will see this name in button editors and the machine picker.

Examples: `Plex Server`, `Pi-hole`, `Work VPS`, `NAS`

### Host / IP

The IP address or hostname of the remote machine. This must be reachable from your computer over the network.

Examples: `192.168.1.50`, `plex.local`, `myserver.example.com`

### SSH User

The username to log in with on the remote machine.

Examples: `pi`, `ubuntu`, `admin`, `yourname`

### Port

The SSH port. Default is **22**. Change this only if your server runs SSH on a non-standard port.

### Authentication

Choose how Commandeck logs in to this machine:

- **SSH Key** *(recommended)* — uses a private key file (see [SSH Key Path](#ssh-key-path) below). Nothing to type or store once it is set up.
- **Password** — connect with a password that Commandeck stores in your OS keychain (see [SSH Password](#ssh-password) below).

SSH keys are the more secure and convenient option — once configured, you never type a password again. Password authentication is there for servers where you can't install a key.

### SSH Key Path

The path to the private key file used for authentication.

Examples: `~/.ssh/id_rsa`, `~/.ssh/id_ed25519`, `~/.ssh/myserver_key`

If the field is empty, Commandeck falls back to your SSH agent or the default key (`~/.ssh/id_rsa`).

!!! note
    Keys with a passphrase require a running `ssh-agent` with the key loaded. If the key is locked, Commandeck shows a clear error — it will not prompt for the passphrase interactively.

### SSH Password

Only used when **Authentication** is set to **Password**. Enter the remote user's login password; Commandeck saves it and uses it for every connection to this machine. Use **Test** to confirm the password works before saving.

!!! info "Where your password is stored"
    Stored passwords live in your operating system's secure keychain — **GNOME Keyring / KWallet** on Linux, **Keychain** on macOS, **Credential Manager** on Windows — encrypted at rest. They are **never** written to Commandeck's config files and **never** included in a backup.

    If no system keychain is available (for example a minimal or headless Linux box), Commandeck falls back to a local obfuscated file (`.secrets`, readable only by your user account) and warns you that this is not strong encryption. Prefer an SSH key in that case.

### Icon

A visual icon shown next to the machine name in the picker dialog and the machine list. Six icons are available: desktop, laptop, server, router, Wi-Fi access point, and a generic device.

---

## SSH key setup

If you don't have an SSH key pair yet, Commandeck can generate one for you and copy the public key to the server:

1. Click **Generate SSH key** — Commandeck creates an Ed25519 key pair in `~/.ssh/`
2. Click **Copy key to server** — enter your password once (it is not stored). This runs `ssh-copy-id` internally
3. Future connections use the key automatically, no password needed

---

## Testing the connection

Click **Test** in the machine dialog. Commandeck runs `echo commandeck-ok` on the remote host. A green message confirms the connection works. If it fails, the full error from SSH is shown.

Run the test after adding a machine and whenever you change credentials.

---

## Assigning machines to a button

In the [Button Editor](button-editor.md), the **Target machines** section shows your machines as toggle switches. Enable the machines you want.

---

## The machine picker

When a button has two or more targets enabled, clicking it opens the machine picker dialog.

![Machine picker](../assets/machine-picker.png)

The picker lists each enabled target. Select one and click **Run**. The command runs on the selected machine only.

!!! tip
    If you want to run on all machines at once without picking, you can do so by creating separate buttons per machine, or by using multi-select to run them in sequence.

---

## Output modes over SSH

All three execution modes work over SSH:

| Mode | Behaviour |
|------|-----------|
| **Silent** | Result shown as a toast notification |
| **Show output** | Remote `stdout`/`stderr` displayed in a dialog after the command finishes |
| **Open in terminal** | Commandeck generates an `ssh -t` command and opens it in your terminal emulator — full interactive session |
