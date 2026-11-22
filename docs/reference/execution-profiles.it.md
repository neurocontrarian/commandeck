# «Esegui come» salvati

!!! tip "Funzione Pro"
    Gli «Esegui come» salvati richiedono [Commandeck Pro](../pro.md).

🔰 **In parole semplici:** un «Esegui come» salvato (chiamato anche profilo) è un piccolo insieme di «condizioni di esecuzione» che salvi una volta e riutilizzi su molti pulsanti: *chi* esegue il comando (un altro utente) e *dove* viene eseguito (una cartella). Invece di scrivere `sudo -u www-data` e `cd /var/www` in ogni pulsante, li imposti una volta e li scegli sul pulsante.

Un profilo **non contiene nessuna password**. Per agire come un altro utente, `sudo` chiede la password dell'account con cui sei *connesso*: per questo quella password sta nella [scheda della macchina](ssh-machines.md#password-di-amministratore) (o in [Preferenze › Questo computer](preferences.md#questo-computer) per questo computer), e uno stesso profilo vale su tutte le macchine.

![Elenco degli «Esegui come» salvati](../assets/profiles-list.png)

## Creare un profilo

Apri **Menu ☰ → «Esegui come» salvati → Aggiungi profilo**, poi compila:

![Editor dei profili](../assets/profile-dialog.png)

| Campo | A che cosa serve |
|-------|------------------|
| **Nome** | Come compare il profilo nell'elenco **Esegui come** dell'editor dei pulsanti (come «Salvato: …»). |
| **Esegui come utente** | Esegue il comando con quell'utente al posto del tuo (usa `sudo -u <utente>`). Lascialo vuoto per eseguirlo tu. |
| **Cartella di lavoro** | La cartella in cui il comando parte (come se ci facessi `cd` prima). |
| **Descrizione** | Nota facoltativa per ricordarti a che cosa serve il profilo. |

## Usare un profilo su un pulsante

Nell'[editor dei pulsanti](button-editor.md), scegli il tuo profilo nell'elenco **Esegui come**: compare come **Salvato: *nome***. Il pulsante viene ora eseguito con l'utente e la cartella di quel profilo, e il campo del comando resta pulito, con dentro soltanto il comando vero.

!!! example "Prima e dopo"
    Invece di un pulsante con `sudo -u www-data bash -c 'cd /var/www/app && git pull'`, crea:

    - un profilo **Deploy web** → *Esegui come utente* `www-data`, *Cartella di lavoro* `/var/www/app`
    - un pulsante con comando `git pull` e profilo **Deploy web**

    Più pulito, e lo stesso profilo vale per tutti i pulsanti di quell'applicazione web.

!!! example "Spegnere una macchina remota, il caso classico"
    Usato via SSH (per esempio dal telefono), il pulsante **Spegni** predefinito fallisce con un messaggio sull'autenticazione. Il comando è giusto: spegnere una macchina richiede **permessi di amministratore**, e una connessione remota non li riceve da sola come quando sei seduto davanti al computer. (Sulla tua scrivania lo stesso pulsante funziona senza problemi.) Con **Riavvia** vale lo stesso.

    La soluzione sta nella **scheda della macchina**, non nel pulsante:

    - se ti colleghi con **password**, lascia spuntato **È anche la password di amministratore (sudo)**: non c'è altro da fare;
    - se ti colleghi con **chiave SSH**, scrivi la tua password su quella macchina in **Password admin**.

    Quando un pulsante fallisce per mancanza di permessi di amministratore, Commandeck lo riesegue una volta come amministratore con quella password, senza profilo e senza toccare il comando. Vale per qualsiasi cosa richieda permessi di amministratore su quella macchina: riavviare un servizio, installare programmi, montare un disco. **Test** nella scheda della macchina ti dice se i permessi di amministratore funzionano.

⚙️ **Per gli amministratori di sistema**

- *Esegui come utente* avvolge il comando con `sudo -u <utente>`. sudo autentica l'account **connesso**: Commandeck gli risponde con la password admin della scheda della macchina (o di Questo computer), passata dall'input standard (`sudo -S`), mai sulla riga di comando, e il comando parte con l'input vuoto.
- Un profilo si applica **allo stesso modo** in locale e via SSH: l'involucro `sudo -u` e la cartella di lavoro valgono sulla macchina verso cui punta il pulsante.
- I profili si sposano bene con i [pulsanti multi-macchina](../use-cases/homelab.md): un profilo di deploy, un pulsante, più server.
- Un assistente IA può creare e assegnare i profili al posto tuo tramite il [server MCP](../pro/mcp.md): scompone automaticamente una riga di comando incollata in un profilo più un comando pulito.
