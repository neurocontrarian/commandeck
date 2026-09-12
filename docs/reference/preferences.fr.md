# Préférences

Ouvrez les Préférences depuis le menu hamburger ou avec `Ctrl+,`.

Les paramètres sont enregistrés immédiatement lorsque vous les modifiez — il n'y a pas de bouton Enregistrer.

---

## Général

![Préférences — Général](../assets/preferences-general.png)

### Langue

Sélectionne la langue de l'interface. Commandeck prend en charge 12 langues :

| Code | Langue |
|------|--------|
| Système | Suivre la locale du bureau (par défaut) |
| en | Anglais |
| fr | Français |
| de | Allemand |
| es | Espagnol |
| it | Italien |
| pt | Portugais |
| ru | Russe |
| ko | Coréen |
| ja | Japonais |
| zh | Chinois (simplifié) |
| ar | Arabe |
| hi | Hindi |

!!! note
    Un changement de langue prend effet après le redémarrage de Commandeck. Une notification toast vous le rappelle.

### Délai d'expiration des commandes

La durée maximale (en secondes) d'attente de la fin d'une commande avant annulation. Par défaut : **30 secondes**.

Augmentez cette valeur pour les commandes censées prendre du temps (copies de grands fichiers, mises à jour système). Diminuez-la pour échouer rapidement sur des machines inaccessibles.

### Disposition de la grille

