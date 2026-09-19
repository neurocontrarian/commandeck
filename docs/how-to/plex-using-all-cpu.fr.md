---
title: Plex consomme tout votre processeur ? Voici pourquoi
description: Le serveur chauffe et le film saccade. Plex reconstruit la vidéo au lieu de l'envoyer telle quelle. Découvrez en un clic pourquoi, et quoi changer — sans terminal.
---

# Plex consomme tout votre processeur ? Voici pourquoi

Le film saccade. Le ventilateur s'emballe. Le serveur, silencieux toute la semaine, est soudain à 100 %.

Presque toujours, c'est la même chose : **Plex reconstruit la vidéo, image par image, au lieu d'envoyer le fichier tel quel.** Plex appelle ça la conversion. Elle se déclenche quand l'appareil sur lequel vous regardez ne sait pas lire le fichier d'origine — mauvais format, image trop grande, ou un sous-titre à incruster.

Votre serveur peut faire ce travail de deux façons. La puce graphique s'en charge sans même chauffer. Le processeur, lui, monte à 100 % et peine. La plupart des serveurs domestiques sont sur la voie lente sans que leur propriétaire l'ait jamais su.

---

## Le savoir en un clic

Commandeck propose un **pack de boutons gratuit pour Plex** — un pour Plex dans Docker, un pour Plex installé sur la machine elle-même. Installez-le, pointez-le sur votre serveur, et deux boutons répondent.

**1. « Why is Plex busy? »** — dit si une conversion est en cours, sur quel fichier, et ce qu'elle coûte :

```
=== Converting a video right now? ===
Yes - Plex is converting a video right now.
  File: Sintel
  CPU:  98.0% for that one process
```

**2. « Why is the graphics chip not used? »** — vérifie une par une les quatre raisons pour lesquelles Plex retombe silencieusement sur le processeur :

```
=== 1. Is there a graphics chip to use? ===
No /dev/dri/renderD* on this machine.

=== 2. Is Plex allowed to open it? ===
The device belongs to group: render
The plex user is NOT in that group. Fix it with: sudo usermod -aG render plex

=== 3. Is the setting ticked? ===
Plex has never been given the setting.
Settings > Transcoder > Use hardware acceleration when available.

=== 4. What the log says the last time it converted ===
Nothing about hardware in the recent log.
```

Il rappelle aussi ce qu'aucune commande ne peut vérifier : la conversion matérielle exige un **Plex Pass** actif. Sans lui, Plex utilise le processeur et ne le dit jamais.

---

## Les quatre causes, et quoi faire pour chacune

**La puce n'est pas là, ou pas partagée.** Sur un mini-PC ou un NAS, elle est là : presque tous les processeurs Intel des dix dernières années en ont une. Si votre Plex tourne dans un conteneur Docker, il faut lui confier l'appareil : ajoutez `devices: - /dev/dri:/dev/dri` à votre fichier compose, ou cochez l'équivalent dans votre gestionnaire de conteneurs. Si Plex tourne dans un conteneur Proxmox, l'appareil doit être transmis depuis l'hôte.

**Plex n'a pas le droit de l'ouvrir.** La puce appartient à un groupe, en général `render` ou `video`, et le compte sous lequel tourne Plex doit en faire partie. Le bouton affiche la commande exacte pour votre machine.

**Le réglage est désactivé.** Plex ne l'active pas tout seul : *Paramètres → Transcodeur → Utiliser l'accélération matérielle lorsqu'elle est disponible*.

**Pas de Plex Pass.** La conversion matérielle est une fonction payante. Celle-là n'est pas un défaut, et aucune commande ne la contourne.

---

## Parfois la solution, c'est de ne pas convertir du tout

La conversion la plus rapide est celle qui n'a pas lieu. Deux choses à essayer avant d'acheter quoi que ce soit :

- **Baisser la qualité sur l'appareil qui regarde.** Si le lecteur demande « Original », Plex envoie le fichier intact et ne fait rien du tout.
- **Regarder ce qui est converti.** Si le bouton dit que l'image est « copiée telle quelle » et que seul le son change, votre serveur travaille à peine — c'est le bon cas, il n'y a rien à corriger.

Et un piège à connaître : un disque presque plein ralentit tout, conversions comprises. Le bouton **Space & conversion cache** du pack vous prévient en toutes lettres quand l'un de vos disques arrive à saturation.

---

## Obtenir les boutons

Menu **☰ → Packs de boutons → Linux → Plex (Docker)** ou **Plex (system install)** — gratuit, comme tous les packs. Choisissez celui qui correspond à la façon dont Plex est installé sur votre serveur : les deux utilisent des commandes complètement différentes.

Atteindre votre serveur en SSH, c'est [Commandeck Pro](../pro.md) — **29 $ une fois, pour de bon, essai de 14 jours sans carte ni compte**. Rien ne quitte votre ordinateur : pas de compte, pas de nuage, aucun serveur à nous au milieu.

---

**À lire aussi :** [Plex n'affiche pas vos nouveaux films ?](plex-not-showing-new-movies.md) · [Voir l'espace disque de son NAS en un clic](check-disk-space-nas.md) · vous débutez ? Commencez par le [guide du débutant](../use-cases/beginner.md).
