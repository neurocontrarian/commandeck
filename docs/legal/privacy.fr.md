---
description: Politique de confidentialité de Commandeck — sans compte, sans télémétrie, sans cloud. Votre configuration reste sur votre appareil. Couvre desktop (Linux/macOS/Windows) et Android.
---

# Politique de confidentialité

*Dernière mise à jour : septembre 2026*

Commandeck est un lanceur de commandes disponible sur **Linux, macOS, Windows et Android**. Cette
politique explique quelles données sont — et ne sont pas — concernées lorsque vous l'utilisez. En
résumé : **Commandeck n'a aucun compte utilisateur, n'exploite aucun serveur collectant des
données, et votre configuration reste sur votre propre appareil.**

## En résumé

- Aucun compte, aucune inscription.
- **Les applications** ne contiennent aucune donnée analytique, aucune télémétrie et aucun suivi
  d'utilisation — elles ne nous rapportent jamais ce que vous faites.
- **Ce site web** ne contient aucun script de mesure. Seul un clic sur un bouton de téléchargement
  est compté, sans cookie et sans rien qui vous identifie — voir *Ce site web* ci-dessous.
- Vos boutons, vos définitions de machines SSH et vos profils d'exécution restent **sur votre
  appareil** — ils ne nous sont jamais transmis.
- Nous n'avons jamais accès à vos clés SSH, à vos identifiants, ni aux commandes que vous exécutez.
- Les achats sont gérés par un prestataire tiers (LemonSqueezy sur desktop, Google Play sur
  Android) — pas par nous.

## Fournisseur

Commandeck est exploité par **neurocontrarian**, situé au Québec, Canada.
**Contact pour toute question relative à la confidentialité :**
[neurocontrarian@gmail.com](mailto:neurocontrarian@gmail.com)

## Achats

### Desktop (Linux, macOS, Windows)

La licence Pro est vendue via [LemonSqueezy](https://www.lemonsqueezy.com), agissant en tant que
Merchant of Record — responsable des données de paiement, qui reçoit votre e-mail et vos
informations de paiement. Nous ne recevons que votre adresse e-mail (pour la validation de
licence) et des rapports de ventes agrégés ; nous ne voyons jamais vos coordonnées bancaires.

Lors de l'activation d'une licence Pro, les éléments suivants sont transmis à l'API de LemonSqueezy
pour la valider et gérer vos emplacements d'activation (max 3 appareils) :

- votre clé de licence,
- un identifiant d'appareil anonyme et haché (dérivé de l'identifiant machine — non lié à votre
  identité), utilisé comme nom de l'activation pour que la licence reste liée à cet appareil.

L'adresse e-mail d'achat que vous saisissez est comparée sur votre appareil à celle que renvoie
LemonSqueezy ; elle n'est pas transmise. Ensuite, au plus une fois tous les 30 jours environ et
uniquement au démarrage de l'application, la clé de licence et l'identifiant de l'activation sont
transmis pour confirmer que la licence est toujours valide. Rien d'autre n'est transmis, et
l'application fonctionne entièrement hors ligne entre les vérifications — une vérification qui ne
peut pas se connecter est simplement ignorée.

### Android (Google Play)

Sur Android, l'application payante (un achat unique) est vendue et traitée par **Google Play**. Google est le
prestataire de paiement, et votre achat est régi par la politique de confidentialité de Google et
les conditions de Google Play. L'application Android n'a **aucun serveur de licence distinct,
aucun compte, et ne transmet aucune donnée personnelle** — l'état de votre achat est fourni
par Google Play sur votre appareil.

## Stocké localement sur votre appareil

Commandeck stocke votre configuration **localement** — sur desktop dans `~/.config/commandeck/`
(et l'équivalent sur macOS/Windows), et sur Android dans le stockage privé de l'application :

- votre configuration de boutons,
- vos définitions de machines SSH (hôte / utilisateur / port — **les clés privées n'y sont jamais
  stockées ni transmises**),
- vos profils d'exécution (les mots de passe sudo sont encodés avec une clé propre à l'appareil et
  ne sont jamais transmis).

Aucun de ces fichiers ne quitte votre appareil.

## Ce site web (commandeck.app)

Le site web — les pages que vous lisez en ce moment — ne contient **aucun script de mesure** :
ni Umami, ni Google Analytics, rien qui se charge dans votre navigateur pour observer ce que vous
faites.

Une seule chose est comptée. Un **bouton de téléchargement** vous fait passer par
`commandeck.app/get/…`, qui note quatre éléments avant de vous rediriger vers le fichier :

- quel fichier a été demandé et s'il s'agit de l'édition gratuite ou Pro,
- votre pays,
- la page ou le message d'où venait le lien, lorsque le lien le précise (par exemple un lien que
  nous avons publié dans un forum).

C'est tout. **Aucun cookie n'est déposé, aucune adresse IP n'est conservée, aucune empreinte de
navigateur, aucun identifiant** — rien qui puisse remonter jusqu'à vous, et rien du tout n'est
conservé sur les personnes qui se contentent de lire les pages. Le but est de savoir si le site
fait son travail : nous comptons le clic, pas la personne.

Rien de tout cela n'atteint l'application que vous installez. Utiliser Commandeck n'est pas suivi.

## Ce que nous ne collectons pas

- Aucune donnée analytique ou d'utilisation **dans les applications** ; nous ne suivons pas les
  commandes que vous exécutez.
- Aucun accès à vos identifiants SSH ni à vos clés privées.
- Aucun cookie, ni sur le site web ni dans les applications.
- Aucune publicité, aucun identifiant publicitaire, et aucun suivi de vous sur d'autres sites.
- Les applications ne contiennent **aucun SDK publicitaire ou analytique tiers**.

## Services tiers

- [LemonSqueezy](https://www.lemonsqueezy.com) — licence et paiement sur desktop ; leur politique
  de confidentialité s'applique aux données qu'ils traitent.
- **Google Play** — achat de l'application payante sur Android ; la politique de confidentialité de Google
  s'applique.
- [Cloudflare](https://www.cloudflare.com) — héberge ce site web et traite les liens de téléchargement ; comme tout hébergeur, il traite le trafic nécessaire à l'affichage des pages.

## Conservation des données

Nous ne stockons aucune donnée personnelle sur nos serveurs. Votre configuration reste sur votre
appareil.

## Vos droits

Vous pouvez nous contacter pour toute demande relative à la protection des données. Sur desktop, la
désactivation de votre licence supprime l'enregistrement d'activation d'appareil des serveurs de
LemonSqueezy. Sur Android, votre achat se gère depuis votre compte Google Play.

## Modifications de cette politique

Nous nous réservons le droit de mettre à jour cette politique à tout moment, à notre seule
discrétion. Les modifications prennent effet dès leur publication sur cette page. La date
« Dernière mise à jour » ci-dessus reflète la révision la plus récente. Nous vous encourageons à
consulter cette page régulièrement.

## Contact

Pour toute question ou pour exercer vos droits de protection des données :
[neurocontrarian@gmail.com](mailto:neurocontrarian@gmail.com)
