---
description: Transformez les commandes Jellyfin que vous cherchez sans arrêt en boutons - pourquoi ça saccade, ce qui remplit le disque, le journal que le support réclame, redémarrer et mettre à jour - sur Docker ou en installation système.
---

# Garder Jellyfin en forme sans apprendre Docker

Jellyfin est la partie du serveur maison que tout le monde remarque, parce que c'est celle que
la maisonnée utilise. Quand un film saccade, qu'un nouveau dossier n'apparaît pas ou que le
disque se remplit en silence, la réponse trouvée en ligne est toujours une commande — et jamais
deux fois la même.

Commandeck garde ces commandes sous forme de **boutons**. Installez le pack, pointez-le vers
votre serveur, et chaque question devient un appui.

!!! tip "Fonction Pro"
    Parler à votre serveur en SSH demande [Commandeck Pro](../pro.md) — inclus dans l'essai de
    14 jours, sans compte. Les packs, eux, sont gratuits.

---

## D'abord : Docker ou installation système ?

Il y a deux packs Jellyfin, parce qu'il y a deux façons de l'installer. Prenez le mauvais et
tous les boutons répondront « introuvable ».

| Vous avez installé Jellyfin… | Votre pack |
|---|---|
| avec **Docker** ou **docker compose** (une stack Portainer, l'app store d'un NAS) | **Jellyfin (Docker)** |
| depuis les **paquets** de votre distribution (`apt install jellyfin`, un .deb, un script) | **Jellyfin (systemd)** |

Dans le doute, installez celui pour Docker et appuyez sur **Jellyfin tourne-t-il ?**. S'il
répond qu'aucun conteneur de ce nom n'existe, c'est que vous avez l'installation système.

---

## La mise en place

1. **Menu ☰ → Gérer les machines → Ajouter** — un nom, l'IP du serveur, votre utilisateur SSH,
   port 22. Choisissez **Mot de passe** ou **Clé SSH** comme authentification, puis **Tester**.
2. **Menu ☰ → Packs de boutons → Linux → Jellyfin (Docker ou systemd) → Installer**, et
   choisissez cette machine.

C'est toute la mise en place. Rien n'est installé sur le serveur.

---

## Ce que répondent les boutons

| Bouton | Répond à |
|---|---|
| **Jellyfin tourne-t-il ?** | En marche, arrêté, ou qui redémarre en boucle |
| **Pourquoi Jellyfin peine-t-il ?** | Ce qu'il fait en ce moment — en général un transcodage |
| **Ressources en ce moment** | Processeur et mémoire : la machine est-elle la limite ? |
| **Erreurs récentes** | Seulement les lignes d'erreur, extraites d'un long journal |
| **Journal récent complet** | Les 60 dernières lignes brutes, quand les erreurs ne suffisent pas |
| **Suivre le journal en direct** † | Le journal qui s'écrit pendant que vous lancez la lecture |
| **Qui utilise les disques ?** | Quel processus martèle le disque |
| **Espace & cache de transcodage** | Le remplissage du disque, et la place que prend le cache |
| **Accélération matérielle** | Votre carte graphique travaille-t-elle vraiment ? |
| **Extensions installées** | Ce qui est chargé, et ce qui a échoué au chargement |
| **Redémarrer Jellyfin** | La solution à la moitié des problèmes |
| **Mettre à jour Jellyfin** | Récupérer et redémarrer, proprement |
| **Vider le cache de transcodage** | Récupère de la place sans toucher à vos films |
| **Terminal dans le conteneur** † | Docker seulement — pour les réponses qui commencent par « lance ça dans le conteneur » |

† Ouvre un terminal sur votre ordinateur : ces deux-là ne marchent que sur ordinateur.

---

## Les trois soirées où ça sert

### « Ça n'arrête pas de charger »

Appuyez sur **Pourquoi Jellyfin peine-t-il ?**. S'il transcode, le film est converti à la volée
— c'est ce qui chauffe le serveur et vide la mémoire tampon. **Accélération matérielle** vous
dit alors si la carte graphique fait ce travail ou si le processeur s'en charge tout seul,
c'est-à-dire toute la différence entre un film fluide et un film qui saccade.

Pour voir la chose arriver, **Suivre le journal en direct** continue d'écrire pendant que
quelqu'un lance la lecture : le transcodage démarre sous vos yeux.

### « Ça ne démarre pas » / « la bibliothèque est vide »

**Jellyfin tourne-t-il ?** d'abord — un conteneur qui redémarre en boucle ressemble exactement à
un serveur éteint. Puis **Erreurs récentes**, qui extrait les lignes d'erreur d'un journal trop
long à lire. Neuf fois sur dix, **Redémarrer Jellyfin** clôt l'affaire.

### « Le disque est plein »

**Espace & cache de transcodage** montre le remplissage du disque et la part qu'y prennent les
fichiers temporaires de transcodage. **Vider le cache de transcodage** supprime ces fichiers-là
et rien d'autre — jamais vos films, jamais vos réglages. À ne pas appuyer pendant que quelqu'un
regarde.

---

## Depuis le canapé aussi

Les mêmes boutons marchent sur téléphone : Commandeck pour Android est
[en test fermé](../android-beta.md) et lit les mêmes packs, sur votre réseau domestique ou via
votre propre VPN.

---

## À lire ensuite

- [Redémarrer Jellyfin ou Plex sans terminal](../how-to/restart-jellyfin-plex-without-terminal.fr.md)
  — la version à un seul bouton, et l'équivalent pour Plex
- [Packs de boutons](../packs.md) — ce qu'est un pack et comment l'installer
- [Gestion d'un serveur domestique](home-server.fr.md) — la même idée pour le reste du serveur
