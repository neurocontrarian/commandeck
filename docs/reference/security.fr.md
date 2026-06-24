# Sécurité & fonctionnement interne

🔰 **En clair :** Commandeck exécute uniquement les commandes que *vous* écrivez et cliquez, sur vos propres ordinateurs. Il ne conserve jamais vos mots de passe en clair, n'ouvre jamais votre machine au réseau en usage normal, et vous demande de confirmer tout ce que vous avez marqué comme important.

## Pourquoi faire confiance à ce projet ?

- **Il fonctionne sur votre ordinateur, pas dans le cloud.** Aucun compte à créer, aucun serveur d'entreprise qui détient vos informations. Tout ce que Commandeck connaît reste sur votre machine.
- **Achat unique.** Vous payez une seule fois, et la version installée continue de fonctionner. Pas d'abonnement à annuler, pas de serveur qui pourrait s'éteindre discrètement et vous laisser en plan.
- **Aucune télémétrie.** Commandeck n'a ni statistiques ni comptes et n'envoie aucune de vos données vers l'extérieur : ce qui se passe sur votre machine y reste.
- **Disponible en 11 langues**, chacune entretenue comme une vraie partie de l'application, et non bricolée après-coup.

## Vos commandes, visibles et modifiables

La commande de chaque bouton est affichée en clair dans l'[éditeur de bouton](button-editor.fr.md). Rien n'est caché ni déguisé — ce que vous voyez est exactement ce qui s'exécute au clic. Commandeck ne modifie jamais vos commandes à votre insu ; la seule chose qu'il y ajoute, c'est le dossier ou le compte utilisateur que vous choisissez vous-même dans un profil.

## Authentification SSH

Quand vous connectez Commandeck à un autre ordinateur (Pro), vous vous identifiez avec une **clé SSH** (recommandé) ou un **mot de passe**. Dans les deux cas, votre mot de passe n'est jamais écrit sur le disque sous une forme lisible par qui que ce soit.

- Un mot de passe enregistré est conservé dans le coffre sécurisé intégré à votre système — le même que celui où votre système d'exploitation range ses propres mots de passe (Trousseau sur macOS, Gestionnaire d'identifiants sur Windows, GNOME Keyring ou KWallet sur Linux). Il n'est **jamais copié dans une sauvegarde**.
- Sur les rares systèmes dépourvus de ce coffre sécurisé, Commandeck se rabat sur un fichier local brouillé que seul votre compte peut ouvrir, et vous prévient clairement que cette protection est plus faible.
- **La première fois que vous joignez une nouvelle machine,** Commandeck vous montre l'empreinte d'identité de cette machine et vous demande de la confirmer. C'est la même vérification de sécurité que celle de l'outil `ssh` classique — simplement dans une boîte de dialogue conviviale plutôt que dans un terminal.
- Si votre clé SSH est protégée par une phrase secrète, Commandeck vous donne un message clair lorsqu'un déverrouillage est nécessaire, au lieu d'échouer en silence.

## Mots de passe sudo

Certaines commandes ont besoin d'un mot de passe administrateur (sudo) pour s'exécuter. Si vous choisissez d'en enregistrer un dans un [profil](execution-profiles.fr.md), il est traité exactement comme un mot de passe SSH : conservé dans le coffre sécurisé de votre système et **jamais inscrit dans vos fichiers de configuration ni vos sauvegardes** — ceux-ci notent seulement qu'un mot de passe existe, jamais le mot de passe lui-même. Sur un système sans coffre sécurisé, il se rabat sur un fichier brouillé lié à cet ordinateur précis (donc non transférable ailleurs), avec un avertissement clair. Quand une commande en a besoin, Commandeck transmet le mot de passe directement au système, pour vous éviter de le retaper dans un terminal.

## Confirmation par bouton

N'importe quel bouton peut être réglé sur **Demander confirmation avant l'exécution** (éditeur de bouton → Comportement). Activé, Commandeck vous montre la commande exacte et attend votre accord avant d'agir — une bonne idée pour les redémarrages, les suppressions, et tout ce qui demande un mot de passe administrateur.

## Accès IA / MCP (Pro)

Commandeck peut se connecter à un assistant IA pour qu'il vous aide à lire et organiser vos boutons. C'est entièrement facultatif et cela reste **désactivé tant que vous ne l'activez pas**. Plusieurs verrous indépendants vous gardent aux commandes :

- L'assistant ne peut voir ou modifier vos boutons qu'après avoir activé *Autoriser l'accès MCP* dans les Préférences.
- Avant qu'il puisse exécuter un bouton à votre place, **trois** autorisations distinctes doivent toutes être actives : un interrupteur principal, un interrupteur par bouton, et — pour tout ce qui est sensible — une confirmation finale. Si une seule est désactivée, rien ne s'exécute.
- Chaque action de l'assistant est inscrite dans un journal sur votre ordinateur, avec l'heure, le bouton, le résultat et la durée, afin que vous puissiez toujours voir exactement ce qui s'est passé.
- Lancée par un assistant de bureau, la connexion reste entièrement sur votre ordinateur et n'ouvre aucun port réseau. (Un module facultatif, destiné à un outil web particulier, ouvre lui une connexion locale — si vous l'utilisez, gardez-le sur votre réseau domestique, derrière votre pare-feu.)

## Ce contre quoi Commandeck vous protège

Commandeck est un **outil de bureau personnel**. Il part du principe que la personne assise devant l'ordinateur a le droit d'exécuter des commandes sur ses propres machines.

Ses garde-fous servent à éviter les *accidents* et les mauvaises surprises : lancer la mauvaise chose par mégarde, laisser un mot de passe enregistré se glisser dans une sauvegarde ou un dossier synchronisé, ou un assistant IA qui agirait sans votre accord. C'est précisément ce que visent les confirmations, le stockage sécurisé des mots de passe et les verrous de l'IA.

Ce qu'il ne cherche **pas** à faire, c'est protéger votre ordinateur contre quelqu'un qui a déjà pris le contrôle de votre compte ou qui est assis devant votre machine déverrouillée. Aucune application de bureau ne le peut — à ce stade, cette personne pourrait de toute façon lancer ces commandes elle-même. Garder votre ordinateur et votre compte en sécurité (un verrouillage d'écran, un mot de passe de session solide) reste la base sur laquelle Commandeck s'appuie.
