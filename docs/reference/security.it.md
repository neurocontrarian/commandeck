# Sicurezza e come funziona

🔰 **In parole semplici:** Commandeck esegue soltanto i comandi che *tu* scrivi e premi, sui tuoi computer. Non conserva mai le tue password in chiaro, non apre mai la tua macchina alla rete durante l'uso normale e ti chiede conferma per tutto ciò che hai segnato come importante.

## Perché fidarsi di questo progetto?

- **Gira sul tuo computer, non nel cloud.** Non c'è nessun account da creare né alcun server di un'azienda che custodisce i tuoi dati. Tutto ciò che Commandeck sa resta sulla tua macchina.
- **Acquisto unico.** Paghi una volta e la versione che hai installato continua a funzionare. Non c'è nessun abbonamento da disdire né alcun server che un giorno possa spegnersi lasciandoti a piedi.
- **Nessuna telemetria, mai.** Commandeck non ha statistiche né account, e non manda i tuoi dati da nessuna parte: ciò che accade sulla tua macchina resta sulla tua macchina.
- **Disponibile in 11 lingue**, e ognuna è mantenuta come parte vera dell'applicazione, non come un'aggiunta dell'ultimo momento.

## I tuoi comandi, visibili e modificabili

Ogni pulsante mostra il suo comando in chiaro nell'[editor dei pulsanti](button-editor.md). Non c'è nulla di nascosto o mascherato: quello che vedi è esattamente ciò che parte quando premi. Commandeck non cambia mai i tuoi comandi alle tue spalle; l'unica cosa che a volte aggiunge è la cartella o l'account utente che scegli tu stesso in un profilo.

## Autenticazione SSH

Quando colleghi Commandeck a un altro computer (Pro), ti identifichi con una **chiave SSH** (consigliata) o con una **password**. In entrambi i casi, la tua password non viene mai scritta su disco in una forma leggibile da chiunque.

- Una password salvata finisce nel deposito sicuro già presente nel tuo sistema: lo stesso forziere protetto che il sistema operativo usa per le proprie password (Portachiavi su macOS, Gestione credenziali su Windows, GNOME Keyring o KWallet su Linux). **Non viene mai copiata in un backup.**
- Su qualche raro sistema privo di quel deposito sicuro, Commandeck ripiega su un file locale cifrato che solo il tuo account può aprire, e ti avverte chiaramente che quella protezione è più debole.
- **La prima volta che ti colleghi a una macchina nuova**, Commandeck ti mostra la sua impronta di identità e ti chiede di confermarla. È lo stesso controllo di sicurezza che fa il classico strumento `ssh`, ma in una finestra gentile invece che in un terminale.
- Se la tua chiave SSH è protetta da una frase di accesso, Commandeck te lo dice chiaramente quando qualcosa va sbloccato, invece di fallire in silenzio.

## Password di sudo

Alcuni comandi hanno bisogno di una password di amministratore (sudo) per partire. Se decidi di salvarne una in un [profilo](execution-profiles.md), viene trattata esattamente come una password SSH: finisce nel deposito sicuro del tuo sistema e **non viene mai scritta nei tuoi file di configurazione né nei backup**; lì risulta soltanto che una password esiste, mai la password stessa. Su un sistema senza deposito sicuro si ripiega su un file cifrato legato a quel computer preciso (così non può essere copiato altrove), con un avviso chiaro. Quando un comando ne ha bisogno, Commandeck la passa direttamente al sistema, così non devi riscriverla in un terminale.

## Conferma per singolo pulsante

Qualsiasi pulsante può avere attivo **Chiedi conferma prima di eseguire** (editor dei pulsanti → Comportamento). Con quello acceso, Commandeck ti mostra il comando esatto e aspetta il tuo consenso prima di fare qualsiasi cosa: una buona idea per riavvii, cancellazioni e tutto ciò che richiede una password di amministratore.

## Accesso dell'IA / MCP (Pro)

Commandeck può collegarsi a un assistente IA perché ti aiuti a leggere e organizzare i tuoi pulsanti. È del tutto facoltativo e resta **spento finché non lo accendi tu**. Diversi blocchi indipendenti ti lasciano il comando:

- L'assistente può vedere o modificare i tuoi pulsanti solo dopo che hai attivato *Consenti l'accesso MCP* nelle Preferenze.
- Prima di poter eseguire un pulsante al posto tuo devono essere attivi **tre** permessi distinti: un interruttore generale, uno per singolo pulsante e — per le cose delicate — una conferma finale. Se ne manca anche uno solo, non parte nulla.
- Ogni azione dell'assistente viene scritta in un registro sul tuo computer, con l'ora, il pulsante, il risultato e la durata, così puoi sempre vedere esattamente che cosa è successo.
- Quando lo avvia un assistente da scrivania, la connessione resta interamente dentro il tuo computer e non apre nessuna porta di rete. (Un componente facoltativo, per un preciso strumento web, apre invece una connessione locale: se lo usi, tienilo dentro la rete di casa, dietro il firewall.)

## Da che cosa ti protegge Commandeck

Commandeck è uno **strumento personale da scrivania**. Dà per scontato che chi è seduto davanti al computer abbia il permesso di eseguire comandi sulle proprie macchine.

Le sue protezioni servono a evitare *incidenti* e sorprese: eseguire la cosa sbagliata per errore, lasciare che una password salvata finisca in un backup o in una cartella sincronizzata, o un assistente IA che agisce senza il tuo consenso. È a questo che servono le conferme, il deposito sicuro delle password e i blocchi dell'IA.

Quello che **non** cerca di fare è proteggere il tuo computer da qualcuno che si è già impossessato del tuo account o che è seduto davanti alla tua macchina sbloccata. Nessuna applicazione da scrivania può farlo: a quel punto quella persona potrebbe comunque eseguire quei comandi da sé. Tenere al sicuro il computer e l'account (blocco dello schermo, una password di accesso solida) è la base su cui Commandeck si appoggia.
