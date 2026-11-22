---
title: Immich ne reconnaît plus les visages ? Trouvez pourquoi en un clic
description: Les visages ne sont pas regroupés, la recherche ne trouve rien. Voici comment vérifier les trois causes habituelles depuis un bouton sur votre ordinateur, sans ouvrir de terminal sur votre serveur.
---

# Immich ne reconnaît plus les visages ? Trouvez pourquoi en un clic

Vous avez envoyé quelques centaines de photos. Des jours plus tard, les visages ne sont toujours pas regroupés, et chercher « plage » ne donne rien.

Rien n'est perdu. Vos photos sont en sécurité : ce qui s'est arrêté, c'est la partie d'Immich qui les *regarde*. Immich, ce sont quatre programmes qui travaillent ensemble, et les visages comme la recherche intelligente viennent de l'un d'eux : la partie d'apprentissage automatique. Quand elle s'arrête, ou que l'application ne la joint plus, Immich continue de fonctionner… il ne reconnaît simplement plus rien.

Le conseil habituel est de se connecter au serveur en SSH, de lister les conteneurs et de lire leurs journaux. Voici la version sans rien de tout cela.

---

## La vérification en un clic

Commandeck propose un **pack de boutons gratuit pour Immich**. Installez-le une fois et vous obtenez un bouton qui vérifie les trois causes habituelles, l'une après l'autre, et vous dit laquelle c'est.

1. Ouvrez Commandeck et ajoutez votre serveur comme machine (son adresse, votre nom d'utilisateur, votre mot de passe ou votre clé SSH).
2. Menu **☰ → Packs de boutons → Linux → Immich (Docker)** → *Installer*, et choisissez cette machine.
3. Cliquez sur **Pourquoi les visages ou la recherche ne fonctionnent-ils pas ?**

Il vérifie, en clair :

- **La partie visages et recherche tourne-t-elle ?** Si elle est arrêtée, c'est la cause, et il le dit.
- **L'application la joint-elle ?** Les deux peuvent tourner sans se parler. Si c'est le cas, il vous indique où régler la bonne adresse dans les paramètres d'Immich.
- **Qu'a-t-elle signalé ces dernières 24 heures ?** Ses erreurs et avertissements récents, y compris ceux qui veulent dire qu'elle a manqué de mémoire.

Rien à taper, aucun nom de conteneur à chercher : le pack trouve les conteneurs d'Immich par leur image, quel que soit le nom que vous leur avez donné.

---

## Les visages vont bien, mais autre chose cloche ?

Le même pack répond aux autres questions pour lesquelles on se connecte en SSH.

**Le disque se remplit.** Immich garde plus que vos photos : des aperçus, des copies converties de vos vidéos, des sauvegardes de sa base. Cliquez sur **Où est passé l'espace disque ?** : il mesure chacun, dit ce que c'est, et vous prévient quand un disque est presque plein.

**Mes sauvegardes ont-elles vraiment lieu ?** Immich peut copier sa base chaque nuit — si le réglage est activé et que rien n'a cassé. Cliquez sur **Les sauvegardes ont-elles lieu ?** : il trouve la copie la plus récente et vous dit son âge, au lieu de vous laisser supposer.

**Faut-il mettre à jour ?** Cliquez sur **Y a-t-il une version plus récente ?** : il compare votre version à la plus récente et vous prévient quand le saut est important, du genre où l'application du téléphone doit suivre. **Mettre à jour Immich** refuse de démarrer sans copie de la base de moins de 24 heures, parce qu'une mise à jour ne se défait pas.

---

## Le reste du pack

Le pack est gratuit et compte treize boutons. Les plus utilisés :

| Bouton | Répond à |
|---|---|
| **Immich tourne-t-il ?** | Chacune de ses quatre parties, à quoi elle sert, et pourquoi l'une s'est arrêtée |
| **Erreurs récentes** | Ce qui a mal tourné ces dernières 24 heures, chaque message une fois — prêt à coller dans un forum ou votre assistant IA |
| **Redémarrer Immich** | Le premier geste quand il bloque : redémarre toutes les parties et attend que l'application soit prête |
| **Ressources en ce moment** | Pourquoi le serveur est occupé — en général la reconnaissance des visages après un gros envoi |
| **Lister les utilisateurs** | Chaque compte, avec son adresse e-mail et s'il est administrateur |

Chaque commande est visible avant l'installation, et vous pouvez toutes les modifier ensuite. Le pack est fait pour **Immich installé avec Docker** (compose ou Portainer). Installé comme modèle Unraid, application TrueNAS ou snap ? Certains boutons ne le trouveront pas.

---

## Agir sur votre serveur passe par SSH

Votre serveur Immich est une autre machine que l'ordinateur devant vous : ces boutons le joignent donc en SSH. Cette partie, c'est [Commandeck Pro](../pro.md) — **29 $ une fois, pour de bon, avec un essai de 14 jours sans carte ni compte**. Le pack lui-même, comme tous les packs, est gratuit.

Rien ne quitte votre ordinateur : pas de compte, pas de cloud, aucun serveur à nous au milieu. Vos machines et vos mots de passe restent sur votre appareil.

---

**À lire aussi :** [Voir l'espace disque de son NAS en un clic](check-disk-space-nas.md) · [Mettre à jour son serveur sans SSH](update-server-without-ssh.md) · vous débutez ? Commencez par le [guide du débutant](../use-cases/beginner.md).
