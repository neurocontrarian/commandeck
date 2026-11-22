# « Exécuter en tant que » enregistrés

!!! tip "Fonctionnalité Pro"
    Les « Exécuter en tant que » enregistrés nécessitent [Commandeck Pro](../pro.fr.md).

🔰 **En clair :** un « Exécuter en tant que » enregistré (aussi appelé profil) est un petit jeu de « conditions d'exécution » que vous enregistrez une fois et réutilisez sur plusieurs boutons — *qui* exécute la commande (un autre utilisateur) et *où* elle s'exécute (un dossier). Plutôt que d'écrire `sudo -u www-data` et `cd /var/www` dans chaque bouton, vous le définissez une fois et le choisissez sur le bouton.

Un profil ne contient **aucun mot de passe**. Pour agir au nom d'un autre utilisateur, `sudo` demande le mot de passe du compte avec lequel vous êtes *connecté* — ce mot de passe vit donc dans la [fiche de la machine](ssh-machines.fr.md#mot-de-passe-administrateur) (ou dans [Préférences › Cet ordinateur](preferences.fr.md#cet-ordinateur) pour cet ordinateur), et un même profil sert sur toutes les machines.

![Liste des « Exécuter en tant que » enregistrés](../assets/profiles-list.png)

## Créer un profil

Ouvrez **Menu ☰ → « Exécuter en tant que » enregistrés → Ajouter un profil**, puis remplissez :

![Éditeur de profil](../assets/profile-dialog.png)

| Champ | Rôle |
|-------|------|
| **Nom** | Comment le profil apparaît dans la liste **Exécuter en tant que** de l'éditeur de bouton (sous la forme « Enregistré : … »). |
| **Exécuter en tant qu'utilisateur** | Exécute la commande sous cet utilisateur au lieu du vôtre (utilise `sudo -u <user>`). Laissez vide pour rester vous-même. |
| **Répertoire de travail** | Le dossier où la commande démarre (comme un `cd` préalable). |
| **Description** | Note facultative pour vous rappeler à quoi sert le profil. |

## Utiliser un profil sur un bouton

Dans l'[éditeur de bouton](button-editor.fr.md), choisissez votre profil dans la liste **Exécuter en tant que** — il y figure sous la forme **Enregistré : *nom***. Le bouton s'exécute alors avec l'utilisateur et le dossier du profil — le champ commande reste propre, ne contenant que la commande réelle.

!!! example "Avant / après"
    Au lieu d'un bouton avec `sudo -u www-data bash -c 'cd /var/www/app && git pull'`, créez :

    - un profil **Déploiement Web** → *Exécuter en tant que* `www-data`, *Répertoire de travail* `/var/www/app`
    - un bouton avec la commande `git pull`, profil **Déploiement Web**

    Plus propre, et le même profil se réutilise pour chaque bouton d'appli web.

!!! example "Éteindre une machine distante — le cas d'école"
    Utilisé via SSH (par exemple depuis votre téléphone), le bouton **Éteindre** par défaut échoue avec un message d'authentification. La commande est bonne : éteindre une machine demande des **droits administrateur**, et une connexion à distance ne les obtient pas automatiquement comme lorsque vous êtes assis devant l'ordinateur. (Sur votre propre PC, le même bouton marche directement.) Le bouton **Redémarrer** est dans le même cas.

    La solution est dans la **fiche de la machine**, pas dans le bouton :

    - si vous vous connectez par **mot de passe**, laissez cochée **C'est aussi le mot de passe administrateur (sudo)** — rien d'autre à faire ;
    - si vous vous connectez par **clé SSH**, tapez votre mot de passe sur cette machine dans **Mot de passe admin**.

    Quand un bouton échoue faute de droits administrateur, Commandeck le relance une fois en administrateur avec ce mot de passe — sans profil, sans toucher à la commande. Pareil pour tout ce qui demande des droits admin sur cette machine — redémarrer un service, installer un logiciel, monter un disque. **Tester** dans la fiche de la machine vous dit si les droits administrateur fonctionnent.

⚙️ **Pour les sysadmins**

- *Exécuter en tant que* enveloppe la commande avec `sudo -u <user>`. sudo authentifie le compte **connecté** : Commandeck lui répond avec le mot de passe admin de la fiche machine (ou de Cet ordinateur), passé par l'entrée standard (`sudo -S`) — jamais sur la ligne de commande, et la commande elle-même démarre sur une entrée vide.
- Un profil s'applique de la **même** façon en local et via SSH — l'enveloppe `sudo -u` / répertoire de travail a lieu sur la machine ciblée par le bouton.
- Les profils se marient bien avec les [boutons multi-machines](../use-cases/homelab.fr.md) : un profil « déploiement », un bouton, plusieurs serveurs.
- Un assistant IA peut créer et assigner des profils pour vous via le [serveur MCP](../pro/mcp.fr.md) — il décompose automatiquement une commande shell collée en un profil + une commande propre.
