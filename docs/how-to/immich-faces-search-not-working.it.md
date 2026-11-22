---
title: Immich non riconosce più i volti? Scopri perché con un clic
description: I volti non vengono raggruppati, la ricerca non trova niente. Ecco come controllare le tre cause abituali da un pulsante sul tuo computer, senza aprire un terminale sul server.
---

# Immich non riconosce più i volti? Scopri perché con un clic

Hai caricato qualche centinaio di foto. Giorni dopo i volti non sono ancora raggruppati, e cercare «spiaggia» non trova niente.

Non si è perso niente. Le tue foto sono al sicuro: quello che si è fermato è la parte di Immich che le *guarda*. Immich è fatto di quattro programmi che lavorano insieme, e volti e ricerca intelligente vengono da uno di loro: la parte di apprendimento automatico. Quando si ferma, o l'app non la raggiunge più, Immich continua a funzionare… solo che non riconosce più niente.

Il consiglio abituale è entrare nel server via SSH, elencare i container e leggerne i registri. Ecco la versione senza niente di tutto questo.

---

## Il controllo con un clic

Commandeck ha un **pack di pulsanti gratuito per Immich**. Installalo una volta e avrai un pulsante che controlla le tre cause abituali, una dopo l'altra, e ti dice qual è.

1. Apri Commandeck e aggiungi il tuo server come macchina (il suo indirizzo, il tuo nome utente, la tua password o la tua chiave SSH).
2. Menu **☰ → Pacchetti di pulsanti → Linux → Immich (Docker)** → *Installa*, e scegli quella macchina.
3. Fai clic su **Perché volti o ricerca non funzionano?**

Controlla, in parole semplici:

- **La parte di volti e ricerca è in funzione?** Se è ferma, la causa è quella, e lo dice.
- **L'app la raggiunge?** Possono essere in funzione tutte e due senza parlarsi. In quel caso ti dice dove impostare l'indirizzo giusto nelle impostazioni di Immich.
- **Cosa ha segnalato nelle ultime 24 ore?** I suoi errori e avvisi recenti, compresi quelli che vogliono dire che è rimasta senza memoria.

Niente da digitare, nessun nome di container da cercare: il pack trova i container di Immich dalla loro immagine, comunque tu li abbia chiamati.

---

## I volti vanno bene, ma qualcos'altro non va?

Lo stesso pack risponde alle altre domande per cui si entra via SSH.

**Il disco si riempie.** Immich conserva più delle tue foto: anteprime, copie convertite dei tuoi video, backup del suo database. Fai clic su **Dove è finito lo spazio su disco?**: misura ogni voce, dice cos'è e ti avvisa quando un disco è quasi pieno.

**I miei backup vengono fatti davvero?** Immich può copiare il suo database ogni notte, se l'impostazione è attiva e niente si è rotto. Fai clic su **I backup vengono eseguiti?**: trova la copia più recente e ti dice quanto è vecchia, invece di lasciartelo supporre.

**Devo aggiornare?** Fai clic su **C'è una versione più recente?**: confronta la tua versione con la più nuova e ti avvisa quando il salto è grande, di quelli in cui deve seguire anche l'app del telefono. **Aggiorna Immich** si rifiuta di partire senza una copia del database delle ultime 24 ore, perché un aggiornamento non si può annullare.

---

## Il resto del pack

Il pack è gratis e ha tredici pulsanti. I più usati:

| Pulsante | Risponde a |
|---|---|
| **Immich è in funzione?** | Ognuna delle sue quattro parti, a cosa serve, e perché una si è fermata |
| **Errori recenti** | Cosa è andato storto nelle ultime 24 ore, ogni messaggio una volta — pronto da incollare in un forum o nel tuo assistente IA |
| **Riavvia Immich** | La prima mossa quando si blocca: riavvia tutte le parti e aspetta che l'app sia pronta |
| **Risorse in questo momento** | Perché il server è occupato — di solito il riconoscimento dei volti dopo un grosso caricamento |
| **Elenca gli utenti** | Ogni account, con la sua e-mail e se è amministratore |

Ogni comando è visibile prima dell'installazione, e puoi modificarli tutti dopo. Il pack è per **Immich installato con Docker** (compose o Portainer). L'hai installato come template Unraid, app TrueNAS o snap? Alcuni pulsanti non lo troveranno.

---

## Agire sul server passa da SSH

Il tuo server Immich è una macchina diversa da quella davanti a cui sei seduto, quindi questi pulsanti lo raggiungono via SSH. Quella parte è [Commandeck Pro](../pro.md): **29 $ una volta, per sempre, con 14 giorni di prova che non chiedono né carta né account**. Il pack, come tutti i pack, è gratis.

Niente esce dal tuo computer: nessun account, nessun cloud, nessun nostro server in mezzo. Le tue macchine e le tue password restano sul tuo dispositivo.

---

**Da leggere anche:** [Vedere lo spazio del NAS con un clic](check-disk-space-nas.md) · [Aggiornare il server senza SSH](update-server-without-ssh.md) · sei all'inizio? Parti dalla [guida per principianti](../use-cases/beginner.md).
