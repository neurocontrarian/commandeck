# Activer votre licence

Bienvenue dans Commandeck Pro ! Ce guide vous accompagne pour activer votre licence sur votre premier appareil.

!!! tip "Ce dont vous avez besoin"
    - Votre **clé de licence** (envoyée dans l'email d'achat LemonSqueezy)
    - L'**adresse email** utilisée lors de l'achat
    - Une **connexion internet** (uniquement pour la première activation)

---

## Télécharger et lancer

Votre email d'achat LemonSqueezy contient un lien **Files** et un bouton de téléchargement. Vous pouvez aussi récupérer la dernière version à tout moment depuis la [page des versions](https://github.com/neurocontrarian/commandeck/releases/latest) — Linux, macOS et Windows y sont tous. Choisissez le fichier de votre système et suivez l'onglet correspondant ci-dessous.

=== "Linux"
    Téléchargez `Commandeck-Pro-…-x86_64.AppImage` (ou le fichier `-ARM64` sur un Raspberry Pi ou une autre machine ARM).

    **Le plus simple — sans terminal :** faites un clic droit sur le fichier téléchargé → **Propriétés** → onglet **Permissions** → cochez **« Autoriser l'exécution du fichier comme un programme »** (certains bureaux affichent **« Est exécutable »**). Fermez la fenêtre, puis **double-cliquez** sur le fichier pour lancer Commandeck.

    Vous préférez le terminal ? La même chose en une ligne :
    ```bash
    chmod +x Commandeck-Pro-*.AppImage && ./Commandeck-Pro-*.AppImage
    ```

    !!! info "S'il ne démarre pas"
        L'AppImage est autonome — Python, Qt et toutes les bibliothèques SSH (Paramiko,
        cryptography…) sont incluses, donc aucun `pip install` à faire. Si votre
        distribution signale un greffon de plateforme Qt manquant, installez `libxcb-cursor0` :
        ```bash
        sudo apt install libxcb-cursor0     # Ubuntu / Mint / Debian
        sudo dnf install xcb-util-cursor    # Fedora
        ```

=== "macOS"
    Ouvrez le `.dmg` téléchargé, puis glissez l'icône **Commandeck** sur le dossier **Applications** affiché à côté.

    **Au tout premier lancement uniquement**, ouvrez Commandeck depuis Applications avec un **clic droit → Ouvrir → Ouvrir**. Cela lève l'avertissement unique « développeur non identifié » que macOS affiche pour les apps installées hors de l'App Store. Ensuite, lancez-la normalement.

=== "Windows"
    Lancez l'installateur `.exe` téléchargé et suivez les étapes.

    Si Windows SmartScreen affiche un cadre bleu **« Windows a protégé votre ordinateur »**, cliquez sur **Informations complémentaires → Exécuter quand même**. Il apparaît pour les apps récentes que Microsoft n'a pas encore vues téléchargées souvent — c'est normal pour une nouvelle version.

---

## Activation pas à pas

1. **Ouvrez Commandeck** — assurez-vous d'utiliser la version **Pro**, pas la version Free. ([Quelle est la différence ?](../pro.fr.md#free-vs-pro))

2. **Ouvrez les Préférences** avec `Ctrl + ,` ou via le menu burger → *Préférences*.

3. **Descendez jusqu'à la section *Licence*.**

    ![Section Licence dans les Préférences](../assets/license-section.png)

4. **Collez votre clé de licence** dans le champ *Clé de licence*.

5. **Saisissez l'email** utilisé à l'achat dans le champ *Email*.

    !!! warning "L'email doit correspondre exactement"
        Nous comparons ce que vous tapez à l'email enregistré chez LemonSqueezy pour cet achat. En cas de différence, l'activation est refusée — aucune activation n'est consommée.

6. Cliquez sur **Activer Pro**.

7. En quelques secondes, la boîte de dialogue se met à jour et affiche :
    - Le **type** de licence
    - Le **nombre d'activations** (ex. *1 / 3*)

C'est tout — toutes les fonctionnalités Pro sont maintenant déverrouillées. Machines SSH, boutons multi-machines, thèmes, sauvegarde, serveur MCP, tout est disponible.

---

## Ce qui se passe ensuite

