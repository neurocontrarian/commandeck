---
description: Commandeck est une appli de bureau (Windows, macOS, Linux) qui transforme vos commandes serveur et shell en boutons cliquables — exécution locale ou via SSH, sans terminal.
---

# Bienvenue sur Commandeck

**Votre IA vous donne les commandes. Commandeck s'en souvient.**

Commandeck est une appli de bureau pour Windows, macOS et Linux qui transforme vos commandes en une grille de boutons cliquables. Un clic — la commande s'exécute sur votre machine, ou sur votre serveur via SSH, et le résultat s'affiche. Sans terminal.

<video controls preload="metadata" style="width:100%;max-width:570px;border-radius:8px;">
  <source src="/assets/Commandeck-Demo-01.mp4" type="video/mp4">
  Votre navigateur ne peut pas lire la vidéo intégrée — <a href="/assets/Commandeck-Demo-01.mp4">téléchargez la démo</a>.
</video>

[Télécharger Commandeck](https://github.com/neurocontrarian/commandeck/releases/latest){ .md-button .md-button--primary }
[Pro & tarifs](pro.fr.md){ .md-button }

---

## À qui s'adresse Commandeck ?

<div class="grid cards" markdown>

-   :material-robot-happy:{ .lg .middle } **Une IA vous a aidé à monter votre serveur ?**

    ---

    Un NAS, Jellyfin, Docker sur un mini-PC — et des dizaines de commandes accumulées
    au fil des conversations et des guides, que vous recherchez à chaque fois que
    quelque chose réclame votre attention. Avec Commandeck elles deviennent des
    boutons : un clic depuis votre bureau Windows ou Mac, la commande s'exécute sur
    votre serveur via SSH.

    [:octicons-arrow-right-24: Guide serveur maison](use-cases/home-server.md)

-   :material-cursor-default-click:{ .lg .middle } **Vous débutez en ligne de commande ?**

    ---

    Rien à mémoriser. Commandeck est livré avec des dizaines de boutons prêts à
    l'emploi — vérifier le disque, mettre à jour le système, redémarrer — et créer
    le vôtre prend 30 secondes.

    [:octicons-arrow-right-24: Guide du débutant](use-cases/beginner.md)

-   :material-server-network:{ .lg .middle } **Vous gérez plusieurs machines ?**

    ---

    Un lanceur de commandes SSH visuel : assignez un bouton à un ou plusieurs hôtes,
    exécutez-le partout d'un seul clic — et pilotez le tout depuis un assistant IA
    via le [serveur MCP](pro/mcp.fr.md).

    [:octicons-arrow-right-24: SSH & multi-machines](pro/ssh.fr.md)

</div>

---

## Ce qui distingue Commandeck

- **Installer et c'est parti — rien à héberger.** Aucun serveur, aucun Docker, aucun YAML, aucun port à exposer. Commandeck est une appli de bureau native : on l'ouvre et on clique.
- **SSH intégré.** Ajoutez une machine une fois, puis choisissez la cible au clic — et un même bouton peut s'exécuter sur plusieurs machines à la fois.
- **Vos commandes, visibles et organisées.** Des boutons étiquetés, classés par catégorie — fini de mémoriser des alias ou de fouiller dans de vieilles conversations IA ou des fichiers de notes. Tout s'édite visuellement ; aucun fichier de config à modifier.
- **Pensé pour l'IA.** Un assistant IA peut créer des boutons pour vous via le [serveur MCP](pro/mcp.fr.md) intégré — « ajoute un bouton qui redémarre nginx » → il apparaît dans votre grille.
- **Local et privé.** Vos boutons sont des fichiers en texte clair sur votre machine. Sans cloud, sans compte, sans télémétrie.

Il fonctionne *en complément* de votre terminal, pas à sa place — Commandeck prend en charge les clics répétitifs ; vous gardez le terminal pour le travail interactif.

---

## Démarrage rapide

1. [Installer Commandeck](installation.md)
2. Lancez l'application — des dizaines de boutons par défaut sont prêts à l'emploi
3. Suivez le [Guide de démarrage rapide](quick-start.md) pour créer votre premier bouton personnalisé
4. Vous avez un serveur ? [Ajoutez-le comme machine SSH](pro/ssh.fr.md) et pointez vos boutons dessus

!!! tip "Essayez Pro gratuitement pendant 14 jours"
    La version Pro inclut un [essai automatique de 14 jours](pro.fr.md#essai-gratuit-de-14-jours) — toutes les fonctionnalités déverrouillées, sans carte bancaire, sans email. Téléchargez simplement la version Pro et lancez-la.

---

## Ce qui est inclus

| Fonctionnalité | Disponible dans |
|----------------|----------------|
| Boutons par défaut prêts à l'emploi, organisés par catégorie | Gratuit |
| Exécution locale illimitée | Gratuit |
| Boutons personnalisés | Gratuit (illimité) |
| Catégories, icônes, couleurs, infobulles | Gratuit |
| Machines SSH | [Pro](pro.fr.md) |
| Boutons multi-machines | [Pro](pro.fr.md) |
| Sélection multiple + actions de groupe | [Pro](pro.fr.md) |
| Thèmes de boutons | [Pro](pro.fr.md) |
| Sauvegarde / restauration de la configuration | [Pro](pro.fr.md) |
| Profils d'exécution (run-as-user + mot de passe sudo) | [Pro](pro.fr.md) |
| Serveur MCP (intégration assistant IA) | [Pro](pro.fr.md) |
