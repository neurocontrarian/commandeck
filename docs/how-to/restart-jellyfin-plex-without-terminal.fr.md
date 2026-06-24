# Redémarrer Jellyfin ou Plex sans terminal

Votre serveur multimédia ne répond plus en plein film, ou il ne voit plus les nouveaux fichiers, et la solution habituelle c'est « redémarrer le service ». Sauf que ça veut dire ouvrir un terminal, se souvenir de la commande `systemctl` exacte, et la taper sans faute. Il y a plus simple : transformer cette commande en un bouton sur lequel vous cliquez.

C'est exactement ce que fait Commandeck — une application de bureau pour Windows, Mac et Linux. Vous configurez le bouton une seule fois ; ensuite, redémarrer Jellyfin ou Plex tient en un clic, avec le résultat affiché dans une fenêtre.

![Une grille Commandeck avec les boutons rouges « Redémarrer Jellyfin » et « Redémarrer Plex » à côté de Library Scan, Jellyfin Logs et Espace disque](../assets/howto-restart-media.png)

---

## La commande derrière le bouton

Sur la plupart des serveurs maison, la commande de redémarrage est l'une de celles-ci :

| Serveur | Commande |
|--------|----------|
| **Jellyfin** | `sudo systemctl restart jellyfin` |
| **Plex** | `sudo systemctl restart plexmediaserver` |
| **Jellyfin (Docker)** | `docker restart jellyfin` |
| **Plex (Docker)** | `docker restart plex` |

Si c'est une IA qui a configuré votre serveur, c'est la commande qu'elle vous a donnée. Commandeck, c'est l'endroit où cette commande arrête de dormir dans une vieille conversation et devient un bouton.

---

## Créer le bouton

Clic droit sur la grille → **Nouveau bouton** (ou `Ctrl+N`) et remplissez :

| Champ | Valeur |
|-------|--------|
| Libellé | `Redémarrer Jellyfin` |
| Commande | `sudo systemctl restart jellyfin` |
| Mode d'exécution | `Silencieux` |
| Confirmer avant d'exécuter | **Activé** |
| Couleur | `#e01b24` (rouge — signale « ça redémarre quelque chose ») |
| Info-bulle | `Redémarre le serveur multimédia Jellyfin` |

**Confirmer avant d'exécuter** est le filet de sécurité : une fenêtre « êtes-vous sûr ? » apparaît, vous ne redémarrez donc jamais le serveur par accident pendant que quelqu'un regarde un film.

C'est tout pour un serveur installé **sur ce même ordinateur**. Vous cliquez, vous confirmez, c'est fait.

---

## L'exécuter sur une autre machine (votre NAS ou mini-PC)

La plupart des gens font tourner Jellyfin/Plex sur une machine séparée — un NAS, un Raspberry Pi, un mini-PC — pas sur l'ordinateur portable du quotidien. Commandeck peut atteindre cette machine via SSH et y exécuter le bouton, ce qui vous permet de redémarrer votre serveur multimédia **depuis l'ordinateur où vous êtes vraiment assis**.

Vous ajoutez le serveur une fois (son adresse et votre identifiant), puis vous pointez le bouton dessus. Ensuite, c'est le même clic unique.

!!! tip "Cette partie est Pro"
    Piloter une autre machine via SSH est une fonctionnalité de [Commandeck Pro](../pro.md) — **29 $ une seule fois, à vie, avec un essai gratuit de 14 jours (sans carte)**. La version gratuite exécute les boutons sur votre propre ordinateur. Voir [Machines SSH](../reference/ssh-machines.md) pour la configuration.

---

## Pourquoi c'est mieux qu'un terminal

- **Rien à retenir.** La commande exacte vit dans le bouton, pas dans votre tête ni dans une vieille conversation IA.
- **Aucune faute de frappe sur une commande sensible.** Vous cliquez ; vous ne retapez pas `systemctl` à 23 h.
- **Une confirmation** empêche les redémarrages accidentels.
- **Privé par conception.** Commandeck n'a ni compte, ni cloud, ni télémétrie. La commande va directement de votre ordinateur à votre serveur, nulle part ailleurs.

Une fois le bouton créé, la prochaine fois que Jellyfin fait des siennes, vous réglez ça en un clic — sans terminal, sans rien chercher.

---

**Pour aller plus loin :** vous montez tout un serveur ? Le guide [Gestion d'un serveur domestique](../use-cases/home-server.md) détaille le SSH et une grille complète, étape par étape. Vous débutez sur Commandeck ? Commencez par le [Guide du débutant](../use-cases/beginner.md).
