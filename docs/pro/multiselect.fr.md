# Sélection multiple

!!! tip "Fonctionnalité Pro"
    La sélection multiple nécessite [Commandeck Pro](../pro.md).

La sélection multiple vous permet d'effectuer des opérations groupées sur plusieurs boutons à la fois — réassigner des catégories, changer de machines ou supprimer un groupe.

![Mode de sélection multiple avec des boutons sélectionnés et la barre d'actions](../assets/multiselect.png)

---

## Quand utiliser la sélection multiple

- Vous avez migré vers un nouveau serveur et devez réassigner 10 boutons
- Vous souhaitez déplacer tout un ensemble de boutons vers une autre catégorie
- Vous avez créé un lot de boutons temporaires et souhaitez tous les supprimer en même temps
- Vous avez dupliqué plusieurs boutons et devez nettoyer rapidement

---

## Démarrer une sélection

Il n'y a pas de « mode de sélection » distinct à activer. Commencez simplement à sélectionner :

- **Ctrl+clic** sur une tuile pour l'ajouter à — ou la retirer de — la sélection (un clic simple exécute toujours la commande comme d'habitude)
- **Tracez un cadre** sur une zone vide de la grille (voir [Sélection rubber-band](#sélection-rubber-band)) pour sélectionner toutes les tuiles qu'il touche

Dès qu'un bouton est sélectionné, une **barre d'actions apparaît en bas** de la fenêtre, indiquant le nombre de boutons sélectionnés et les actions groupées disponibles.

---

## Sélectionner des boutons

### Ctrl+clic pour basculer

**Ctrl+clic** sur n'importe quelle tuile pour l'ajouter à la sélection ; Ctrl+clic à nouveau pour la retirer. Les tuiles sélectionnées sont mises en surbrillance en bleu. (Un clic gauche simple — sans Ctrl — exécute la commande du bouton.)

### Sélection rubber-band

Cliquez et faites glisser sur une **zone vide** de la grille (pas sur un bouton) pour dessiner un rectangle de sélection. Tous les boutons que le rectangle chevauche sont ajoutés à la sélection actuelle.

!!! tip
    Commencez le glissement depuis les marges autour de la grille de boutons — l'espace entre les tuiles ou le rembourrage autour des bords. Commencer directement sur un bouton bascule ce bouton au lieu de dessiner un rectangle.

### Combiner les deux méthodes

Vous pouvez mélanger librement Ctrl+clic et rubber-band. Faites d'abord Ctrl+clic sur des boutons individuels, puis utilisez le rubber-band pour ajouter un groupe, puis Ctrl+clic pour désélectionner des boutons spécifiques.

---

## Actions groupées

La barre d'actions en bas affiche les opérations disponibles dès qu'au moins un bouton est sélectionné.

### Supprimer

Supprime définitivement tous les boutons sélectionnés. Une boîte de dialogue de confirmation indique le nombre ("Supprimer 5 boutons ?"). Cette action est irréversible.

Les boutons par défaut (Linux Essentials, Développement) peuvent être supprimés même dans la version gratuite.

### Catégorie

Assigne tous les boutons sélectionnés à une catégorie. Une petite boîte de dialogue demande le nom de la catégorie :

- Saisissez un nouveau nom pour créer une nouvelle catégorie
- Saisissez un nom de catégorie existant pour y déplacer les boutons
- Laissez vide et confirmez pour supprimer l'assignation de catégorie (les boutons deviennent sans catégorie)

### Machine

Assigne tous les boutons sélectionnés à une machine SSH. Un sélecteur liste vos machines configurées ainsi que **Local** :

- Sélectionner une machine → tous les boutons sélectionnés sont mis à jour pour cibler uniquement cette machine (leurs cibles précédentes sont remplacées)
- Sélectionner **Local** → tous les boutons sélectionnés sont configurés pour une exécution locale

!!! note
    L'action **Machine** remplace la cible sur chaque bouton, elle ne l'ajoute pas. Si vous souhaitez des boutons multi-machines, modifiez-les individuellement dans l'éditeur de bouton.

---

## Vider la sélection

Cliquez sur le **✕** de la barre d'actions pour vider la sélection en cours. La barre se masque et la grille revient à la normale. (Un clic simple sur un bouton exécute sa commande à tout moment — sélectionner des boutons ne gêne jamais l'usage normal.)
