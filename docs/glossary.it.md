# Glossario

Ci sono parole di questo wiki che non ti dicono nulla? Eccole spiegate in parole semplici.

**Comando**
: Una riga di testo che dice al computer cosa fare — per esempio `df -h` mostra lo spazio libero sul disco. Commandeck esegue il comando al posto tuo quando premi un pulsante, così non devi scriverlo.

**Pulsante (casella)**
: Ogni quadrato della griglia di Commandeck. Un pulsante contiene un comando e lo esegue quando lo premi.

**Shell**
: Il programma che legge ed esegue i comandi. Su Linux e macOS di solito è `bash` o `zsh`; su Windows è **PowerShell**. Commandeck usa automaticamente quello giusto per il tuo sistema.

**Terminale**
: La finestra di testo nera in cui di solito si scrivono i comandi. Commandeck esiste proprio per permetterti di evitarla, anche se un pulsante può aprirne una se scegli la modalità «Apri nel terminale».

**Categoria**
: Un'etichetta che raggruppa pulsanti affini (per esempio *Rete* o *Hardware*). Le categorie compaiono come schede sopra la griglia e servono a filtrare ciò che vedi.

**SSH** *(Pro)*
: Un modo sicuro per eseguire comandi su un altro computer attraverso la rete — per esempio gestire il server di casa dal portatile. Commandeck usa SSH per mandare il comando di un pulsante a una macchina remota.

**Macchina** *(Pro)*
: Un computer remoto che hai aggiunto a Commandeck (indirizzo, nome utente e chiave SSH). Un pulsante può puntare a una o più macchine.

**sudo / esegui come utente**
: `sudo` esegue un comando con i permessi di amministratore; *esegui come utente* lo esegue con un account preciso (per esempio un account di servizio come `www-data`). Commandeck può farlo per te tramite un [profilo di esecuzione](reference/execution-profiles.md).

**Profilo di esecuzione** *(Pro)*
: Un insieme salvato di «condizioni di esecuzione» — quale utente e quale cartella — da riutilizzare su più pulsanti. Vedi [Profili di esecuzione](reference/execution-profiles.md).

**Output**
: Ciò che il comando scrive in risposta (per esempio i numeri sullo spazio del disco). Un pulsante può mostrarlo in una finestra, restare silenzioso o aprire un terminale.

**AppImage**
: Un'applicazione Linux in un solo file: la scarichi, la rendi eseguibile e la avvii. Nessuna installazione e nulla da toccare a livello di sistema.

**MCP** *(Pro)*
: Il ponte che consente a un assistente IA di leggere e gestire i tuoi pulsanti al posto tuo. Vedi [Integrazione IA](pro/mcp.md).

**Gratis e Pro**
: La versione **gratuita** esegue comandi locali illimitati e pulsanti personalizzati illimitati. **Pro** aggiunge macchine SSH, pulsanti multi-macchina, temi, profili, backup e integrazione con l'IA, con una prova gratuita di 14 giorni.