Il n'y a pas de réglage « boutons par ligne » — la grille se réorganise automatiquement selon la largeur de la fenêtre. Redimensionnez la fenêtre pour plus ou moins de colonnes (jusqu'à une seule colonne). Pour changer la taille des tuiles, utilisez **Taille des boutons** dans [Apparence des boutons](#apparence-des-boutons).

### Confirmer avant d'exécuter par défaut

Lorsque cette option est activée, la case **Confirmer avant d'exécuter** dans l'éditeur de bouton est pré-cochée pour chaque nouveau bouton créé.

N'affecte pas les boutons existants.

---

## Apparence des boutons

![Préférences — Apparence des boutons](../assets/preferences-appearance.png)

### Taille des boutons

Définit la taille de toutes les tuiles de boutons globalement.

| Taille | Dimensions de la tuile | Taille de l'icône |
|--------|------------------------|-------------------|
| Petite | 80 × 80 px | 20 px |
| Moyenne | 120 × 120 px | 32 px |
| Grande | 160 × 160 px | 48 px |

### Thème des boutons

!!! tip "Fonctionnalité Pro"
    Les thèmes de boutons nécessitent [Commandeck Pro](../pro.md). Dans la version gratuite, cette option est verrouillée sur **Gras** (thème système par défaut).

Applique un style visuel à toutes les tuiles de boutons. Consultez [Thèmes](../pro/themes.md) pour une description complète et des captures d'écran de chaque option.

| Thème | Style |
|-------|-------|
| Gras | Tuiles colorées pleines avec un fort contraste (par défaut) |
| Phone | Tuiles plates compactes, évoquant un clavier de téléphone |
| Neon | Fond sombre avec des bordures lumineuses de la couleur d'accent |
| Retro | Style monochrome inspiré du terminal avec des lignes de balayage |

---

## Intégration bureau

![Préférences — Intégration bureau](../assets/preferences-desktop.png)


### Toujours au premier plan

Lorsque cette option est activée, la fenêtre Commandeck flotte au-dessus de toutes les autres fenêtres.

- **Windows, macOS et Linux/X11** — fonctionne d'emblée, sans dépendance supplémentaire.
- **Linux/Wayland** — le protocole Wayland n'autorise pas une application à se forcer au premier plan ; l'option est donc désactivée avec une explication. (La plupart des sessions X11, dont celle par défaut de Linux Mint, ne sont pas concernées.)

!!! tip "Garder Commandeck au premier plan sous Wayland"
    Même lorsque l'option de l'application est désactivée, vous pouvez tout de même épingler la fenêtre : **faites un clic droit sur la barre de titre de la fenêtre et choisissez _Toujours au premier plan_**. C'est le gestionnaire de fenêtres de votre bureau qui le fait, et lui en a le droit. Vous pouvez aussi ouvrir une session **X11 / « Xorg »** à l'écran de connexion, où l'option de Commandeck fonctionne normalement.

Ce paramètre est également accessible depuis le menu hamburger comme raccourci.

### Lancer au démarrage de session

Lorsque cette option est activée, Commandeck démarre automatiquement à la connexion à votre bureau. Cela crée un fichier `.desktop` dans `~/.config/autostart/commandeck.desktop`.

La désactivation supprime le fichier de démarrage automatique.

### Terminal

Certains boutons ouvrent une **fenêtre de terminal** pour des outils interactifs (comme `btop` ou `ncdu`). Commandeck détecte votre terminal automatiquement, mais si votre distribution en fournit un inhabituel, vous pouvez le choisir ici.

- **Automatique (détection)** — l'option par défaut ; Commandeck utilise le premier terminal installé qu'il reconnaît, et respecte la variable d'environnement `$TERMINAL` si elle est définie.
- **_(un terminal précis)_** — la liste affiche les terminaux trouvés sur votre système. Vous pouvez aussi saisir la commande de n'importe quel autre terminal.

### Autoriser l'accès MCP

Active le serveur MCP (Model Context Protocol) intégré. Lorsqu'il est actif, un assistant IA compatible (Claude Desktop, Cursor, etc.) peut lire et gérer vos boutons.

Désactivé par défaut. Consultez [Intégration IA (MCP)](../pro/mcp.fr.md) pour les instructions de configuration.

!!! warning
    Lorsque l'accès MCP est activé, votre assistant IA peut créer, modifier et supprimer des boutons. Désactivez cette option lorsque vous ne l'utilisez pas.

---

## Catégories

![Préférences — Catégories](../assets/preferences-categories.png)

Liste toutes les catégories qui existent actuellement dans votre configuration de boutons. Chaque ligne possède une option à bascule :

- **Activée** — la catégorie apparaît dans le menu déroulant de catégories de la barre d'en-tête et ses boutons apparaissent dans la grille
- **Désactivée** — la catégorie et ses boutons sont masqués de la grille (mais pas supprimés)

C'est la façon de restaurer une catégorie après l'avoir masquée avec clic droit → **Masquer la catégorie**.

La liste se met à jour automatiquement lorsque vous ajoutez ou supprimez des catégories.

---

## Profils d'exécution *(Pro)*

Gérez les contextes d'exécution nommés depuis le menu hamburger → **Gérer les profils** (accessible aussi depuis cette section). Chaque profil regroupe :

- **Nom du profil** — un libellé court et descriptif (par ex. `En tant que www-data dans /var/www`)
- **Exécuter en tant que** — l'utilisateur cible : utilisateur courant (sans sudo), root, ou un nom d'utilisateur personnalisé
- **Répertoire de travail** — le répertoire dans lequel effectuer un `cd` avant d'exécuter la commande
- **Mot de passe sudo** — stocké localement avec un encodage propre à la machine ; transmis automatiquement à `sudo -S` à l'exécution, sans invite dans le terminal

Assignez un profil à un bouton dans l'[Éditeur de bouton](button-editor.md#profil-dexécution) pour appliquer ses paramètres.

!!! tip "Fonctionnalité Pro"
    Les profils d'exécution nécessitent [Commandeck Pro](../pro.md).

---

## Licence

![Préférences — Licence](../assets/preferences-license.png)

Gère votre licence Commandeck Pro.

### Activation

1. Achetez une licence sur la [page Commandeck Pro](../pro.md)
2. Collez votre clé de licence dans le champ
3. Cliquez sur **Activer Pro**

Une connexion internet est nécessaire pour l'activation initiale.

### Affichage de la licence active

Lorsqu'une licence valide est active, cette section affiche :

- **Type de licence** — Pro (achat unique)
- **Nombre d'activations** — ex. *1 / 3*
- **Statut** — Active

### Désactivation

Cliquez sur **Désactiver la licence** pour retirer la licence Pro de cet appareil. Les limites de la version gratuite s'appliquent immédiatement.

Rien n'est supprimé. Vos boutons restent — les boutons locaux sont illimités dans la version gratuite. Seules les fonctionnalités Pro se verrouillent jusqu'à la réactivation : les machines SSH cessent de fonctionner (leurs boutons restent mais ne peuvent plus s'exécuter à distance), les thèmes personnalisés reviennent au thème par défaut, et la sauvegarde/restauration ainsi que le serveur MCP deviennent indisponibles.
