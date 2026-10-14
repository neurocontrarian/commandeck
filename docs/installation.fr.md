# Installation

Commandeck fonctionne sur **Linux, macOS et Windows**. Chaque version liste les fichiers
des trois plateformes au même endroit :
**[GitHub Releases](https://github.com/neurocontrarian/commandeck/releases/latest)** — ce
lien pointe toujours vers la dernière version, ajoutez-le à vos favoris.

Toutes les versions **Pro** incluent un **essai gratuit de 14 jours** — sans compte,
sans carte. L'essai démarre automatiquement au premier lancement.

---

## Linux (AppImage)

Un seul fichier, aucune installation. Téléchargez-le, rendez-le exécutable, lancez-le.
L'AppImage est **autonome** : elle embarque Python, Qt et toutes les dépendances, il n'y
a donc rien à installer sur le système.

| Fichier | Quand l'utiliser |
|---------|------------------|
| `Commandeck-Linux-x86_64.AppImage` | **Gratuit — Intel/AMD.** |
| `Commandeck-Linux-ARM64.AppImage` | **Gratuit — ARM64** (Raspberry Pi 4+, serveur ARM, VM Apple Silicon). |
| `Commandeck-Pro-Linux-x86_64.AppImage` | **Pro — Intel/AMD.** Essai de 14 jours inclus. |
| `Commandeck-Pro-Linux-ARM64.AppImage` | **Pro — ARM64.** Essai de 14 jours inclus. |

Vous ne savez pas quel processeur vous avez ? Lancez `uname -m` — `x86_64` pour
Intel/AMD, `aarch64` pour ARM.

```bash
chmod +x Commandeck-*.AppImage
./Commandeck-*.AppImage
```

Si votre distribution signale un greffon de plateforme Qt manquant au lancement,
installez `libxcb-cursor0` :

=== "Debian / Ubuntu / Linux Mint"

    ```bash
    sudo apt install libxcb-cursor0
    ```

=== "Fedora"

    ```bash
    sudo dnf install xcb-util-cursor
    ```

=== "Arch Linux"

    ```bash
    sudo pacman -S xcb-util-cursor
    ```

---

## macOS (Apple Silicon)

| Fichier | Quand l'utiliser |
|---------|------------------|
| `Commandeck-macOS-AppleSilicon.dmg` | **Gratuit.** |
| `Commandeck-Pro-macOS-AppleSilicon.dmg` | **Pro.** Essai de 14 jours inclus. |

Ouvrez le `.dmg` et glissez **Commandeck** sur le dossier **Applications** — relâchez quand le
dossier se surligne. Puis **éjectez le disque** apparu sur le bureau : une app lancée depuis le
`.dmg` lui-même ne fonctionnera pas.

> **Les Mac Intel ne sont pas encore pris en charge** — la version est pour Apple Silicon (M1 ou plus récent).

L'application n'est **pas encore signée**, donc au premier lancement macOS affiche
*« Apple n'a pas pu vérifier que Commandeck ne contient pas de logiciels malveillants »*.
Il faut trois étapes pour passer :

1. Cliquez **OK** — jamais *Placer dans la corbeille*.
2. Ouvrez **Réglages Système → Confidentialité et sécurité** et descendez jusqu'à la section
   *Sécurité* : une ligne *« Commandeck » a été bloqué* propose **Ouvrir quand même**.
   Cliquez-la et confirmez avec Touch ID ou votre mot de passe. Cette ligne n'apparaît
   qu'après une tentative de lancement.
3. **Relancez Commandeck.** Le même avertissement revient, mais avec un bouton de plus :
   **Ouvrir quand même**. Cliquez-le. C'est la dernière fois que vous le verrez.

> À partir de macOS 15, le clic droit sur l'app → *Ouvrir* ne fonctionne plus pour une app non
> signée. Les Réglages Système sont le seul chemin.

Si le bouton n'apparaît pas, la même chose depuis le Terminal :

```bash
xattr -dr com.apple.quarantine /Applications/Commandeck.app
```

---

## Windows (x86_64)

| Fichier | Quand l'utiliser |
|---------|------------------|
| `Commandeck-Windows-x64.exe` | **Gratuit** — installeur (raccourci menu Démarrer + désinstallateur). |
| `Commandeck-Pro-Windows-x64.exe` | Installeur **Pro**. Essai de 14 jours inclus. |

Lancez l'installeur. Il n'est **pas encore signé**, donc SmartScreen peut vous avertir :
cliquez sur **Informations complémentaires → Exécuter quand même**.

---

## Mise à jour

Pour mettre à jour, téléchargez le dernier installateur depuis
[commandeck.app](https://commandeck.app) (ou la
[page des versions](https://github.com/neurocontrarian/commandeck/releases/latest)) et
installez-le par-dessus votre version actuelle — vos boutons et réglages sont conservés.
