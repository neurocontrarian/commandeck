---
description: Questions fréquentes sur Commandeck — tarifs, confidentialité, sécurité de l'IA, plateformes, et la différence avec les alias, scripts et panneaux web.
---

# Questions fréquentes

## Commandeck est-il gratuit ?

La version gratuite est **gratuite** : commandes et boutons locaux illimités,
sans compte, sans expiration. **Pro** est un **achat unique de 29 $** (pas d'abonnement —
payez une fois, c'est à vous pour toujours) qui ajoute les machines SSH, les boutons multi-machines, les
thèmes, la sauvegarde/restauration, l'édition des boutons par défaut et le serveur MCP.
Chaque version Pro inclut un **essai automatique de 14 jours** — sans carte, sans email.
Voir [Pro & tarifs](pro.fr.md).

## Pourquoi pas de simples alias shell ou un script ?

Si vous vivez dans le terminal et que vos alias vous suffisent, vous n'avez peut-être pas
besoin de Commandeck. Il brille dans deux cas : les commandes que vous n'exécutez *pas*
assez souvent pour les retenir (la maintenance mensuelle, ou cette commande qu'une IA vous
a donnée il y a trois semaines), et les personnes qui veulent un bouton, pas une invite.
Les boutons sont visibles et organisés, le résultat s'ouvre dans une fenêtre, la cible SSH
se choisit au clic, et les commandes risquées affichent une confirmation — tout ce que
`history | grep` ne fait pas.

## Quelle différence avec un panneau web auto-hébergé ?

Certains outils résolvent un problème proche sous forme de **service web installé sur un
serveur** (un conteneur à lancer, un fichier YAML à configurer, un port à exposer, un
navigateur pour y accéder). Commandeck prend la forme inverse : une **appli de bureau sur
votre propre machine**. Rien à héberger, aucun port ouvert, aucun fichier de config — les
boutons s'éditent dans l'interface et sont stockés en TOML lisible sur votre disque. Le
compromis est assumé : Commandeck est mono-utilisateur par conception. Si plusieurs
personnes doivent partager un panneau sur le réseau, un outil web convient mieux ; si vous
voulez ça sur votre propre ordinateur — y compris Windows et macOS — Commandeck est fait
exactement pour ça.

## Est-ce que ça téléphone à la maison ? Télémétrie ? Compte ?

Aucune télémétrie, aucun compte, aucun cloud, aucun service à l'écoute. Boutons et
machines sont des fichiers TOML en clair sur votre disque ; vos clés SSH restent où elles
sont (Commandeck stocke le *chemin*, jamais la clé). Le seul trafic réseau, ce sont les
connexions SSH que *vous* configurez. Voir [Sécurité](reference/security.md).

## Laisser une IA exécuter des commandes, ce n'est pas dangereux ?

Ça le serait si c'était activé par défaut — ce n'est pas le cas. L'exécution par l'IA est
derrière **trois consentements distincts** : un réglage global (désactivé par défaut), un
drapeau par bouton « l'IA peut exécuter ceci », et, pour les boutons avec confirmation, un
aller-retour de confirmation explicite. Les boutons en mode terminal ne sont jamais
exécutables par l'IA, et chaque exécution est inscrite dans un journal d'audit. Le serveur
MCP est purement local (stdio) — rien n'est exposé sur le réseau. Détails dans
[Intégration IA (MCP)](pro/mcp.fr.md).

## C'est de l'Electron ? C'est lourd ?

Non — Commandeck c'est Python + Qt (PySide6) avec des widgets natifs, pas un navigateur
embarqué. Linux est distribué en AppImage, macOS en .dmg, Windows avec un installateur.
Le SSH passe par Paramiko : aucune dépendance à l'OpenSSH du système.

## Ça fonctionne sous Wayland ?

Oui. Quelques raffinements de gestion de fenêtres sont honnêtement limités : « toujours
au premier plan » fonctionne sous X11 et est désactivé-avec-explication sous Wayland,
car c'est le compositeur qui décide.

## L'appli Android arrive quand ? Et iOS ?

Une appli Android native (une vraie appli avec SSH et thèmes — pas une page web emballée)
est en test fermé, en route vers le Play Store. iOS suivra Android (même base de code),
sans date pour l'instant.

## Que se passe-t-il si le projet s'arrête ?

Votre appli continue de fonctionner. Pro est un achat unique avec une licence pensée pour
le hors-ligne — pas d'abonnement qui expire, pas de serveur dont vos boutons dépendent.
Votre config est du TOML en clair sur votre disque — rien n'est verrouillé à un serveur ni à un compte.

## Où est stockée ma configuration ?

| Plateforme | Emplacement |
|------------|-------------|
| Linux | `~/.config/commandeck/` |
| macOS | `~/Library/Application Support/Commandeck/` |
| Windows | `%APPDATA%\Commandeck\` |

`buttons.toml` est lisible par un humain — vous pouvez le consulter, le sauvegarder ou le
versionner comme vous voulez. Pro ajoute la [sauvegarde/restauration](pro/backup.fr.md)
en un clic.

## Je peux l'utiliser sans aucun serveur ?

Absolument — la version gratuite, c'est exactement ça : un lanceur local pour les
commandes de votre propre machine. Le SSH n'entre en jeu que si vous ajoutez des machines
distantes (Pro).

## J'ai trouvé un bug / j'ai une idée. Où aller ?

[GitHub Issues](https://github.com/neurocontrarian/commandeck/issues) pour les bugs,
[Discussions](https://github.com/neurocontrarian/commandeck/discussions) pour les idées
et le partage de boutons utiles. Commandeck est développé par une seule personne — les
signalements sont lus.
