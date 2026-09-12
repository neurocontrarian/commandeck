---
description: Trasforma in pulsanti i comandi di Jellyfin che finisci sempre per cercare — perché si blocca, che cosa riempie il disco, il log che chiede l'assistenza, riavviare e aggiornare — sia in Docker sia con un'installazione di sistema.
---

# Tenere in forma Jellyfin senza imparare Docker

Jellyfin è la parte del server di casa che si nota, perché è quella che usa tutta la famiglia. Quando un film si blocca, quando una cartella nuova non compare o quando il disco si riempie in silenzio, la risposta che trovi in rete è sempre un comando, e non è mai lo stesso due volte.

Commandeck conserva quei comandi come **pulsanti**. Installi il pacchetto, lo punti sul tuo server e ogni domanda diventa un tocco.

!!! tip "Funzione Pro"
    Parlare con il tuo server via SSH richiede [Commandeck Pro](../pro.md), incluso nella prova di 14 giorni e senza account. I pacchetti sono gratuiti.

---

## Prima cosa: Docker o installazione di sistema?

Esistono due pacchetti Jellyfin, perché ci sono due modi di usarlo. Se scegli quello sbagliato, ogni pulsante risponderà «non trovato».

| Hai installato Jellyfin… | Il tuo pacchetto |
|---|---|
| con **Docker** o **docker compose** (uno stack di Portainer, l'app store del NAS) | **Jellyfin (Docker)** |
| dai **pacchetti** della tua distribuzione (`apt install jellyfin`, un .deb, uno script) | **Jellyfin (systemd)** |

Se non sei sicuro, installa quello Docker e premi **Jellyfin è attivo?**. Se dice che non esiste nessun container con quel nome, hai l'installazione di sistema.

---

## Preparazione

1. **Menu ☰ → Gestisci macchine → Aggiungi**: nome, IP del server, il tuo utente SSH, porta 22. Scegli **Password** o **Chiave SSH** per l'autenticazione e premi **Prova**.
2. **Menu ☰ → Pacchetti di pulsanti → Linux → Jellyfin (Docker o systemd) → Installa**, e scegli quella macchina.

È tutta qui la configurazione. Sul server non viene installato nulla.

---

## A che cosa rispondono i pulsanti

| Pulsante | Risponde a |
|---|---|
| **Jellyfin è attivo?** | Attivo, fermo o in riavvio continuo |
| **Perché Jellyfin è occupato?** | Che cosa sta facendo adesso, di solito una conversione |
| **Risorse in questo momento** | CPU e memoria, per capire se il limite è la macchina |
| **Errori recenti** | Solo le righe di errore, estratte da un log lunghissimo |
| **Log recente completo** | Le ultime 60 righe grezze, quando gli errori non bastano |
| **Segui il log in diretta** † | Il log che scorre mentre qualcuno preme play |
| **Chi sta usando i dischi?** | Quale processo sta martellando il disco |
| **Spazio e cache di conversione** | Quanto è pieno il disco e quanto occupa la cache |
| **Accelerazione hardware** | Se la tua scheda video viene davvero usata |
| **Plugin installati** | Che cosa è caricato e che cosa non è riuscito a caricarsi |
| **Riavvia Jellyfin** | La soluzione di metà dei problemi |
| **Aggiorna Jellyfin** | Scarica e riavvia, in modo pulito |
| **Svuota la cache di conversione** | Recupera spazio senza toccare i tuoi film |
| **Shell dentro il container** † | Solo Docker, per le risposte che iniziano con «esegui questo dentro il container» |

† Aprono un terminale sul tuo computer, quindi questi due sono solo da scrivania.

---

## Le tre serate in cui lo userai

### «Si blocca in continuazione»

Premi **Perché Jellyfin è occupato?**. Se sta convertendo, il film viene trasformato al volo: è questo che scalda il server e svuota il buffer. Poi **Accelerazione hardware** ti dice se quel lavoro lo fa la scheda video o se lo fa il processore da solo, cioè la differenza tra un film fluido e uno a scatti.

Se vuoi vederlo accadere, **Segui il log in diretta** continua a scrivere mentre qualcuno preme play, così vedi partire la conversione in tempo reale.

### «Non parte» / «la libreria è vuota»

Prima **Jellyfin è attivo?**: un container che si riavvia in continuazione somiglia moltissimo a un server spento. Poi **Errori recenti**, che estrae le righe di errore da un log troppo lungo da leggere. Nove volte su dieci **Riavvia Jellyfin** chiude la questione.

### «Il disco è pieno»

**Spazio e cache di conversione** mostra quanto è pieno il disco e quanto se ne prendono i file temporanei della conversione. **Svuota la cache di conversione** cancella quei file e nient'altro: mai i tuoi film, mai le tue impostazioni. Non premerlo mentre qualcuno sta guardando qualcosa.

---

## Anche dal divano

Gli stessi pulsanti funzionano sul telefono: Commandeck per Android è [in test chiuso](../android-beta.md) e legge gli stessi pacchetti, sulla rete di casa o sulla tua VPN.

---

## Correlato

- [Riavviare Jellyfin o Plex senza terminale](../how-to/restart-jellyfin-plex-without-terminal.md): la versione con un solo pulsante e l'equivalente per Plex
- [Pacchetti di pulsanti](../packs.md): che cos'è un pacchetto e come funziona l'installazione
- [Gestione di un server domestico](home-server.md): la stessa idea applicata al resto del server
