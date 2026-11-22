---
title: Controlla la configurazione di Home Assistant prima di riavviare
description: Un refuso in un file YAML e Home Assistant non torna dopo un riavvio. Ecco un pulsante di riavvio che controlla prima la configurazione, e si rifiuta se è rotta.
---

# Controlla la configurazione di Home Assistant prima di riavviare

Hai copiato in `configuration.yaml` un'automazione trovata su un forum. Riavvii Home Assistant. Non torna.

È il modo più comune di restare senza Home Assistant per una serata: un rientro sbagliato, una virgoletta dimenticata, e si rifiuta di partire. Home Assistant ha il suo controllo della configurazione; il trucco è usarlo *ogni volta*, prima di ogni riavvio, anche il giorno in cui hai fretta.

Il consiglio abituale è entrare nel server via SSH e lanciare il controllo a mano dentro il container. Ecco la versione senza niente di tutto questo.

---

## Il controllo con un clic

Commandeck ha un **pack di pulsanti gratuito per Home Assistant**. Installalo una volta e avrai due pulsanti che si ricordano al posto tuo.

1. Apri Commandeck e aggiungi il tuo server come macchina (il suo indirizzo, il tuo nome utente, la tua password o la tua chiave SSH).
2. Menu **☰ → Pacchetti di pulsanti → Linux → Home Assistant (Docker)** → *Installa*, e scegli quella macchina.
3. Dopo aver modificato un file, fai clic su **La mia configurazione è valida?**

Lancia il controllo di Home Assistant, mostra il suo rapporto e chiude con un verdetto in una riga:

- **Valida**: riavviare è sicuro.
- **Problemi trovati**: non riavviare finché non li hai corretti; il rapporto qui sopra mostra cosa non va.
- **Partirà, ma alcune parti verranno ignorate**: riavviare è sicuro, le parti elencate restano spente finché non le correggi.

Poi, invece di riavviare dalla pagina di Home Assistant, fai clic su **Riavvia Home Assistant**. Controlla prima la configurazione e **si rifiuta di riavviare se è rotta**. Se va tutto bene, riavvia Home Assistant e aspetta che la sua pagina risponda di nuovo.

Niente da digitare, nessun nome di container da cercare: il pack trova Home Assistant dalla sua immagine, comunque tu l'abbia chiamato.

---

## Si è riavviato, ma manca qualcosa?

Lo stesso pack risponde alle domande che vengono dopo.

**Un'integrazione non è tornata.** Fai clic su **Cosa non si è avviato?**: elenca le integrazioni che non si sono caricate e segnala quelle personalizzate, la causa abituale dopo un aggiornamento.

**La chiavetta Zigbee o Z-Wave non viene trovata.** Fai clic su **La mia chiavetta Zigbee o Z-Wave viene rilevata?** Controlla i due capi — il server la vede? viene passata al container? — e mostra la riga esatta da aggiungere se no.

**Qualcosa continua a fallire.** Fai clic su **Errori recenti**: tutto quello che è andato storto dall'ultimo avvio, ogni messaggio una volta invece dello stesso avviso 300 volte — pronto da incollare in un forum o nel tuo assistente IA.

---

## Il resto del pack

Il pack è gratis e ha tredici pulsanti. I più usati:

| Pulsante | Risponde a |
|---|---|
| **Home Assistant è in funzione?** | La versione che esegue, e se Docker ha dovuto riavviarlo dopo dei crash |
| **C'è una versione più recente?** | Quante versioni mensili sei indietro, e quali note leggere prima di saltare |
| **I backup vengono eseguiti?** | Il backup più recente e quanto è vecchio |
| **Aggiorna Home Assistant** | Si rifiuta di partire senza un backup delle ultime 24 ore, poi aggiorna e aspetta che risponda |
| **Database e spazio su disco** | Quanto è cresciuto il database della cronologia, e se il disco è quasi pieno |

Ogni comando è visibile prima dell'installazione, e puoi modificarli tutti dopo. Il pack è per **Home Assistant Container**, l'installazione con Docker. Usi Home Assistant OS (il Green, lo Yellow, un'immagine per Raspberry Pi, una macchina virtuale)? Questo pack non fa per te: Home Assistant OS non ha un Docker raggiungibile.

---

## Agire sul server passa da SSH

Il tuo server Home Assistant è una macchina diversa da quella davanti a cui sei seduto, quindi questi pulsanti lo raggiungono via SSH. Quella parte è [Commandeck Pro](../pro.md): **29 $ una volta, per sempre, con 14 giorni di prova che non chiedono né carta né account**. Il pack, come tutti i pack, è gratis.

Niente esce dal tuo computer: nessun account, nessun cloud, nessun nostro server in mezzo. Le tue macchine e le tue password restano sul tuo dispositivo.

---

**Da leggere anche:** [Aggiornare il server senza SSH](update-server-without-ssh.md) · [Comandi Docker come pulsanti](docker-commands-one-click-buttons.md) · sei all'inizio? Parti dalla [guida per principianti](../use-cases/beginner.md).
