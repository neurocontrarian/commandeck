# Variables de commande

La commande d'un bouton peut contenir des **emplacements** écrits `{{clef}}`. Au clic,
Commandeck vous demande chaque valeur, la remplace, puis exécute la commande. La valeur ne
sert **que pour cette exécution** — elle n'est jamais enregistrée.

Cela garde un pack partagé générique (aucune donnée personnelle figée) : le pack livre
`docker restart {{container}}`, et chacun saisit le nom de son conteneur à l'exécution.

## Fonctionnement

1. Une commande comme `docker logs --tail {{lines}} {{container}}` a deux emplacements.
2. Au clic, une petite fenêtre demande **Lignes** et **Conteneur**.
3. Vous tapez `50` et `jellyfin` → Commandeck exécute `docker logs --tail 50 jellyfin`.
4. Rien n'est stocké — la prochaine fois, la question est reposée.

Un emplacement s'écrit `{{clef}}` (lettres, chiffres, tiret bas). Les espaces internes sont
tolérés : `{{ container }}` fonctionne aussi.

## Variables standard

Ces clefs ont un libellé et une invite intégrés. Réutilisez-les pour des questions
cohérentes. La liste **s'enrichit avec le temps**.

| Emplacement | Demande | Effet sur la commande |
|---|---|---|
| `{{container}}` | nom de conteneur Docker | remplace `{{container}}` avant d'exécuter |
| `{{service}}` | nom de service systemd | remplace `{{service}}` |
| `{{path}}` | un chemin de fichier ou dossier | remplace `{{path}}` |
| `{{host}}` | un nom d'hôte ou une IP | remplace `{{host}}` |
| `{{port}}` | un numéro de port | remplace `{{port}}` |
| `{{branch}}` | une branche Git | remplace `{{branch}}` |
| `{{package}}` | un nom de paquet | remplace `{{package}}` |
| `{{user}}` | un nom d'utilisateur | remplace `{{user}}` |
| `{{pid}}` | un identifiant de processus | remplace `{{pid}}` |
| `{{lines}}` | un nombre de lignes | remplace `{{lines}}` |
| `{{player}}` | un nom de joueur | remplace `{{player}}` |
| `{{message}}` | un message | remplace `{{message}}` |

## Autres variables (saisies dans la commande)

Vous pouvez toujours saisir **n'importe quelle** clef directement dans une commande, p. ex.
`{{region}}`. Si ce n'est pas une variable standard, Commandeck la demande quand même à
l'exécution via un champ texte simple nommé d'après la clef — les packs qui utilisent leurs
propres clefs continuent donc de fonctionner.

À noter : le gestionnaire **Variable Values** et le sélecteur **Insert variable** ne listent
que les variables standard ci-dessus — vous ne pouvez pas y créer de nouvelles clefs. Les
clefs personnalisées vivent dans le texte de la commande.

## Valeurs sauvegardées (plus rapide, cohérent)

Vous pouvez enregistrer une liste de valeurs par variable dans **Menu → Valeurs de
variables** (p. ex. `service` → `jellyfin`, `sonarr`). Ensuite :

- **À la création d'un bouton**, le bouton **Insérer une variable** (à côté du champ
  Commande) permet soit d'insérer `{{service}}` (demandé à chaque exécution), soit de
  **choisir une valeur sauvegardée pour la figer** dans la commande.
- **À l'exécution**, une variable qui a des valeurs sauvegardées affiche une **liste
  déroulante** — et vous pouvez toujours saisir une autre valeur à la main.

## Ne mettez pas de secret dans une commande

N'écrivez jamais un vrai mot de passe ou une clé d'API dans une commande. Si une commande en
a besoin, utilisez un emplacement (p. ex. `{{token}}`) pour qu'il soit saisi à l'exécution et
jamais stocké ni partagé dans un pack. Les soumissions de pack contenant un secret littéral
sont rejetées automatiquement.
