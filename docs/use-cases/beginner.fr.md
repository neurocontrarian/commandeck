# Cas d'utilisation : Guide pour débutants Linux

Vous venez d'installer Commandeck et vous ne savez pas par où commencer. Ce guide est fait pour vous. Vous n'avez pas besoin de connaître la moindre commande — Commandeck inclut déjà des dizaines de boutons prêts à l'emploi.

---

## Vous avez déjà 29 boutons

Au premier lancement de Commandeck, votre grille est remplie avec trois catégories de boutons préconfigurés :

- **Hardware** (13 boutons) — disque, mémoire, CPU, température, GPU et outils d'espace disque
- **Linux Essentials** (12 boutons) — infos système, utilisateurs, logs, mises à jour et maintenance de base
- **Network** (4 boutons) — interfaces, connexions, ports et services en écoute

Ces boutons sont prêts à l'emploi immédiatement. Aucune configuration nécessaire.

Vous en voulez plus ? Les outils de **développement** (git, Docker, Python, Node) et d'autres ensembles sont disponibles en [packs de boutons](../packs.fr.md) gratuits, installables en un appui. Ouvrez le menu hamburger → **Packs de boutons** pour les parcourir et les installer.

---

## Ce que fait chaque bouton par défaut

### Hardware

| Bouton | Ce qu'il vous montre |
|--------|----------------------|
| **Utilisation disque** | Le remplissage de chaque partition (`df -h`) |
| **Utilisation mémoire** | Utilisation de la RAM et du swap (`free -h`) |
| **Charge CPU** | Charge actuelle et processus les plus gourmands |
| **Température** | Températures CPU/capteurs si `lm-sensors` est installé |
| **Périphériques bloc** | Disques durs, clés USB, partitions (`lsblk`) |
| **Répertoires les plus grands** | Dossiers les plus volumineux sous `/` |
| **NVIDIA GPU** | État du GPU NVIDIA (`nvidia-smi`) |
| **AMD GPU** | Détection du GPU AMD, activité et température |
| **NCDU** | Explorateur d'espace disque interactif (propose d'installer `ncdu` s'il manque) |
| **btop** | Moniteur système en direct (propose d'installer `btop` s'il manque) |
| **NVIDIA Settings** | Ouvre le panneau de configuration NVIDIA |
| **Hardware Info** | Rapport matériel d'un coup — CPU, mémoire, périphériques |
| **Disk I/O** | Statistiques de lecture/écriture disque |

### Linux Essentials

| Bouton | Ce qu'il vous montre |
|--------|----------------------|
| **Processus en cours** | Tous les processus, triés par utilisation CPU |
| **Informations système** | Version du noyau et distribution Linux |
| **Utilisateurs connectés** | Qui est actuellement connecté (`w`) |
| **Dernières connexions** | Historique des connexions |
| **Services en échec** | Services qui ont planté ou n'ont pas démarré |
| **Journal système** | Les 50 dernières lignes du journal système |
| **Messages noyau** | Messages matériels et pilotes |
| **Vider la corbeille** | Vide votre dossier Corbeille |
| **Mise à jour système** | Met à jour votre système (fonctionne sur Ubuntu, Fedora, Arch) |
| **Redémarrer** | Redémarre l'ordinateur |
| **Éteindre** | Éteint l'ordinateur |
| **Tail Syslog** | Les 50 dernières lignes du journal système |

!!! warning
    **Redémarrer** et **Éteindre** ont **Confirmer avant d'exécuter** activé — une boîte de dialogue vous demandera de confirmer avant toute action.

### Network

| Bouton | Ce qu'il affiche |
|--------|------------------|
| **Interfaces réseau** | Vos adresses IP et cartes réseau (`ip addr`) |
| **Connexions actives** | Connexions TCP établies |
| **Ports ouverts** | Services en écoute sur votre machine |
| **Listening Services** | Services à l'écoute sur des ports TCP |

---

## Commencez par cliquer

Cliquez sur **Utilisation disque**. Une petite boîte de dialogue s'ouvre avec les informations de votre système de fichiers. Cliquez sur **Utilisation mémoire**. Essayez-en d'autres.

Vous ne pouvez rien casser en cliquant sur ces boutons — ils ne font que lire des informations. Les deux boutons qui font vraiment quelque chose (Redémarrer et Éteindre) demandent une confirmation en premier.

---

## Désencombrer : désinstaller un pack, ou masquer une catégorie

Les boutons par défaut arrivent sous forme de **packs de boutons**. Si tout un ensemble ne vous sert pas, le plus propre pour désencombrer est de **désinstaller le pack** : ouvrez le menu hamburger → **Packs de boutons**, trouvez-le et cliquez sur **Désinstaller**. Ses boutons disparaissent — et vous pouvez réinstaller le pack à tout moment en un appui.

Si vous préférez simplement mettre une catégorie de côté pour l'instant (sans rien supprimer), vous pouvez la masquer :

1. Ouvrez **Préférences → Catégories**
2. Désactivez la catégorie

Une catégorie masquée et ses boutons disparaissent de la vue mais ne sont pas supprimés — vous pouvez les faire réapparaître à tout moment au même endroit.

---

## Personnaliser le nom ou la couleur d'un bouton

Les noms des boutons par défaut sont fonctionnels mais génériques. Vous pouvez les renommer ou les recolorer selon votre style — c'est **gratuit pour tout le monde**, sans Pro.

Faites un clic droit sur n'importe quel bouton → **Modifier** :

- Changez l'**Étiquette** en quelque chose de plus convivial (`Utilisation disque` → `Mon disque est-il plein ?`)
- Choisissez une **Couleur** pour faire ressortir les boutons importants
- Changez l'**Icône** pour quelque chose qui vous parle davantage

---

## Créer votre premier bouton personnalisé

Les boutons personnalisés sont **gratuits et illimités**. En voici un facile pour commencer :

1. Appuyez sur `Ctrl+N` (ou cliquez sur **+**)
2. **Étiquette :** `Mon adresse IP`
3. **Commande :** `hostname -I`
4. **Mode d'exécution :** `Afficher la sortie`
5. Cliquez sur **Enregistrer**

Vous avez maintenant un moyen en un clic de voir votre adresse IP locale.

---

## Que faire si un bouton affiche une erreur ?

Certains boutons nécessitent des logiciels qui peuvent ne pas être installés :

- **Température** — nécessite `lm-sensors` (`sudo apt install lm-sensors`)
- **NCDU** et **btop** — proposent de s'installer eux-mêmes au premier lancement
- Si vous installez le pack **Développement**, ses boutons Docker/Python/Node nécessitent ces outils installés

Si une commande échoue, une boîte de dialogue de sortie s'ouvre avec l'erreur exacte. Il s'agit généralement d'un paquet manquant — copiez le nom du paquet et installez-le.

---

## Aller plus loin avec Commandeck

Une fois à l'aise avec les boutons par défaut :

- [Créer des boutons personnalisés](../quick-start.md#3-créer-votre-premier-bouton-personnalisé) pour vos propres commandes fréquentes
- [Organiser avec des catégories](../reference/main-window.md#filtre-de-catégories) pour regrouper les boutons liés
- [Ajuster la mise en page de la grille](../reference/preferences.fr.md#disposition-de-la-grille) pour s'adapter à votre écran
- Envisager [Commandeck Pro](../pro.md) lorsque vous souhaitez gérer un serveur distant
