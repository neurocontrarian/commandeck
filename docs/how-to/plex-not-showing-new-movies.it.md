---
title: Plex non mostra i film nuovi? Fallo guardare di nuovo
description: Hai copiato un film nella cartella e Plex lo ignora. Ecco come fargli riesaminare le librerie, da un pulsante sul tuo computer e senza aprire un terminale.
---

# Plex non mostra i film nuovi? Fallo guardare di nuovo

Hai copiato un film nella cartella dei film. Apri Plex. Non c'è.

Non è rotto niente. Plex conosce solo i file che ha *guardato*, e non sorveglia le cartelle a ogni istante — soprattutto quando la cartella sta su un NAS, su una condivisione di rete o dentro Docker, dove il segnale che dice «è arrivato un file nuovo» spesso non gli arriva mai.

La soluzione è dirgli di guardare di nuovo. Su un server il consiglio abituale è entrare via SSH e lanciare un comando con un numero di libreria che prima bisogna scoprire. Questa è la versione senza niente di tutto ciò.

---

## La soluzione con un clic

Commandeck offre un **pack di pulsanti gratuito per Plex**. Installalo una volta e avrai un pulsante che chiede a Plex di riesaminare tutte le librerie — film, serie, musica — nominando ciascuna mentre procede.

1. Apri Commandeck e aggiungi il tuo server come macchina (indirizzo, nome utente, password o chiave SSH).
2. Menu **☰ → Pack di pulsanti → Linux → Plex (Docker)** → *Installa*, e scegli quella macchina. (Plex installato direttamente sulla macchina invece che in un container? Prendi **Plex (system install)**: gli stessi pulsanti, con comandi diversi sotto.)
3. Premi **Look for new films and episodes**.

```
Film... looked through.
Serie... looked through.
Musica... looked through.

Plex legge i file nuovi in background; compaiono via via.
```

Niente da digitare, nessun numero di libreria da cercare. Il film nuovo compare in Plex dopo qualche secondo; una libreria grande richiede qualche minuto.

---

## Se ancora non compare

Tre motivi spiegano quasi tutti i casi, e lo stesso pack risponde a tutti e tre.

**Il disco è pieno.** Plex ha bisogno di spazio per scrivere quello che impara su un file. Con il disco al 100% una scansione può finire senza aggiungere nulla e, nel caso peggiore, danneggiare il catalogo di Plex. Premi **Space & conversion cache**: legge tutte le cartelle che Plex vede e ti avverte a chiare lettere se una è quasi piena.

**Plex non riesce a leggere il file.** Un film copiato da un altro computer conserva spesso i permessi di quello. Premi **What Plex reported**: se Plex non è riuscito ad aprire qualcosa lo dice lì, una volta sola, invece di finire sepolto sotto migliaia di righe di chiacchiere sue.

**Il catalogo stesso è danneggiato.** È raro, ma spiega un Plex che dimentica film o perde i segni di visione. Premi **Is the database healthy?**: controlla una *copia* del database di Plex, quindi non modifica niente, e ti dice che cosa ha trovato.

---

## Il resto del pack

Il pack è gratuito e ha quindici pulsanti. I più usati:

| Pulsante | Risponde a |
|---|---|
| **Is Plex running?** | Se è in funzione e, se si è fermato, perché |
| **Why is Plex busy?** | Un video in conversione, una scansione in corso, o nessuna delle due |
| **What Plex reported** | Tutti i messaggi scritti da Plex, ognuno una volta, con quante volte si è ripetuto |
| **Why is the graphics chip not used?** | I quattro motivi per cui Plex converte il video nel modo lento |
| **Restart Plex** | La prima mossa quando qualcosa si blocca |
| **Clear the conversion cache** | Cancella solo il video convertito temporaneo, mai i tuoi film |

Ogni comando è visibile prima di installare, e puoi modificarli tutti dopo.

---

## Agire sul server passa da SSH

Il tuo server Plex è una macchina diversa da quella davanti a cui sei seduto, quindi questi pulsanti lo raggiungono via SSH. Quella parte è [Commandeck Pro](../pro.md): **29 $ una volta, per sempre, con 14 giorni di prova che non chiedono né carta né account**. Il pack, come tutti i pack, è gratis.

Niente esce dal tuo computer: nessun account, nessun cloud, nessun nostro server in mezzo. Le tue macchine e le tue password restano sul tuo dispositivo.

---

**Da leggere anche:** [Riavviare Jellyfin o Plex senza terminale](restart-jellyfin-plex-without-terminal.md) · [Vedere lo spazio del NAS con un clic](check-disk-space-nas.md) · sei all'inizio? Parti dalla [guida per principianti](../use-cases/beginner.md).
