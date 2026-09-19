---
title: Gérer son serveur depuis son téléphone
description: Redémarrer un conteneur, vérifier l'espace disque, suivre un journal — depuis votre téléphone, en SSH vers les machines que vous avez déjà. Sans compte, sans cloud. L'application Android est en test fermé et cherche 12 testeurs.
---

# Votre serveur, depuis votre téléphone

Les commandes que vous lancez sur votre serveur — redémarrer un conteneur, vérifier l'espace
disque, suivre un journal, mettre à jour — deviennent des boutons sur votre téléphone, en SSH.
Rien à installer sur le serveur, aucun panneau web à héberger, pas de compte, pas de cloud.

**Elle n'est pas encore sur Google Play, et c'est là que vous intervenez.** Commandeck pour Android est terminé et attend dans la file de test fermé de Google. Google
impose aux nouveaux comptes développeurs un test fermé avec **12 testeurs pendant 14 jours
consécutifs** avant qu'une application puisse être publiée. C'est la seule chose qui sépare
encore l'application mobile de sa sortie.

[S'inscrire (2 minutes)](https://docs.google.com/forms/d/1N3R9aRd24ZAjmTUU1x7dPLEOmA22zCIXcbT9Nda8wfM/viewform){ .md-button .md-button--primary }

## Ce que vous testeriez

Tout ce que fait l'application de bureau en SSH, sur un écran de téléphone : votre grille de
boutons, les packs de boutons gratuits, les machines jointes par clé ou par mot de passe, et
une vue en direct pour les commandes qui continuent d'écrire pendant qu'elles tournent. Les
sauvegardes passent du téléphone à l'ordinateur et inversement. La seule chose qu'elle ne fait
pas, c'est lancer des commandes sur le téléphone lui-même : le téléphone est la télécommande,
pas la machine.

## Ce que nous demandons

- Rester inscrit **les 14 jours entiers**. C'est la règle de Google, et un seul départ anticipé
  remet le compteur à zéro pour tout le monde.
- Ouvrir l'application plusieurs fois par semaine, pas seulement le premier jour.
- Envoyer **au moins un message** sur ce qui a marché ou non. Une ligne suffit.

## Ce que vous y gagnez

Les testeurs gardent l'application **gratuite à vie**. Commandeck pour Android est une
application payante — **19 $ une seule fois**, sans abonnement — et les testeurs qui vont au
bout des deux semaines conservent leur accès gratuit après la sortie.

## Ce qu'il vous faut

- Un **téléphone Android** (pas seulement une tablette, pas un émulateur).
- Une machine que vous pouvez joindre **en SSH** : un NAS, un Raspberry Pi, un serveur privé,
  un hôte Proxmox, une machine Docker — tout ce que vous faites déjà tourner.
- Une **adresse Gmail**, c'est ce que la liste de test de Google utilise.

## Ce qui se passe après votre inscription

Nous lisons chaque inscription et écrivons aux personnes retenues. Ce message contient votre
lien d'inscription au test, la marche à suivre pour installer, et ce que nous aimerions que
vous essayiez en premier. Rien à faire d'ici là, et les 14 jours ne démarrent qu'une fois le
groupe complet. Sans nouvelles de notre part sous une semaine, c'est que le groupe était plein
— nous gardons votre adresse et vous préviendrons à la sortie.

## Ce à quoi l'application se connecte

Autant le dire clairement, puisque vous la pointeriez vers vos propres serveurs.

Commandeck ouvre **deux** connexions sortantes, et uniquement quand vous le demandez : la
galerie de packs télécharge depuis GitHub quand vous ouvrez cet écran, et l'activation de
licence contacte le prestataire de paiement quand vous saisissez une clé. Aucune télémétrie,
aucune statistique, aucun rapport de plantage, aucun compte, et aucun serveur nous appartenant
vers lequel quoi que ce soit pourrait partir. Vos boutons, vos machines et vos identifiants
restent dans le stockage de l'application sur le téléphone, et le SSH va de votre appareil
directement à votre machine.

[S'inscrire (2 minutes)](https://docs.google.com/forms/d/1N3R9aRd24ZAjmTUU1x7dPLEOmA22zCIXcbT9Nda8wfM/viewform){ .md-button }
