# Voir l'espace disque de son NAS en un clic

Un disque plein, c'est ce qui casse un serveur maison en silence : les téléchargements s'arrêtent, les sauvegardes échouent, le serveur multimédia n'ajoute plus de fichiers, les bases de données se corrompent. La solution, c'est de vérifier l'espace disque *avant* qu'il ne se remplisse — mais qui a envie de se connecter en SSH au NAS et de taper `df -h` chaque semaine ?

Commandeck en fait un bouton. Un clic, et vous voyez exactement à quel point chaque disque est plein, dans une fenêtre sur votre bureau.

![La fenêtre de sortie de Commandeck montrant le résultat de df -h, avec un disque rempli à 94 %](../assets/howto-disk-output.png)

---

## Le bouton

Clic droit sur la grille → **Nouveau bouton** et remplissez :

| Champ | Valeur |
|-------|--------|
| Libellé | `Espace disque` |
| Commande | `df -h` |
| Mode d'exécution | `Afficher la sortie` |
| Icône | `drive-harddisk-symbolic` |
| Info-bulle | `À quel point chaque disque est plein` |

Cliquez et vous obtenez un tableau clair : chaque disque, sa taille, l'espace utilisé et le pourcentage de remplissage. Les chiffres qui comptent sont la colonne **Util%** — tout ce qui approche 90 % mérite votre attention.

---

## D'autres boutons disque utiles

| Libellé | Commande | Ce que ça montre |
|---------|----------|------------------|
| `Plus gros dossiers` | `du -h -d 1 / \| sort -hr \| head -20` | Ce qui mange l'espace |
| `Plus gros dossiers (perso)` | `du -h -d 1 ~ \| sort -hr \| head -20` | Pareil, dans votre dossier personnel |
| `Espace Docker` | `docker system df` | Combien Docker utilise |
| `Libérer l'espace Docker` | `docker system prune -f` | Récupère les images/couches inutilisées |

Le bouton **Plus gros dossiers** est la suite logique : quand `Espace disque` montre qu'un disque est presque plein, celui-ci vous dit *quoi* nettoyer.

---

## Vérifier un NAS ou un serveur (pas seulement ce PC)

Votre NAS est une machine séparée, le vrai gain c'est donc d'exécuter ces boutons **sur le NAS via SSH** pendant que vous êtes à votre bureau Windows ou Mac. Ajoutez le NAS une fois, pointez les boutons dessus, et « vérifier le disque du NAS » devient un clic unique depuis l'autre bout de la maison.

!!! tip "Les vérifications à distance sont Pro"
    Atteindre une autre machine via SSH, c'est [Commandeck Pro](../pro.md) — **29 $ une seule fois, à vie, essai gratuit de 14 jours (sans carte)**. Vérifier le disque de *cet* ordinateur fonctionne gratuitement.

---

## En faire une habitude

L'espace disque, c'est le genre de chose à laquelle on ne pense qu'une fois qu'il est trop tard. Avec un bouton posé dans votre grille, y jeter un œil prend deux secondes — alors vous le faites vraiment, et vous repérez un disque qui se remplit avant qu'il ne fasse tomber le serveur.

- **Pas de terminal, pas de `df -h` à retenir** — c'est un bouton.
- **En lecture seule et sans danger** — ces boutons ne font que *regarder* ; ils ne changent rien.
- **Privé** — ni compte, ni cloud, ni télémétrie.

---

**Pour aller plus loin :** le guide [Gestion d'un serveur domestique](../use-cases/home-server.md) met en place les boutons disque, mise à jour et redémarrage ensemble. Vous débutez ? Voir le [Guide du débutant](../use-cases/beginner.md).
