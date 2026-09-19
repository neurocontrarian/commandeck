# Caso d'uso: gestione di un server domestico

Questa guida prepara Commandeck per seguire un tipico server di casa: una macchina con Plex, con Pi-hole o che fa da NAS. L'obiettivo è ridurre a un solo clic le operazioni di manutenzione più comuni.

!!! tip "Funzione Pro"
    Questa guida controlla una macchina remota via SSH. **Le macchine SSH, i pulsanti multi-macchina e i profili di esecuzione richiedono [Commandeck Pro](../pro.md).** Nella versione gratuita puoi comunque creare gli stessi pulsanti per eseguirli sul tuo computer.

## Lo scenario

Hai un Raspberry Pi o un mini-PC nella rete di casa. Ci girano:

- **Plex Media Server**: il tuo server video personale
- **Pi-hole**: blocco della pubblicità per tutta la rete
- **Samba**: condivisione dei file in casa

E sei stanco di entrare in SSH ogni volta che serve riavviare un servizio o controllare il disco.

---

## Passo 1 — Aggiungi il server come macchina SSH

Apri **Menu → Gestisci macchine → +** e compila:

| Campo | Valore di esempio |
|-------|-------------------|
| Nome | `Server di casa` |
| Host | `192.168.1.50` |
| Utente SSH | `pi` |
| Porta | `22` |
| Percorso della chiave SSH | `~/.ssh/id_ed25519` |
| Icona | Server |

Se non hai ancora una chiave SSH, premi **Genera chiave SSH** e poi **Copia la chiave sul server**, inserendo la password una volta sola. Poi premi **Prova** per confermare che la connessione funziona.

!!! tip "Funzione Pro"
    Aggiungere macchine SSH richiede [Commandeck Pro](../pro.md).

---

## Passo 2 — Crea una categoria «Server di casa»

Nell'editor dei pulsanti, tutti i pulsanti che crei per questo server avranno **Categoria: Server di casa**. Così restano raggruppati sotto una voce dedicata nel menu delle categorie.

---

## Passo 3 — Crea i pulsanti

### Controllare lo spazio su disco

| Campo | Valore |
|-------|--------|
| Etichetta | `Uso del disco` |
| Comando | `df -h` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` (la tua macchina SSH) |
| Modalità di esecuzione | `Mostra l'output` |
| Icona | `drive-harddisk-symbolic` |

Mostra il dettaglio di ogni filesystem del server. La finestra di output si apre da sola.

---

### Riavviare Plex

| Campo | Valore |
|-------|--------|
| Etichetta | `Riavvia Plex` |
| Comando | `sudo systemctl restart plexmediaserver` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` |
| Modalità di esecuzione | `Silenzioso` |
| Chiedi conferma prima di eseguire | Attivo |
| Suggerimento | `Riavvia il servizio Plex Media Server` |
| Icona | `media-playback-start-symbolic` |

La conferma evita i riavvii accidentali mentre qualcuno sta guardando qualcosa.

---

### Aggiornare i pacchetti

| Campo | Valore |
|-------|--------|
| Etichetta | `Aggiorna il sistema` |
| Comando | `sudo apt update && sudo apt upgrade -y` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` |
| Modalità di esecuzione | `Mostra l'output` |
| Suggerimento | `Aggiorna tutti i pacchetti installati` |

La modalità `Mostra l'output` ti fa vedere che cosa è stato aggiornato.

---

### Svuotare la cache DNS di Pi-hole

| Campo | Valore |
|-------|--------|
| Etichetta | `Svuota DNS` |
| Comando | `pihole restartdns` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` |
| Modalità di esecuzione | `Silenzioso` |

---

### Vedere lo stato di Samba

| Campo | Valore |
|-------|--------|
| Etichetta | `Stato di Samba` |
| Comando | `sudo systemctl status smbd nmbd` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` |
| Modalità di esecuzione | `Mostra l'output` |

---

### Riavviare il server

| Campo | Valore |
|-------|--------|
| Etichetta | `Riavvia il server` |
| Comando | `sudo systemctl reboot` |
| Categoria | `Server di casa` |
| Destinazione | `Server di casa` |
| Modalità di esecuzione | `Silenzioso` |
| Chiedi conferma prima di eseguire | Attivo |
| Colore | `#e01b24` (rosso: segnale di pericolo) |
| Suggerimento | `Riavvia il server di casa: disconnette tutti` |

---

## Passo 4 — Multi-macchina: eseguire su più server

Se in seguito aggiungi un secondo server (un NAS, un altro Pi), puoi configurare pulsanti che puntano a più macchine. Per esempio un pulsante **Aggiorna il sistema** da usare su entrambe:

1. Apri l'editor del pulsante **Aggiorna il sistema**
2. In **Macchine di destinazione**, attiva sia `Server di casa` sia la seconda macchina
3. Salva

Da lì in poi, premendo il pulsante si apre il [selettore di macchina](../reference/ssh-machines.md#the-machine-picker): scegli quale aggiornare, oppure premi due volte per farle entrambe.

---

## Risultato

Scegliendo la categoria **Server di casa** dal menu in alto hai a un clic tutto ciò che ti serve. Senza terminale.

!!! tip
    Se durante la giornata torni spesso sul server, attiva **Sempre in primo piano** dal menu. Commandeck resta visibile mentre lavori in altre applicazioni.

---

## Guide rapide

Scorciatoie per un singolo compito, tra i più frequenti:

- [Riavviare Jellyfin o Plex senza terminale](../how-to/restart-jellyfin-plex-without-terminal.md)
- [Gestire il server di casa da Windows](../how-to/manage-home-server-from-windows.md)
- [Comandi Docker come pulsanti](../how-to/docker-commands-one-click-buttons.md)
- [Vedere lo spazio del NAS con un clic](../how-to/check-disk-space-nas.md)
- [Aggiornare il server senza SSH](../how-to/update-server-without-ssh.md)
