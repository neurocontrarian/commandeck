---
title: Plex si mangia tutto il processore? Ecco perché
description: Il server si scalda e il film scatta. Plex sta rifacendo il video invece di inviarlo così com'è. Scopri con un clic perché e che cosa cambiare, senza terminale.
---

# Plex si mangia tutto il processore? Ecco perché

Il film scatta. La ventola parte. Il server, silenzioso tutta la settimana, è improvvisamente al 100%.

Quasi sempre succede la stessa cosa: **Plex sta rifacendo il video, fotogramma per fotogramma, invece di inviare il file così com'è.** Plex la chiama conversione. Scatta quando il dispositivo con cui guardi non sa leggere il file originale: formato sbagliato, immagine troppo grande, o un sottotitolo da incidere.

Il tuo server può fare quel lavoro in due modi. Il chip grafico se ne occupa senza nemmeno scaldarsi. Il processore ci arriva al 100% e fatica. La maggior parte dei server di casa sta sulla via lenta senza che il proprietario lo abbia mai saputo.

---

## Saperlo con un clic

Commandeck offre un **pack di pulsanti gratuito per Plex**: uno per Plex in Docker, uno per Plex installato sulla macchina stessa. Installalo, puntalo al tuo server e due pulsanti rispondono.

**1. «Why is Plex busy?»** — dice se una conversione è in corso, su quale file e quanto costa:

```
=== Converting a video right now? ===
Yes - Plex is converting a video right now.
  File: Sintel
  CPU:  98.0% for that one process
```

**2. «Why is the graphics chip not used?»** — verifica uno a uno i quattro motivi per cui Plex ripiega in silenzio sul processore:

```
=== 1. Is there a graphics chip to use? ===
No /dev/dri/renderD* on this machine.

=== 2. Is Plex allowed to open it? ===
The device belongs to group: render
The plex user is NOT in that group. Fix it with: sudo usermod -aG render plex

=== 3. Is the setting ticked? ===
Plex has never been given the setting.
Settings > Transcoder > Use hardware acceleration when available.

=== 4. What the log says the last time it converted ===
Nothing about hardware in the recent log.
```

Ricorda anche ciò che nessun comando può verificare: la conversione hardware richiede un **Plex Pass** attivo. Senza, Plex usa il processore e non lo dice mai.

---

## Le quattro cause, e che cosa fare per ognuna

**Il chip non c'è, o non è condiviso.** Su un mini-PC o un NAS c'è: quasi tutti i processori Intel degli ultimi dieci anni ne hanno uno. Se il tuo Plex gira in un container Docker, bisogna affidargli il dispositivo: aggiungi `devices: - /dev/dri:/dev/dri` al file compose, o spunta l'equivalente nel tuo gestore di container. Se Plex gira in un container Proxmox, il dispositivo va passato dall'host.

**Plex non ha il permesso di aprirlo.** Il chip appartiene a un gruppo, di solito `render` o `video`, e l'account con cui gira Plex deve farne parte. Il pulsante mostra il comando esatto per la tua macchina.

**L'impostazione è spenta.** Plex non la accende da solo: *Impostazioni → Transcodificatore → Usa l'accelerazione hardware quando disponibile*.

**Niente Plex Pass.** La conversione hardware è una funzione a pagamento. Questa non è un difetto, e nessun comando la aggira.

---

## A volte la soluzione è non convertire affatto

La conversione più veloce è quella che non avviene. Due cose da provare prima di comprare qualsiasi cosa:

- **Abbassa la qualità sul dispositivo che sta guardando.** Se il lettore chiede «Originale», Plex invia il file intatto e non fa nulla.
- **Guarda che cosa viene convertito.** Se il pulsante dice che l'immagine è «copiata così com'è» e cambia solo l'audio, il tuo server lavora appena: è il caso buono, non c'è niente da sistemare.

E una trappola da conoscere: un disco quasi pieno rallenta tutto, conversioni comprese. Il pulsante **Space & conversion cache** del pack ti avverte a chiare lettere quando uno dei dischi sta finendo lo spazio.

---

## Ottenere i pulsanti

Menu **☰ → Pacchetti di pulsanti → Linux → Plex (Docker)** oppure **Plex (system install)**, gratis come tutti i pack. Scegli quello che corrisponde a come Plex è installato sul tuo server: i due usano comandi completamente diversi.

Raggiungere il server via SSH è [Commandeck Pro](../pro.md): **29 $ una volta, per sempre, con 14 giorni di prova senza carta e senza account**. Niente esce dal tuo computer: nessun account, nessun cloud, nessun nostro server in mezzo.

---

**Da leggere anche:** [Plex non mostra i film nuovi?](plex-not-showing-new-movies.md) · [Vedere lo spazio del NAS con un clic](check-disk-space-nas.md) · sei all'inizio? Parti dalla [guida per principianti](../use-cases/beginner.md).
