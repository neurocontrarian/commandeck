# Profili di esecuzione

!!! tip "Funzione Pro"
    I profili di esecuzione richiedono [Commandeck Pro](../pro.md).

🔰 **In parole semplici:** un profilo è un piccolo insieme di «condizioni di esecuzione» che salvi una volta e riutilizzi su molti pulsanti: *chi* esegue il comando (un altro utente) e *dove* viene eseguito (una cartella). Invece di scrivere `sudo -u www-data` e `cd /var/www` in ogni pulsante, li imposti una volta in un profilo e scegli quel profilo sul pulsante.

![Elenco dei profili di esecuzione](../assets/profiles-list.png)

## Creare un profilo

Apri **Menu ☰ → Profili di esecuzione → Aggiungi**, poi compila:

![Editor dei profili](../assets/profile-dialog.png)

| Campo | A che cosa serve |
|-------|------------------|
| **Nome** | Come compare il profilo nel menu a tendina dell'editor dei pulsanti. |
| **Esegui come utente** | Esegue il comando con quell'utente al posto del tuo (usa `sudo -u <utente>`). Lascialo vuoto per eseguirlo tu. |
| **Cartella di lavoro** | La cartella in cui il comando parte (come se ci facessi `cd` prima). |
| **Descrizione** | Nota facoltativa per ricordarti a che cosa serve il profilo. |
| **Password di sudo** | Facoltativa. Serve solo quando *Esegui come utente* richiede una password. Viene salvata in locale, cifrata; vedi [Sicurezza](security.md). |

## Usare un profilo su un pulsante

Nell'[editor dei pulsanti](button-editor.md), scegli il tuo profilo dal menu **Profilo di esecuzione**. Il pulsante viene ora eseguito con l'utente e la cartella di quel profilo, e il campo del comando resta pulito, con dentro soltanto il comando vero.

!!! example "Prima e dopo"
    Invece di un pulsante con `sudo -u www-data bash -c 'cd /var/www/app && git pull'`, crea:

    - un profilo **Deploy web** → *Esegui come utente* `www-data`, *Cartella di lavoro* `/var/www/app`
    - un pulsante con comando `git pull` e profilo **Deploy web**

    Più pulito, e lo stesso profilo vale per tutti i pulsanti di quell'applicazione web.

!!! example "Spegnere una macchina remota, il caso classico"
    Usato via SSH (per esempio dal telefono), il pulsante **Spegni** predefinito fallisce con un messaggio sull'autenticazione. Il comando è giusto: spegnere una macchina richiede **permessi di amministratore**, e una connessione remota non li riceve da sola come quando sei seduto davanti al computer. (Sulla tua scrivania lo stesso pulsante funziona senza problemi.) Con **Riavvia** vale lo stesso.

    La soluzione è un profilo, non un comando diverso:

    - crea un profilo **Alimentazione (admin)** → *Esegui come utente* `root`, e inserisci la **Password di sudo** di quella macchina (la tua password su di essa)
    - assegnalo a **Spegni** (e a **Riavvia**), senza toccare il comando

    Il pulsante viene ora eseguito con i permessi di amministratore e spegne la macchina in modo pulito. Quello stesso profilo ti servirà poi per qualsiasi cosa richieda permessi di amministratore su una macchina remota: riavviare un servizio, installare programmi, montare un disco.

⚙️ **Per gli amministratori di sistema**

- *Esegui come utente* avvolge il comando con `sudo -u <utente>`. Se quella destinazione richiede una password, compila la **Password di sudo** del profilo; Commandeck la passa con `sudo -S` al momento, quindi non compare nessuna richiesta in un terminale.
- Un profilo si applica **allo stesso modo** in locale e via SSH: l'involucro `sudo -u` e la cartella di lavoro valgono sulla macchina verso cui punta il pulsante.
- I profili si sposano bene con i [pulsanti multi-macchina](../use-cases/homelab.md): un profilo di deploy, un pulsante, più server.
- Un assistente IA può creare e assegnare i profili al posto tuo tramite il [server MCP](../pro/mcp.md): scompone automaticamente una riga di comando incollata in un profilo più un comando pulito.
