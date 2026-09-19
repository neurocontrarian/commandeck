# Commandeck Pro

Commandeck esiste in due edizioni: **Gratis** (solo esecuzione locale) e **Pro** (tutte le funzioni, con SSH e integrazione IA).

## Gratis a confronto con Pro

| | Gratis | Pro |
|--|--------|-----|
| Esecuzione locale dei comandi | Illimitata | Illimitata |
| Pulsanti personalizzati | Illimitati | Illimitati |
| Pulsanti predefiniti | Visibili, eseguibili, modificabili, eliminabili | Uguale |
| Variabili di comando (`{{…}}`) e valori salvati | ✓ | ✓ |
| Macchine SSH | — | Illimitate |
| Pulsanti multi-macchina | — | ✓ |
| Selezione multipla e azioni di gruppo | — | ✓ |
| Temi dei pulsanti (Bold, Phone, Neon, Retro…) | — | ✓ |
| Tema CSS su misura | — | ✓ |
| Profili di esecuzione | — | ✓ |
| Backup e ripristino della configurazione | — | ✓ |
| Server MCP (integrazione IA) | — | ✓ |
| Esecuzione dei pulsanti da parte dell'IA | — | ✓ |

!!! note
    Gratis e Pro sono **download distinti**, non lo stesso programma sbloccato da una licenza. La versione gratuita non contiene nemmeno una riga di codice Pro.

## Prezzo

**29 $, acquisto unico. Si compra una volta ed è tuo per sempre.** Nessun abbonamento e nessun rinnovo: la versione che compri continua a funzionare a vita. Una futura versione maggiore (Commandeck 2) sarebbe un acquisto a parte; tutto ciò che hai comprato resta tuo.

[Acquista una licenza →](https://neurocontrarian.lemonsqueezy.com/checkout/buy/9c16845a-8ab6-4a36-b8da-9874d9d64f33){ .md-button .md-button--primary }

## Prova gratuita di 14 giorni

La versione Pro include una **prova di 14 giorni** che parte da sola al primo avvio. Nessuna chiave, nessun pagamento e nessuna email da lasciare: tutte le funzioni Pro sono subito disponibili.

Qualche giorno prima della fine della prova, Commandeck mostra un'offerta dentro l'applicazione con un codice sconto. Dopo il quattordicesimo giorno le funzioni Pro diventano di sola lettura (in grigio): i tuoi pulsanti, le tue macchine e le tue impostazioni **non vengono mai cancellati**.

Per continuare a usare Pro, attiva una licenza da **Preferenze → Licenza**.

## Attivare la licenza

1. Apri le **Preferenze** (`Ctrl+,`)
2. Scendi fino alla sezione **Licenza**
3. Scrivi l'indirizzo email usato per l'acquisto
4. Incolla la tua chiave di licenza
5. Premi **Attiva Pro**

La connessione a internet serve solo per l'attivazione iniziale. Dopo, Commandeck funziona benissimo offline: l'uso quotidiano non ha bisogno di rete. Quando capita di essere online, ricontrolla la licenza ogni tanto in secondo piano; quando sei offline, resta semplicemente attiva.

## Disattivare

Per togliere la licenza da un dispositivo: **Preferenze → Licenza → Disattiva la licenza**.

Così liberi un posto di attivazione e puoi usare la stessa chiave su un altro dispositivo. La tua licenza Pro consente fino a **3 attivazioni contemporanee su computer** (Linux, macOS, Windows) che usi personalmente; vedi [Licenza e dispositivi](pro/license-devices.md) per i dettagli.

!!! note "Android è un prodotto a parte"
    La licenza desktop copre **solo il desktop** (Linux, macOS, Windows). L'app Android è un prodotto separato, disponibile su Google Play con la propria fatturazione, e non è coperta dalla chiave desktop.

I limiti della versione gratuita valgono subito dopo la disattivazione. I tuoi pulsanti non vengono cancellati; le funzioni Pro tornano appena riattivi.

## Profili di esecuzione *(Pro)*

Crea contesti di esecuzione riutilizzabili che uniscono un utente di destinazione, una cartella di lavoro e una password di sudo in un unico profilo con un nome.

Assegna un profilo a qualsiasi pulsante: quando parte, il comando viene eseguito con l'utente indicato nella cartella indicata, con la password di sudo fornita automaticamente (senza che nessun terminale la chieda).

I profili valgono sia per l'esecuzione locale sia per quella remota (SSH), inclusa la modalità **Apri nel terminale**.

Gestisci i profili dal menu → **Gestisci profili**.

---

## Backup e ripristino *(Pro)*

Esporta e importa tutta la tua configurazione dalle **Preferenze**:

- **Backup dei pulsanti**: esporta i tuoi pulsanti in un file `.cdbackup` (solo i pulsanti)
- **Backup delle macchine**: esporta le definizioni delle macchine SSH in un file `.cdmachines` (le chiavi private SSH non sono mai incluse)

Il ripristino sta nella stessa sezione delle Preferenze. Importando i pulsanti, questi si fondono con quelli predefiniti già presenti: i predefiniti aggiunti di recente non vanno mai persi.

---

## Integrazione con l'IA *(Pro)*

Il server MCP permette ad assistenti IA come Claude, Cursor o Open WebUI di leggere, modificare ed eseguire i tuoi pulsanti attraverso un'unica connessione sicura. Vedi [Integrazione IA (MCP)](pro/mcp.md) per la configurazione completa e i dettagli di sicurezza.
