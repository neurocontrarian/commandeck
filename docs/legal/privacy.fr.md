---
description: Politique de confidentialité de Commandeck — sans compte, sans télémétrie, sans cloud. Votre configuration reste sur votre appareil. Couvre desktop (Linux/macOS/Windows) et Android.
---

# Politique de confidentialité

*Dernière mise à jour : juin 2026*

Commandeck est un lanceur de commandes disponible sur **Linux, macOS, Windows et Android**. Cette
politique explique quelles données sont — et ne sont pas — concernées lorsque vous l'utilisez. En
résumé : **Commandeck n'a aucun compte utilisateur, n'exploite aucun serveur collectant des
données, et votre configuration reste sur votre propre appareil.**

## En résumé

- Aucun compte, aucune inscription.
- Aucune donnée analytique, aucune télémétrie, aucun suivi d'utilisation, aucun cookie.
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
  identité),
- le nom de l'activation (votre nom d'hôte, facultatif).

L'application fonctionne entièrement hors ligne entre les vérifications (au plus une validation
environ tous les 30 jours).

### Android (Google Play)

Sur Android, l'achat unique est vendu et traité par **Google Play Billing**. Google est le
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

## Ce que nous ne collectons pas

- Aucune donnée analytique ou d'utilisation ; nous ne suivons pas les commandes que vous exécutez.
- Aucun accès à vos identifiants SSH ni à vos clés privées.
- Aucun cookie ni suivi web.
- Les applications ne contiennent **aucun SDK publicitaire ou analytique tiers**.

## Services tiers

- [LemonSqueezy](https://www.lemonsqueezy.com) — licence et paiement sur desktop ; leur politique
  de confidentialité s'applique aux données qu'ils traitent.
- **Google Play Billing** — achat unique sur Android ; la politique de confidentialité de Google
  s'applique.

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
