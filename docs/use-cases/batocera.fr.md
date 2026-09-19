---
description: Transformez les commandes SSH de Batocera en boutons. Pourquoi un jeu ne démarre pas, fermer un émulateur figé, réparer un écran noir et voir ce qui remplit le disque - sans brancher de clavier sur la boîte sous la télé.
---

# Gérer sa Batocera sans clavier

Une machine Batocera vit sous la télé. Elle a une manette, pas de clavier, et aucune fenêtre
pour vous dire ce qui a mal tourné. Alors le jour où un jeu refuse de se lancer, où l'émulateur
se fige ou où l'écran reste noir, la réponse qu'on trouve en ligne est toujours la même :
*« connecte-toi en SSH et lance cette commande. »*

Le conseil est bon. Il tombe juste mal pour une machine qu'on utilise depuis le canapé : il
faut retrouver l'adresse IP, ouvrir un terminal sur un autre ordinateur, et retaper des
commandes cherchées il y a trois mois.

Commandeck garde ces commandes sous forme de **boutons**. Vous les préparez une fois, puis vous
obtenez la réponse en un clic, depuis votre bureau.

!!! tip "Fonction Pro"
    Parler à une autre machine en SSH demande [Commandeck Pro](../pro.md) — inclus dans
    l'essai de 14 jours, sans compte. Batocera, elle, est gratuite et n'a rien à installer.

---

## Ce qu'il vous faut

- Une **Batocera allumée sur votre réseau**, et son **adresse IP** (Batocera l'affiche dans le
  menu principal, sous *Paramètres réseau*).
- SSH est **déjà activé** sur Batocera — rien à installer ni à configurer sur la boîte.
- Commandeck sur votre ordinateur Windows, Mac ou Linux.

Batocera vous connecte en **root** : aucun `sudo`, aucun mot de passe administrateur ici.

---

## Étape 1 — Ajouter la boîte comme machine

**Menu ☰ → Gérer les machines → Ajouter**, puis remplissez :

| Champ | Valeur |
|-------|--------|
| Nom | `Batocera` |
| Hôte | l'IP de votre boîte, par exemple `192.168.1.42` |
| Utilisateur SSH | `root` |
| Port | `22` |
| Authentification | **Mot de passe** |
| Mot de passe SSH | `linux` |

`linux` est le mot de passe d'usine du compte `root` de Batocera — vous l'avez déjà, et il n'y a
rien à configurer sur la boîte. (Si vous l'avez changé dans les réglages de Batocera, mettez le
vôtre.)

Cliquez **Tester**. Le résultat doit être vert, et c'est fini.

!!! note "Où va le mot de passe"
    Commandeck ne l'écrit jamais dans un fichier lisible : il part dans le trousseau de votre
    propre ordinateur — Gestionnaire d'identifiants sous Windows, Trousseau sous macOS, service
    de secrets du système sous Linux. Vous le tapez une fois, ici, et jamais plus.

---

## Étape 2 — Installer le pack Batocera

Plutôt que d'écrire les commandes vous-même, installez l'ensemble tout prêt.

**Menu ☰ → Packs de boutons → Linux → Batocera → Installer**, puis choisissez la machine que
vous venez d'ajouter.

Vous obtenez dix-sept boutons, formulés comme des questions plutôt que comme des commandes :

| Bouton | Répond à |
|--------|----------|
| **Infos système Batocera** | C'est quoi cette boîte, et depuis quand tourne-t-elle ? |
| **Un jeu tourne-t-il en ce moment ?** | Quel jeu, sur quelle console — par son nom, pas un numéro |
| **Débogage (es_launch_stderr.log)** | Pourquoi le dernier jeu a démarré… ou pas |
| **Débogage (es_log.txt)** | Ce que fait l'interface : scraping, thèmes, démarrage lent |
| **Voir un jeu démarrer en direct** † | Le même journal, qui s'écrit pendant que le jeu démarre |
| **Espace libre** | Le disque est plein à combien, et quels dossiers prennent la place |
| **Quelles consoles remplissent mon disque ?** | La taille des ROMs de chaque console, la plus grosse d'abord |
| **Explorer le disque (ncdu)** † | Parcourir /userdata dossier par dossier et supprimer au passage |
| **Mes manettes** | Quelles manettes sont vues, et leur batterie si elles sont sans fil |
| **Déconnecter les manettes sans fil** | Éteint tous les appareils Bluetooth — les manettes ne se vident plus la nuit |
| **Que fait mon écran ?** | La résolution envoyée, et les modes que votre télé accepte |
| **Changer le mode d'affichage** | Force une résolution — le sauvetage de l'écran noir |
| **Fermer le jeu en cours** | Tue un émulateur figé et vous ramène au menu |
| **Redémarrer le menu** | Relance EmulationStation sans redémarrer la machine |
| **Moniteur en direct (htop)** † | Processeur, mémoire et processus pendant qu'un jeu tourne |
| **Redémarrer la machine** / **Éteindre la machine** | Proprement, depuis votre bureau |

