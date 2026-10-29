---
title: Vérifiez votre configuration Home Assistant avant de redémarrer
description: Une faute de frappe dans un fichier YAML et Home Assistant ne revient pas après un redémarrage. Voici un bouton de redémarrage qui vérifie d'abord la configuration, et refuse si elle est cassée.
---

# Vérifiez votre configuration Home Assistant avant de redémarrer

Vous avez copié une automatisation trouvée sur un forum dans `configuration.yaml`. Vous redémarrez Home Assistant. Il ne revient pas.

C'est la façon la plus courante de perdre Home Assistant pour la soirée : une indentation de travers, un guillemet oublié, et il refuse de démarrer. Home Assistant a son propre vérificateur de configuration ; tout l'art est de le lancer *à chaque fois*, avant chaque redémarrage, y compris le jour où vous êtes pressé.

Le conseil habituel est de se connecter au serveur en SSH et de lancer le vérificateur à la main dans le conteneur. Voici la version sans rien de tout cela.

---

## La vérification en un clic

Commandeck propose un **pack de boutons gratuit pour Home Assistant**. Installez-le une fois et vous obtenez deux boutons qui se souviennent à votre place.

1. Ouvrez Commandeck et ajoutez votre serveur comme machine (son adresse, votre nom d'utilisateur, votre mot de passe ou votre clé SSH).
2. Menu **☰ → Packs de boutons → Linux → Home Assistant (Docker)** → *Installer*, et choisissez cette machine.
3. Après avoir modifié un fichier, cliquez sur **Ma configuration est-elle valide ?**

Il lance le vérificateur de Home Assistant, affiche son rapport, et termine par un verdict en une ligne :

- **Valide** : redémarrer est sans risque.
- **Problèmes trouvés** : ne redémarrez pas avant de les avoir corrigés ; le rapport au-dessus montre ce qui ne va pas.
- **Il démarrera, mais certaines parties seront ignorées** : redémarrer est sans risque, les parties listées restent éteintes jusqu'à ce que vous les corrigiez.

Ensuite, au lieu de redémarrer depuis la page de Home Assistant, cliquez sur **Redémarrer Home Assistant**. Il vérifie d'abord la configuration et **refuse de redémarrer si elle est cassée**. Si tout va bien, il redémarre Home Assistant et attend que sa page réponde de nouveau.

Rien à taper, aucun nom de conteneur à chercher : le pack trouve Home Assistant par son image, quel que soit le nom que vous lui avez donné.

---

## Il a redémarré, mais quelque chose manque ?

Le même pack répond aux questions qui viennent ensuite.

**Une intégration n'est pas revenue.** Cliquez sur **Qu'est-ce qui n'a pas démarré ?** : il liste les intégrations qui ne se sont pas chargées et signale les intégrations personnalisées, la cause habituelle après une mise à jour.

**La clé Zigbee ou Z-Wave n'est pas trouvée.** Cliquez sur **Ma clé Zigbee ou Z-Wave est-elle détectée ?** Il vérifie les deux bouts — le serveur voit-il la clé, est-elle transmise au conteneur — et affiche la ligne exacte à ajouter si ce n'est pas le cas.

**Quelque chose échoue sans cesse.** Cliquez sur **Erreurs récentes** : tout ce qui a mal tourné depuis le dernier démarrage, chaque message une fois au lieu du même avertissement 300 fois — prêt à coller dans un forum ou votre assistant IA.

---

## Le reste du pack

Le pack est gratuit et compte treize boutons. Les plus utilisés :

| Bouton | Répond à |
|---|---|
| **Home Assistant tourne-t-il ?** | La version qu'il fait tourner, et si Docker a dû le relancer après des plantages |
| **Y a-t-il une version plus récente ?** | Combien de versions mensuelles de retard vous avez, et quelles notes lire avant de sauter |
| **Les sauvegardes ont-elles lieu ?** | La sauvegarde la plus récente et son âge |
| **Mettre à jour Home Assistant** | Refuse de démarrer sans sauvegarde de moins de 24 heures, puis met à jour et attend qu'il réponde |
| **Base de données et espace disque** | La taille atteinte par la base de l'historique, et si le disque est presque plein |

Chaque commande est visible avant l'installation, et vous pouvez toutes les modifier ensuite. Le pack est fait pour **Home Assistant Container**, l'installation Docker. Vous utilisez Home Assistant OS (le Green, le Yellow, une image Raspberry Pi, une machine virtuelle) ? Ce pack n'est pas pour vous : Home Assistant OS n'offre pas de Docker accessible.

---

## Agir sur votre serveur passe par SSH

Votre serveur Home Assistant est une autre machine que l'ordinateur devant vous : ces boutons le joignent donc en SSH. Cette partie, c'est [Commandeck Pro](../pro.md) — **29 $ une fois, pour de bon, avec un essai de 14 jours sans carte ni compte**. Le pack lui-même, comme tous les packs, est gratuit.

Rien ne quitte votre ordinateur : pas de compte, pas de cloud, aucun serveur à nous au milieu. Vos machines et vos mots de passe restent sur votre appareil.

---

**À lire aussi :** [Mettre à jour son serveur sans SSH](update-server-without-ssh.md) · [Commandes Docker en boutons d'un clic](docker-commands-one-click-buttons.md) · vous débutez ? Commencez par le [guide du débutant](../use-cases/beginner.md).
