# Preferenze

Apri le Preferenze dal menu oppure con `Ctrl+,`.

Le impostazioni vengono salvate appena le cambi: non c'è nessun pulsante di salvataggio.

---

## Generale

![Preferenze — Generale](../assets/preferences-general.png)

### Lingua

Sceglie la lingua dell'interfaccia. Commandeck parla 12 lingue:

| Codice | Lingua |
|--------|--------|
| Sistema | Segue la lingua del tuo desktop (predefinito) |
| en | Inglese |
| fr | Francese |
| de | Tedesco |
| es | Spagnolo |
| it | Italiano |
| pt | Portoghese |
| ru | Russo |
| ko | Coreano |
| ja | Giapponese |
| zh | Cinese (semplificato) |
| ar | Arabo |
| hi | Hindi |

!!! note
    Il cambio di lingua ha effetto al riavvio di Commandeck. Un avviso a comparsa te lo ricorda.

### Tempo massimo di un comando

Il tempo massimo (in secondi) di attesa perché un comando finisca, prima di annullarlo. Predefinito: **30 secondi**.

Alzalo per i comandi che si sa che durano (copie di file grandi, aggiornamenti di sistema). Abbassalo per fallire in fretta con macchine irraggiungibili.

### Disposizione della griglia

Non esiste nessuna impostazione «pulsanti per riga»: la griglia si ridispone da sola secondo la larghezza della finestra. Ridimensiona la finestra per avere più o meno colonne (fino a una sola). Per cambiare la dimensione delle caselle, usa **Dimensione dei pulsanti** in [Aspetto dei pulsanti](#button-appearance).

### Chiedi conferma prima di eseguire, come impostazione predefinita

Quando è attivo, la casella **Chiedi conferma prima di eseguire** dell'editor dei pulsanti risulta già spuntata su ogni nuovo pulsante che crei.

Non tocca i pulsanti già esistenti.

---

## Aspetto dei pulsanti

![Preferenze — Aspetto dei pulsanti](../assets/preferences-appearance.png)

### Dimensione dei pulsanti

Fissa la dimensione di tutte le caselle insieme.

| Dimensione | Misure della casella | Dimensione dell'icona |
|------------|----------------------|-----------------------|
| Piccola | 80 × 80 px | 20 px |
| Media | 120 × 120 px | 32 px |
| Grande | 160 × 160 px | 48 px |

### Tema dei pulsanti

!!! tip "Funzione Pro"
    I temi dei pulsanti richiedono [Commandeck Pro](../pro.md). Nella versione gratuita resta fisso su **Bold** (lo stile predefinito).

Applica uno stile visivo a tutte le caselle. Vedi [Temi](../pro/themes.md) per una descrizione completa e le immagini di ogni opzione.

| Tema | Stile |
|------|-------|
| Bold | Caselle a tinta piena con molto contrasto (predefinito) |
| Phone | Caselle compatte e piatte, con un'aria da tastierino telefonico |
| Neon | Sfondo scuro con bordi luminosi colorati |
| Retro | Monocromatico ispirato ai vecchi terminali, con righe di scansione |

---

## Integrazione con il desktop

![Preferenze — Integrazione con il desktop](../assets/preferences-desktop.png)

### Sempre in primo piano

Quando è attivo, la finestra di Commandeck galleggia sopra tutte le altre.

- **Windows, macOS e Linux/X11**: funziona subito, senza dipendenze aggiuntive.
- **Linux/Wayland**: il protocollo Wayland non permette a un'applicazione di mettersi in primo piano da sola, quindi l'opzione compare disattivata con la sua spiegazione. (La maggior parte delle sessioni X11, compresa quella predefinita di Linux Mint, non è interessata.)

!!! tip "Tenere Commandeck in primo piano su Wayland"
    Anche quando l'opzione dell'applicazione è disattivata, puoi comunque fissare la finestra: **clic destro sulla barra del titolo della finestra e scegli _Sempre in primo piano_**. Lo offre il gestore delle finestre del tuo desktop, che ha il permesso di farlo. In alternativa, accedi a una sessione **X11 / «Xorg»** dalla schermata di login, dove l'opzione di Commandeck funziona normalmente.

Questa impostazione è anche nel menu, come interruttore rapido.

### Avvia all'accesso

Quando è attivo, Commandeck parte da solo quando accedi al tuo desktop. Questo scrive un file `.desktop` in `~/.config/autostart/commandeck.desktop`.

Disattivandolo, quel file viene rimosso.

### Terminale

Alcuni pulsanti aprono una **finestra di terminale** per strumenti interattivi (come `btop` o `ncdu`). Commandeck rileva il tuo terminale da solo, ma se la tua distribuzione ne porta uno insolito puoi sceglierlo qui.

- **Automatico (rileva)**: l'impostazione predefinita; Commandeck usa il primo terminale installato che riconosce e rispetta la variabile d'ambiente `$TERMINAL` se è impostata.
- **_(un terminale preciso)_**: l'elenco mostra i terminali trovati installati sul tuo sistema. Puoi anche scrivere il comando di un altro qualsiasi.

### Consenti l'accesso MCP

![Preferenze — interruttore dell'accesso MCP](../assets/preferences-mcp.png)

Attiva il server MCP (Model Context Protocol) integrato. Con quello in funzione, un assistente IA compatibile (Claude Desktop, Cursor e simili) può leggere e gestire i tuoi pulsanti.

Disattivato di fabbrica. Vedi [Integrazione IA (MCP)](../pro/mcp.md) per la configurazione.

!!! warning
    Con l'accesso MCP attivo, il tuo assistente IA può creare, modificare ed eliminare pulsanti. Disattivalo quando non lo stai usando.

---

## Categorie

![Preferenze — Categorie](../assets/preferences-categories.png)

Elenca tutte le categorie esistenti in questo momento nella tua configurazione dei pulsanti. Ogni riga ha un interruttore:

- **Attiva**: la categoria compare nel menu della barra in alto e i suoi pulsanti si vedono nella griglia
- **Disattivata**: la categoria e i suoi pulsanti spariscono dalla griglia (ma non vengono cancellati)

È il modo di far tornare una categoria dopo averla nascosta con clic destro → **Nascondi la categoria**.

L'elenco si aggiorna da solo man mano che aggiungi o togli categorie.

---

## Profili di esecuzione *(Pro)*

Gestisci i contesti di esecuzione con un nome dal menu → **Gestisci profili** (raggiungibile anche da questa sezione). Ogni profilo mette insieme:

- **Nome del profilo**: un'etichetta breve e descrittiva (per esempio `Come www-data in /var/www`)
- **Esegui come**: l'utente di destinazione: il tuo utente attuale (senza sudo), root oppure un nome utente preciso
- **Cartella di lavoro**: la cartella in cui entrare con `cd` prima di eseguire il comando
- **Password di sudo**: salvata in locale con una cifratura legata alla macchina; viene passata automaticamente a `sudo -S` al momento, così non compare nessuna richiesta in un terminale

Assegna un profilo a un pulsante nell'[editor dei pulsanti](button-editor.md#execution-profile) per applicarne le impostazioni.

!!! tip "Funzione Pro"
    I profili di esecuzione richiedono [Commandeck Pro](../pro.md).

---

## Licenza

![Preferenze — Licenza](../assets/preferences-license.png)

Gestisce la tua licenza di Commandeck Pro.

### Attivare

1. Acquista una licenza dalla [pagina di Commandeck Pro](../pro.md)
2. Incolla la tua chiave di licenza nel campo
3. Premi **Attiva Pro**

Per l'attivazione iniziale serve una connessione a internet.

### Dati della licenza attiva

Quando c'è una licenza valida attiva, questa sezione mostra:

- **Tipo di licenza**: Pro (acquisto unico)
- **Numero di attivazioni**: per esempio *1 / 3*
- **Stato**: attiva

### Disattivare

Premi **Disattiva la licenza** per togliere la licenza Pro da questo dispositivo. I limiti della versione gratuita valgono subito.

Non viene cancellato nulla. I tuoi pulsanti restano: quelli locali sono illimitati nella versione gratuita. Si bloccano solo le funzioni esclusive di Pro: le macchine SSH smettono di funzionare (i loro pulsanti restano ma non possono partire da remoto), i temi personalizzati tornano a quello predefinito, e backup, ripristino e server MCP non sono più disponibili.