† Ouvre un terminal sur votre ordinateur : ces trois-là ne marchent que sur ordinateur.

Tous les packs sont gratuits. Seule la connexion SSH est une fonction Pro.

---

## Les quatre moments où ça sert vraiment

### « Ce jeu ne démarre pas »

Vous appuyez sur A, l'écran clignote, et vous revoilà dans le menu. Batocera a noté ce qui
s'est passé, mais le fichier est sur la boîte.

Cliquez **Débogage (es_launch_stderr.log)**. Le bouton sort d'abord les lignes suspectes du
dernier lancement — un BIOS manquant, un format de ROM non géré, un problème de permission —
et vous dit clairement quand il n'y a rien d'anormal. Puis cliquez **Copier** : c'est
exactement ce que les forums Batocera demandent de coller quand vous posez une question.

Si le problème vient de l'interface et non d'un jeu — un système qui n'apparaît pas, un thème
cassé, un scraping qui bloque — utilisez plutôt **Débogage (es_log.txt)**, le deuxième fichier
que le support réclame.

EmulationStation n'écrit ce deuxième journal que si son niveau de log est monté : s'il est
éteint, le bouton vous dit où l'activer et liste les journaux réellement présents.

### « C'est figé »

La manette ne répond plus et l'émulateur reste à l'écran. **Fermer le jeu en cours** annonce le
jeu qu'il ferme, le tue, puis vérifie que vous êtes bien revenu au menu. Si ça ne suffit pas,
**Redémarrer le menu** reconstruit l'interface sans redémarrage complet.

### « L'écran est noir » ou « l'image est coupée »

**Que fait mon écran ?** affiche la résolution actuellement envoyée et la liste des modes
que votre télé accepte réellement. **Changer le mode d'affichage** en force un : vous tapez le nom du
mode, et si vous vous trompez le bouton refuse de rien changer et vous réaffiche la liste
valide.

### « Les manettes sont encore à plat »

Une manette sans fil oubliée sur le tapis garde sa radio allumée et se vide pendant la nuit.
**Déconnecter les manettes sans fil** coupe toutes les connexions Bluetooth de la boîte, et la
manette s'éteint quelques secondes après. C'est aussi la façon propre de faire lâcher une
manette qu'un jeu figé retient. On la rallume avec son bouton central.

---

### « Je n'ai plus de place »

**Espace libre** montre le remplissage du disque et les plus gros dossiers, en Go ou To lisibles.
**Quelles consoles remplissent mon disque ?** détaille console par console : vous voyez qu'un seul système
prend la moitié du disque avant de commencer à supprimer quoi que ce soit.

---

## Depuis le canapé aussi

Les mêmes boutons existent sur téléphone : Commandeck pour Android est
[en test fermé](../android-beta.md) et lit les mêmes packs. Ça fonctionne sur votre réseau
domestique — ou via votre propre VPN, si vous en avez un. Rien ne passe par un service en
ligne, puisqu'il n'y en a pas.

---

## Bon à savoir sur Batocera

Batocera n'est pas un serveur Linux ordinaire, et ça change les commandes qui ont du sens :

- **Vous êtes root.** Pas de `sudo`, pas de mot de passe administrateur.
- **Le système est en lecture seule hors de `/userdata`.** Ce que vous modifiez ailleurs
  disparaît au redémarrage suivant.
- **Ni `systemctl` ni `journalctl`.** Les journaux sont de simples fichiers : c'est pour ça que
  les deux boutons de débogage lisent des fichiers au lieu d'interroger un service.
- **Les outils plein écran** (`htop`, `ncdu`, un journal en direct) ont besoin d'un vrai
  terminal pour s'afficher. Un bouton peut le leur donner : son mode est **Ouvrir dans un
  terminal**, et Commandeck lance `ssh -t` vers la boîte dans une fenêtre de terminal de votre
  ordinateur. Le pack en contient trois — *Voir un jeu démarrer en direct*,
  *Explorer le disque (ncdu)*, *Moniteur en direct (htop)*.
- Ces trois-là fonctionnent **seulement sur ordinateur** : un téléphone n'a pas de terminal à
  ouvrir, ils n'apparaissent donc pas dans la grille sur Android. Tous les autres boutons du
  pack marchent des deux côtés.
- Tout ce qui pourrait **effacer un disque** est écarté du pack, volontairement.

---

## À lire ensuite

- [Packs de boutons](../packs.md) — ce qu'est un pack et comment l'installer
- [Machines SSH](../reference/ssh-machines.md) — ajouter une machine, ports et dépannage
- [Gérer un parc homelab](homelab.md) — la même idée sur plusieurs machines
- [Démarrage rapide](../quick-start.md) — si c'est votre premier bouton
