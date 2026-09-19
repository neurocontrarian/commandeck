# Des commandes Docker en boutons d'un clic

Si votre serveur maison fait tourner des applis dans Docker — Jellyfin, Immich, Pi-hole, Nextcloud, la stack *arr — vous vivez avec une poignée de commandes `docker` que vous retapez sans cesse : lister ce qui tourne, redémarrer un conteneur, voir les logs, mettre à jour la stack. Ce n'est pas compliqué, mais c'est facile à rater et pénible à retaper en boucle.

Commandeck transforme chacune en bouton. Vous cliquez, la commande s'exécute (sur cet ordinateur ou sur votre serveur via SSH), et le résultat apparaît dans une fenêtre.

![Une catégorie « Docker » dans Commandeck : Ce qui tourne, Redémarrer un conteneur, Voir les logs, Stats en direct, Mettre à jour la stack et Libérer l'espace](../assets/howto-docker.png)

---

## Les commandes Docker à transformer en boutons

| Tâche | Commande | Mode suggéré |
|-------|----------|--------------|
| Voir ce qui tourne | `docker ps` | Afficher la sortie |
| Tout voir (même arrêté) | `docker ps -a` | Afficher la sortie |
| Redémarrer un conteneur | `docker restart jellyfin` | Silencieux + Confirmer |
| Voir les logs d'un conteneur | `docker logs --tail 100 jellyfin` | Afficher la sortie |
| Usage des ressources en direct | `docker stats --no-stream` | Afficher la sortie |
| Mettre à jour une stack compose | `docker compose pull && docker compose up -d` | Afficher la sortie + Confirmer |
| Libérer de l'espace disque | `docker system prune -f` | Afficher la sortie + Confirmer |
| Espace disque utilisé par Docker | `docker system df` | Afficher la sortie |

Le bouton « mettre à jour la stack » est celui qu'on préfère : il récupère les images les plus récentes et redémarre tout, en un clic au lieu de deux commandes tapées dans le bon ordre.

---

## Créer une catégorie « Docker »

Créez les boutons ci-dessus et réglez la **Catégorie** de chacun sur `Docker`. Ils se regrouperont sous une seule entrée dans le menu des catégories, ainsi tous vos contrôles de conteneurs sont rangés au même endroit.

Pour les commandes d'exemple, remplacez `jellyfin` par le nom de votre conteneur (`docker ps` vous montre les noms).

!!! tip "Un seul bouton pour n'importe quel conteneur"
    Avec une [variable de commande](../reference/command-variables.md), un unique bouton **Redémarrer un conteneur** peut demander *lequel* à chaque fois — tapez ou choisissez le nom, et il exécute `docker restart {{container}}`. Un bouton les couvre tous.

---

## Les exécuter sur votre serveur, pas seulement en local

Docker tourne généralement sur votre serveur — le NAS ou le mini-PC — pas sur votre portable. Pointez les boutons vers cette machine et ils s'exécutent via SSH, vous gérez donc vos conteneurs depuis le bureau où vous êtes assis.

!!! tip "Distant = Pro"
    Exécuter des boutons sur une autre machine via SSH, c'est [Commandeck Pro](../pro.md) — **29 $ une seule fois, à vie, essai gratuit de 14 jours (sans carte)**. Les boutons qui lancent Docker sur *cet* ordinateur fonctionnent dans la version gratuite.

---

## Pourquoi le bouton bat le retapage

- **La bonne commande, dans le bon ordre, à chaque fois** — surtout le « mettre à jour la stack » en deux temps.
- **Aucun nom de conteneur ni option à mémoriser** — ils sont intégrés au bouton.
- **Une confirmation** sur les commandes destructrices (`prune`, redémarrages) pour que rien n'arrive par accident.
- **Privé** — ni compte, ni cloud, ni télémétrie ; la commande va directement sur votre machine.

Construisez la catégorie une fois, et toute votre installation Docker devient un panneau de boutons que n'importe qui à la maison pourrait utiliser.

---

**Pour aller plus loin :** voir le guide [Gestion d'un serveur domestique](../use-cases/home-server.md) pour l'installation complète, ou le guide [Flux de développement](../use-cases/dev-workflow.md) si ce sont des conteneurs de dev.
