---
description: Trasforma i comandi SSH di Batocera in pulsanti. Scopri perché un gioco non parte, chiudi un emulatore bloccato, risolvi uno schermo nero e vedi che cosa riempie il disco, senza collegare una tastiera alla macchina sotto il televisore.
---

# Gestire la tua Batocera senza tastiera

Una macchina Batocera vive sotto il televisore. Ha un controller, non ha tastiera e non ha nessuna finestra che ti dica che cosa è andato storto. Così, il giorno in cui un gioco si rifiuta di partire, l'emulatore si blocca o lo schermo resta nero, la risposta che trovi in rete è sempre la stessa: *«entra in SSH ed esegui questo comando»*.

È un consiglio che funziona. Semplicemente si adatta male a una macchina che usi dal divano: finisci per cercare l'indirizzo IP, aprire un terminale su un altro computer e riscrivere comandi che avevi cercato tre mesi fa.

Commandeck conserva quei comandi come **pulsanti**. Li prepari una volta e poi rispondi alla domanda con un clic, dalla tua scrivania.

!!! tip "Funzione Pro"
    Parlare con un'altra macchina via SSH richiede [Commandeck Pro](../pro.md), incluso nella prova di 14 giorni e senza account. Batocera è gratuita e non ha bisogno che le installi nulla.

---

## Che cosa ti serve

- Una **macchina Batocera in rete**, accesa, e il suo **indirizzo IP** (Batocera lo mostra nel menu principale, sotto *Impostazioni di rete*).
- L'SSH è **già attivo** su Batocera: non c'è nulla da installare o configurare sulla macchina.
- Commandeck sul tuo computer Windows, Mac o Linux.

Batocera ti collega come **root**, quindi qui non compaiono né `sudo` né password di amministratore.

---

## Passo 1 — Aggiungi la macchina

**Menu ☰ → Gestisci macchine → Aggiungi**, poi compila:

| Campo | Valore |
|-------|--------|
| Nome | `Batocera` |
| Host | l'IP della tua macchina, per esempio `192.168.1.42` |
| Utente SSH | `root` |
| Porta | `22` |
| Autenticazione | **Password** |
| Password SSH | `linux` |

`linux` è la password di fabbrica di Batocera per l'utente `root`: ce l'hai già e non c'è nulla da preparare sulla macchina. (Se l'hai cambiata nelle impostazioni di Batocera, usa la tua.)

Premi **Prova**. Dovrebbe tornare verde, e hai finito.

!!! note "Dove viene conservata la password"
    Commandeck non la scrive mai in un file leggibile: finisce nel portachiavi del tuo computer — Gestione credenziali su Windows, Portachiavi su macOS, il servizio dei segreti di sistema su Linux. Si digita una volta, qui, e mai più.

---

## Passo 2 — Installa il pacchetto Batocera

Invece di scrivere i comandi a mano, installa l'insieme già pronto.

**Menu ☰ → Pacchetti di pulsanti → Linux → Batocera → Installa**, e scegli la macchina appena aggiunta.

Ottieni diciassette pulsanti, già formulati come domande e non come comandi:

| Pulsante | Risponde a |
|----------|------------|
| **Informazioni di sistema Batocera** | Che macchina è questa e da quanto è accesa? |
| **C'è un gioco in esecuzione?** | Quale gioco e di quale console, per nome e non con un numero di processo |
| **Debug (es_launch_stderr.log)** | Perché l'ultimo gioco è partito, o non è partito |
| **Debug (es_log.txt)** | Che cosa sta facendo il menu stesso: copertine, temi, avvii lenti |
| **Vedere partire un gioco in diretta** † | Lo stesso log, che scorre mentre il gioco parte |
| **Spazio libero** | Quanto è pieno il disco e quali cartelle occupano posto |
| **Quali sistemi si mangiano il disco?** | La dimensione della cartella ROM di ogni console, dalla più grande |
| **Esplorare il disco (ncdu)** † | Percorri /userdata cartella per cartella e cancella strada facendo |
| **I miei controller** | Quali pad vengono visti, con la batteria di quelli senza filo |
| **Disconnettere i pad senza filo** | Spegne tutti i dispositivi Bluetooth: evita che i pad si scarichino di notte |
| **Che cosa sta facendo il mio schermo?** | La risoluzione inviata e le modalità che il televisore accetta |
| **Impostare la modalità video** | Forza una risoluzione: il salvataggio per lo schermo nero |
| **Chiudere il gioco in esecuzione** | Termina un emulatore bloccato e ti riporta al menu |
| **Riavviare il menu** | Riavvia EmulationStation senza riavviare la macchina |
| **Monitor in diretta (htop)** † | CPU, memoria e processi aggiornati mentre giochi |
| **Riavviare la macchina** / **Spegnere la macchina** | In modo pulito, dalla tua scrivania |

