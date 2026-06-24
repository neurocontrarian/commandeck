# Gérer son serveur maison depuis Windows

Vous vivez sur un PC Windows, mais votre serveur maison tourne sous Linux — un NAS, un mini-PC, une machine Proxmox, un Raspberry Pi. Chaque fois qu'il faut s'en occuper, vous êtes coincé entre des options pénibles : ouvrir PowerShell et se connecter en SSH à la main, installer PuTTY et se rappeler les commandes, ou fouiller un tableau de bord web qui ne couvre pas ce dont vous avez vraiment besoin.

Commandeck offre une troisième voie : une application Windows normale où chaque tâche serveur est un bouton. Vous cliquez, la commande s'exécute sur votre serveur Linux via SSH, et le résultat s'affiche dans une fenêtre. Pas de terminal, pas de commandes à mémoriser.

![Une grille Commandeck de boutons serveur maison : Espace disque, Ce qui tourne, Mettre à jour le serveur, Redémarrer le multimédia, Plus gros dossiers et un Reboot rouge](../assets/howto-home-server-grid.png)

---

## Pourquoi ça colle à la situation Windows → Linux

Beaucoup de serveurs maison sont aujourd'hui montés avec une IA comme tutrice — elle dit quoi installer et fournit les commandes. Vous vous retrouvez avec une machine Linux que vous touchez à peine directement et un tas de commandes éparpillées dans de vieilles conversations ChatGPT ou Claude. Les retrouver à chaque panne, c'est ça la vraie corvée.

Commandeck, c'est l'endroit où ces commandes deviennent des boutons. Il tourne nativement sous Windows (aussi Mac et Linux), vous gérez donc le serveur Linux depuis le bureau que vous utilisez déjà toute la journée.

---

## Étape 1 — Installer Commandeck sous Windows

[Téléchargez](../download.md) l'installeur Windows et lancez-le. C'est une application de bureau normale — aucune ligne de commande pour l'installer ni l'utiliser.

---

## Étape 2 — Ajouter votre serveur une fois

Ouvrez **Menu → Gérer les machines → +** et renseignez les détails de votre serveur :

| Champ | Exemple |
|-------|---------|
| Nom | `Serveur maison` |
| Hôte | `192.168.1.50` |
| Utilisateur SSH | `pi` |
| Port | `22` |
| Clé SSH | cliquez **Générer une clé SSH**, puis **Copier la clé vers le serveur** |

Si vous n'avez jamais utilisé de clés SSH, Commandeck s'en charge pour vous — générez une clé, copiez-la vers le serveur (vous tapez votre mot de passe une seule fois), puis cliquez **Tester** pour confirmer la connexion. Ensuite, vous ne tapez plus jamais de mot de passe.

!!! tip "Le SSH est Pro"
    Se connecter à une autre machine est une fonctionnalité de [Commandeck Pro](../pro.md) — **29 $ une seule fois, à vie, essai gratuit de 14 jours (sans carte)**. C'est la raison d'être de l'application pour le cas Windows → Linux.

---

## Étape 3 — Transformer vos tâches courantes en boutons

Créez un bouton pour chaque chose que vous faites régulièrement sur le serveur. Quelques-unes qui conviennent à presque tous les serveurs maison :

| Libellé | Commande | Mode |
|---------|----------|------|
| `Espace disque` | `df -h` | Afficher la sortie |
| `Ce qui tourne` | `docker ps` | Afficher la sortie |
| `Mettre à jour le serveur` | `sudo apt update && sudo apt upgrade -y` | Afficher la sortie |
| `Redémarrer le multimédia` | `sudo systemctl restart jellyfin` | Silencieux + Confirmer |
| `Reboot` | `sudo systemctl reboot` | Silencieux + Confirmer (rouge) |

Chaque bouton pointe vers le serveur ajouté à l'étape 2. Cliquer dessus exécute la commande **sur le serveur** et vous montre le résultat sur votre bureau Windows.

---

## Le résultat

Votre serveur Linux a maintenant un tableau de bord Windows que vous avez construit, réglé exactement sur les tâches que vous faites. Pas de PowerShell, pas de PuTTY, pas de fouille dans de vieilles conversations.

- **Privé par conception** — ni compte, ni cloud, ni télémétrie. Les commandes vont directement de votre PC à votre serveur.
- **Vos boutons sont de simples fichiers** sur votre propre ordinateur — sauvegardez-les, déplacez-les vers un autre PC, ils sont à vous.
- **La même application sur Mac et Linux** si vous changez de machine plus tard, et une application Android native pour que les mêmes boutons marchent depuis votre téléphone.

---

**Pour aller plus loin :** le guide [Gestion d'un serveur domestique](../use-cases/home-server.md) en est la version complète, étape par étape. Plusieurs machines ? Voir [Gérer un parc homelab](../use-cases/homelab.md).
