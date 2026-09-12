# Attivare la licenza

Benvenuto in Commandeck Pro! Questa guida ti accompagna nella prima attivazione della licenza.

!!! tip "Che cosa ti serve"
    - La tua **chiave di licenza** (arrivata nell'email di acquisto di LemonSqueezy)
    - L'**indirizzo email** usato al momento dell'acquisto
    - Una **connessione a internet** (solo per la prima attivazione)

---

## Scaricare e installare

L'email di acquisto di LemonSqueezy contiene un link **Files** e un pulsante di download. Puoi anche prendere la versione più recente quando vuoi dalla [pagina dei rilasci](https://github.com/neurocontrarian/commandeck/releases/latest): Linux, macOS e Windows sono tutti lì. Scegli il file del tuo sistema e segui la scheda corrispondente.

=== "Linux"
    Scarica `Commandeck-Pro-…-x86_64.AppImage` (oppure il file `-ARM64` se sei su un Raspberry Pi o un'altra macchina ARM).

    **Il modo facile, senza terminale:** clic destro sul file scaricato → **Proprietà** → scheda **Permessi** → spunta **«Consenti l'esecuzione del file come programma»** (su alcuni desktop si chiama **«È eseguibile»**). Chiudi la finestra e fai **doppio clic** sul file per avviare Commandeck.

    Preferisci il terminale? La stessa cosa in una riga:
    ```bash
    chmod +x Commandeck-Pro-*.AppImage && ./Commandeck-Pro-*.AppImage
    ```

    !!! info "Se non parte"
        L'AppImage è autonomo: Python, Qt e tutte le librerie SSH (Paramiko,
        cryptography…) sono già dentro, quindi non c'è nessun `pip install` da fare. Se la
        tua distribuzione segnala che manca il plugin di piattaforma Qt, installa
        `libxcb-cursor0`:
        ```bash
        sudo apt install libxcb-cursor0     # Ubuntu / Mint / Debian
        sudo dnf install xcb-util-cursor    # Fedora
        ```

=== "macOS"
    Apri il `.dmg` scaricato e trascina l'icona di **Commandeck** nella cartella **Applicazioni** che compare di fianco.

    **Solo la prima volta**, apri Commandeck da Applicazioni con **clic destro → Apri → Apri**. Così si toglie l'avviso «sviluppatore non identificato» che macOS mostra una volta per le app installate fuori dall'App Store. Dopo, aprilo normalmente.

=== "Windows"
    Avvia l'installer `.exe` scaricato e segui i passaggi.

    Se SmartScreen mostra il riquadro blu **«Windows ha protetto il PC»**, premi **Ulteriori informazioni → Esegui comunque**. Compare con le applicazioni nuove che Microsoft non ha ancora visto scaricare molte volte: è normale per una versione appena pubblicata.

---

## Attivazione passo per passo

1. **Apri Commandeck** e assicurati di usare la **versione Pro**, non quella gratuita. ([Qual è la differenza?](../pro.md#free-vs-pro))

2. **Apri le Preferenze** con `Ctrl + ,` oppure dal menu → *Preferenze*.

3. **Scendi fino alla sezione *Licenza*.**

    ![Sezione Licenza nelle Preferenze](../assets/license-section.png)

4. **Incolla la tua chiave di licenza** nel campo *Chiave di licenza*.

5. **Scrivi l'email** usata per l'acquisto nel campo *Email*.

    !!! warning "L'email deve coincidere esattamente"
        Confrontiamo quello che scrivi con l'email che LemonSqueezy ha registrato per l'acquisto. Se non coincide, l'attivazione viene rifiutata e non viene consumato nessun posto.

6. Premi **Attiva Pro**.

7. In pochi secondi la finestra si aggiorna e mostra:
    - Il **tipo** di licenza
    - Il tuo **numero di attivazioni** (per esempio *1 / 3*)

Ecco fatto: tutte le funzioni Pro sono sbloccate. Macchine SSH, pulsanti multi-macchina, temi, backup, server MCP, tutto disponibile.

---

## Che cosa succede dopo

| Quando | Che cosa succede |
|---|---|
| Subito dopo l'attivazione | Tutte le funzioni Pro si sbloccano all'istante |
| Circa una volta al mese, all'avvio | Commandeck conferma in silenzio che la licenza è ancora attiva. Non c'è nulla da fare, ed essere offline non ti blocca mai fuori. |

I tuoi dati non sono mai a rischio. Pulsanti, macchine, impostazioni: tutto resta, qualunque cosa accada alla licenza.

---

## Risoluzione dei problemi

### *«Questa chiave di licenza è registrata con un'altra email.»*

L'email che hai scritto non corrisponde a quella dell'acquisto su LemonSqueezy. Controlla la ricevuta che ti ha mandato LemonSqueezy e usa esattamente quell'indirizzo (le maiuscole non contano, gli errori di battitura sì).

### *«Hai raggiunto il massimo di 3 attivazioni.»*

Hai usato tutti e 3 i posti di questa licenza. Apri Commandeck su uno dei dispositivi attivi, vai in **Preferenze → Licenza → Disattiva**, poi torna qui e attiva.

Hai perso l'accesso a un dispositivo che era attivato (portatile smarrito, sistema reinstallato senza disattivare)? [Scrivi all'assistenza](mailto:neurocontrarian@gmail.com) e lo risolviamo insieme.

Vedi la [guida completa su Licenza e dispositivi](license-devices.md) per tutti i casi.

### *«Errore di rete: impossibile contattare il server delle licenze.»*

La prima attivazione **richiede** una connessione a internet (verifichiamo la chiave su LemonSqueezy). Assicurati che Commandeck possa raggiungere `api.lemonsqueezy.com`: i proxy aziendali e i firewall severi possono bloccarlo.

Dopo la prima attivazione, Commandeck funziona **offline a tempo indeterminato**: restare senza connessione non ti blocca mai fuori. Ricontrolla la licenza solo **circa una volta al mese**, all'avvio, e se quel controllo non raggiunge internet viene semplicemente saltato fino alla volta successiva.

### *Non vedo nessuna sezione «Licenza» nelle Preferenze*

Stai usando la **versione gratuita**, che non ha un sistema di licenze: non c'è nulla da attivare. Per usare Pro, [scarica la versione Pro](../pro.md#download) e avvia quella. I tuoi pulsanti, le macchine e le impostazioni vengono ripresi automaticamente (stessa cartella di configurazione).

---

## Dove andare adesso

- **[Aggiungi la tua prima macchina SSH](../reference/ssh-machines.md)**: la funzione Pro da cui quasi tutti cominciano
- **[Crea un pulsante multi-macchina](../reference/ssh-machines.md#assigning-machines-to-a-button)**: un comando per un intero parco
- **[Licenza e dispositivi](license-devices.md)**: tutto sul limite dei 3 dispositivi, le reinstallazioni e i trasferimenti
- **[Politica di rimborso](../legal/refund.md)**: la garanzia di 14 giorni e che cosa copre

Ti serve altro? [Scrivi all'assistenza](mailto:neurocontrarian@gmail.com): leggiamo ogni messaggio.