† Aprono un terminale sul tuo computer, quindi questi tre sono solo da scrivania.

Tutti i pacchetti sono gratuiti. Solo la connessione SSH è una funzione Pro.

---

## I quattro momenti in cui lo userai davvero

### «Questo gioco non parte»

Premi A, lo schermo sfarfalla e sei di nuovo nel menu. Batocera ha annotato che cosa è successo, ma il file è sulla macchina.

Premi **Debug (es_launch_stderr.log)**. Estrae per prime le righe sospette dell'ultimo avvio — un BIOS mancante, un formato di ROM non supportato, un problema di permessi — e ti dice chiaramente quando lì dentro non c'è nulla di strano. Poi premi **Copia**: è esattamente ciò che i forum di Batocera ti chiedono di incollare quando chiedi aiuto.

Se il problema è il menu e non un gioco — un sistema che non compare, un tema rotto, il recupero delle copertine che si blocca — usa **Debug (es_log.txt)**. È il secondo file che l'assistenza chiede.

EmulationStation scrive quel secondo log solo quando se ne alza il livello di dettaglio: se è spento, il pulsante ti dice dove accenderlo e intanto ti elenca i log che esistono davvero.

### «Si è bloccato»

Il controller non fa nulla e l'emulatore è fermo sullo schermo. **Chiudere il gioco in esecuzione** ti dice quale gioco sta chiudendo, lo termina e verifica dopo che sei davvero tornato al menu. Se non basta, **Riavviare il menu** ricostruisce l'interfaccia senza un riavvio completo.

### «Lo schermo è nero» oppure «l'immagine è tagliata»

**Che cosa sta facendo il mio schermo?** mostra la risoluzione inviata in questo momento e l'elenco delle modalità che il tuo televisore accetta davvero. **Impostare la modalità video** ne forza una: scrivi il nome della modalità e, se sbagli, il pulsante si rifiuta di cambiare qualcosa e ti mostra l'elenco valido.

### «I pad sono di nuovo scarichi»

Un pad senza filo lasciato sul tappeto tiene sveglia la sua radio e al mattino è vuoto. **Disconnettere i pad senza filo** chiude tutte le connessioni Bluetooth della macchina e il pad si spegne da solo pochi secondi dopo. È anche il modo educato di far mollare la presa a un pad quando un gioco si è bloccato con lui. Per riaccenderlo, il suo tasto centrale.

---

### «Ho finito lo spazio»

**Spazio libero** mostra quanto è pieno il disco e le cartelle più grandi in GB o TB. **Quali sistemi si mangiano il disco?** lo scompone console per console, così vedi che un sistema si sta prendendo metà disco prima di cominciare a cancellare qualcosa.

---

## Anche dal divano

Gli stessi pulsanti esistono sul telefono: Commandeck per Android è [in test chiuso](../android-beta.md) e legge gli stessi pacchetti. Funziona sulla rete di casa, oppure sulla tua VPN se ne hai una. Nulla passa da un servizio nel cloud, perché non esiste nessun servizio nel cloud.

---

## Cose utili da sapere su Batocera

Batocera non è un normale server Linux, e questo cambia quali comandi hanno senso:

- **Sei root.** Nessun `sudo` e nessuna password di amministratore da nessuna parte.
- **Il sistema è di sola lettura fuori da `/userdata`.** Ciò che modifichi altrove sparisce al riavvio successivo.
- **Non ci sono `systemctl` né `journalctl`.** I log sono file normali; per questo i due pulsanti di debug leggono file invece di interrogare un servizio.
- **Gli strumenti a schermo intero** (`htop`, `ncdu`, un log in diretta) hanno bisogno di un terminale vero in cui disegnarsi. Un pulsante glielo dà: la sua modalità è **Apri nel terminale**, e Commandeck apre `ssh -t` verso la macchina in una finestra di terminale del tuo computer. Il pacchetto ne porta tre: *Vedere partire un gioco in diretta*, *Esplorare il disco (ncdu)* e *Monitor in diretta (htop)*.
- Quei tre sono **solo da scrivania**: un telefono non ha un terminale da aprire, quindi non compaiono nella griglia su Android. Tutti gli altri pulsanti del pacchetto funzionano su entrambi.
- Tutto ciò che potrebbe **cancellare un disco** è stato lasciato fuori dal pacchetto di proposito.

---

## Correlato

- [Pacchetti di pulsanti](../packs.md): che cos'è un pacchetto e come funziona l'installazione
- [Macchine SSH](../reference/ssh-machines.md): aggiungere macchine, porte e risoluzione dei problemi
- [Gestire un parco homelab](homelab.md): la stessa idea su più macchine
- [Avvio rapido](../quick-start.md): se questo è il tuo primo pulsante