| Quand | Ce qui se passe |
|---|---|
| Juste après l'activation | Toutes les fonctionnalités Pro sont déverrouillées immédiatement |
| Environ une fois par mois, au démarrage | Commandeck vérifie discrètement que votre licence est toujours active. Rien à faire — et être hors-ligne ne vous bloque jamais. |

Vos données ne sont jamais en danger. Boutons, machines, réglages — tout est conservé, quel que soit l'état de la licence.

---

## En cas de problème

### *« Cette clé est enregistrée pour un autre email. »*

L'email que vous avez tapé ne correspond pas à celui de l'achat LemonSqueezy. Vérifiez l'email du reçu LemonSqueezy et utilisez cette adresse exacte (la casse n'importe pas, mais les fautes de frappe oui).

### *« Vous avez atteint la limite de 3 activations. »*

Vous avez utilisé les 3 emplacements d'activation de cette licence. Ouvrez Commandeck sur un de vos appareils actifs, allez dans **Préférences → Licence → Désactiver**, puis revenez ici pour activer.

Vous n'avez plus accès à un appareil activé (laptop perdu, OS réinstallé sans désactiver) ? [Écrivez au support](mailto:neurocontrarian@gmail.com) et nous verrons ensemble comment vous dépanner.

Voir le guide complet [Licence et appareils](license-devices.fr.md) pour tous les cas de figure.

### *« Erreur réseau — impossible de joindre le serveur de licences. »*

La première activation **nécessite** une connexion internet (nous vérifions la clé auprès de LemonSqueezy). Assurez-vous que Commandeck peut joindre `api.lemonsqueezy.com` — les proxies d'entreprise et pare-feu stricts peuvent le bloquer.

Après la première activation, Commandeck fonctionne **hors-ligne sans limite** — être déconnecté ne vous bloque jamais. Il revérifie votre licence seulement **une fois par mois environ**, au démarrage, et si cette vérification ne peut pas joindre internet, elle est simplement ignorée jusqu'à la prochaine fois.

**Une seule exception, une seule fois :** une licence activée avec une version antérieure à 2.4.4 doit être confirmée en ligne la première fois que vous ouvrez la 2.4.4 ou plus récente. Ouvrez Commandeck une fois connecté après la mise à jour ; ensuite, le hors-ligne fonctionne de nouveau.

### *L'onglet Licence indique « Ceci est l'édition gratuite de Commandeck »*

Vous utilisez la version **Free**. Elle ne contient aucun code Pro : une clé de licence n'a donc rien à y débloquer. Cliquez sur **Télécharger Commandeck Pro** dans cet onglet — vous obtenez la dernière version Pro pour votre système — et lancez-la à la place. Vos boutons, machines et réglages seront repris automatiquement (même répertoire de configuration). **À propos**, dans le menu ☰, indique aussi quelle édition vous utilisez.

### *« Votre licence doit être réactivée sur cet appareil »*

Commandeck ne reconnaît plus l'activation de cet appareil. Cela arrive quand :

- le fichier de licence a été **copié depuis un autre ordinateur** (une licence est liée à l'appareil sur lequel elle a été activée),
- le système a été **réinstallé**, ou l'ordinateur remplacé,
- l'emplacement de cet appareil a été **libéré** depuis un autre appareil, ou LemonSqueezy ne le connaît plus.

Votre clé est conservée et déjà remplie : cliquez sur **Activer Pro** avec une connexion internet. Sur un nouvel appareil, cela utilise l'un de vos 3 emplacements — voir [Licence et appareils](license-devices.fr.md).

---

## Pour aller plus loin

- **[Ajouter votre première machine SSH](../reference/ssh-machines.fr.md)** — la fonction Pro par laquelle la plupart des gens commencent
- **[Créer un bouton multi-machines](../reference/ssh-machines.fr.md#assigner-des-machines-à-un-bouton)** — lancer une commande sur tout un parc
- **[Licence et appareils](license-devices.fr.md)** — tout sur la limite de 3 appareils, réinstallations OS, migrations
- **[Politique de remboursement](../legal/refund.fr.md)** — la garantie 14 jours et ce qu'elle couvre

Besoin d'autre chose ? [Écrivez au support](mailto:neurocontrarian@gmail.com) — nous lisons chaque message.
