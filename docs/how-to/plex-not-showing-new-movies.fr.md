---
title: Plex n'affiche pas vos nouveaux films ? Faites-le regarder à nouveau
description: Vous avez copié un film dans le dossier et Plex l'ignore. Voici comment lui faire reparcourir vos bibliothèques, depuis un bouton sur votre ordinateur, sans ouvrir de terminal.
---

# Plex n'affiche pas vos nouveaux films ? Faites-le regarder à nouveau

Vous avez copié un film dans votre dossier de films. Vous ouvrez Plex. Il n'y est pas.

Rien n'est cassé. Plex ne connaît que les fichiers qu'il a *regardés*, et il ne surveille pas vos dossiers en permanence — surtout quand le dossier se trouve sur un NAS, un partage réseau ou dans Docker, où le signal qui dit « un nouveau fichier est arrivé » ne lui parvient souvent jamais.

La solution est de lui dire de regarder à nouveau. Sur un serveur, le conseil habituel est de se connecter en SSH et de lancer une commande avec un numéro de bibliothèque qu'il faut d'abord trouver. Voici la version sans rien de tout cela.

---

## La solution en un clic

Commandeck propose un **pack de boutons gratuit pour Plex**. Installez-le une fois et vous obtenez un bouton qui demande à Plex de reparcourir toutes vos bibliothèques — vos films, vos séries, votre musique — en nommant chacune au passage.

1. Ouvrez Commandeck et ajoutez votre serveur comme machine (son adresse, votre nom d'utilisateur, votre mot de passe ou votre clé SSH).
2. Menu **☰ → Packs de boutons → Linux → Plex (Docker)** → *Installer*, et choisissez cette machine. (Plex installé directement sur la machine plutôt que dans un conteneur ? Prenez **Plex (system install)** : mêmes boutons, commandes différentes en dessous.)
3. Cliquez sur **Look for new films and episodes**.

```
Films... looked through.
Séries... looked through.
Musique... looked through.

Plex lit les nouveaux fichiers en arrière-plan ; ils apparaissent au fur et à mesure.
```

Rien à taper, aucun numéro de bibliothèque à chercher. Le nouveau film apparaît dans Plex quelques secondes plus tard — une grosse bibliothèque prend quelques minutes.

---

## S'il n'apparaît toujours pas

Trois raisons expliquent presque tous les cas, et le même pack répond aux trois.

**Le disque est plein.** Plex a besoin de place pour écrire ce qu'il apprend d'un fichier. Quand le disque est à 100 %, une analyse peut se terminer sans rien ajouter — et, au pire, abîmer le catalogue de Plex. Cliquez sur **Space & conversion cache** : il lit tous les dossiers que Plex peut voir et vous prévient en toutes lettres si l'un d'eux est presque plein.

**Plex n'arrive pas à lire le fichier.** Un film copié depuis une autre machine garde souvent les permissions de cette machine. Cliquez sur **What Plex reported** : si Plex n'a pas réussi à ouvrir quelque chose, il le dit là, une seule fois, au lieu d'être noyé dans des milliers de lignes de son propre bavardage.

**Le catalogue lui-même est abîmé.** C'est rare, mais cela explique un Plex qui oublie des films ou perd les marques de visionnage. Cliquez sur **Is the database healthy?** : il vérifie une *copie* de la base de Plex, ne modifie donc rien, et vous dit ce qu'il a trouvé.

---

## Le reste du pack

Le pack est gratuit et compte quinze boutons. Les plus cliqués :

| Bouton | Répond à |
|---|---|
| **Is Plex running?** | Est-il en marche, et s'il s'est arrêté, pourquoi |
| **Why is Plex busy?** | Une vidéo en conversion, une analyse en cours, ou ni l'un ni l'autre |
| **What Plex reported** | Tous les messages écrits par Plex, chacun une fois, avec le nombre de répétitions |
| **Why is the graphics chip not used?** | Les quatre raisons pour lesquelles Plex convertit la vidéo lentement |
| **Restart Plex** | Le premier geste quand quelque chose est bloqué |
| **Clear the conversion cache** | Supprime seulement la vidéo convertie temporaire — jamais vos films |

Chaque commande est visible avant l'installation, et vous pouvez toutes les modifier ensuite.

---

## Agir sur votre serveur passe par SSH

Votre serveur Plex est une autre machine que celle devant laquelle vous êtes assis : ces boutons l'atteignent donc en SSH. Cette partie-là, c'est [Commandeck Pro](../pro.md) — **29 $ une fois, pour de bon, avec un essai de 14 jours qui ne demande ni carte ni compte**. Le pack, lui, est gratuit comme tous les packs.

Rien ne quitte votre ordinateur : pas de compte, pas de nuage, aucun serveur à nous au milieu. Vos machines et vos mots de passe restent sur votre appareil.

---

**À lire aussi :** [Redémarrer Jellyfin ou Plex sans terminal](restart-jellyfin-plex-without-terminal.md) · [Voir l'espace disque de son NAS en un clic](check-disk-space-nas.md) · vous débutez ? Commencez par le [guide du débutant](../use-cases/beginner.md).
