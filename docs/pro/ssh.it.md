# SSH e multi-macchina

!!! tip "Funzione Pro"
    Le macchine SSH e i pulsanti multi-macchina richiedono [Commandeck Pro](../pro.md).

Questa pagina copre il flusso di lavoro proprio di Pro per l'SSH: aggiungere macchine, assegnarle ai pulsanti e usare il selettore di macchina. Per il riferimento campo per campo della finestra di aggiunta, vedi [Macchine SSH](../reference/ssh-machines.md).

---

## Aggiungere la prima macchina

1. Apri **Menu → Gestisci macchine**
2. Premi **+** per aprire la finestra di aggiunta
3. Inserisci nome, host, utente SSH e il metodo di autenticazione: una **chiave** SSH (consigliata) o una **password**
4. Premi **Prova** per verificare la connessione
5. Premi **Salva**

La macchina è ora disponibile in ogni editor di pulsanti.

!!! note "Chiave o password"
    Le macchine SSH si autenticano con una **chiave** (consigliata) o con una **password**. Una password salvata vive nel portachiavi del tuo sistema, mai in chiaro e mai in un backup. Vedi [Password SSH](../reference/ssh-machines.md#ssh-password).

Per preparare una chiave SSH (generare la coppia e copiarla sul server), vedi [Preparare la chiave SSH](../reference/ssh-machines.md#ssh-key-setup).

---

## Assegnare una macchina a un pulsante

Apri l'editor dei pulsanti (creane uno nuovo oppure clic destro su uno esistente → **Modifica**).

Nella sezione **Macchine di destinazione**:

- Disattiva **Locale** se vuoi solo la macchina remota
- Attiva la macchina o le macchine che ti servono

Premi **Salva**. Il suggerimento del pulsante mostra ora il nome della macchina di destinazione.

---

## Pulsanti a macchina singola

Quando è attiva esattamente una destinazione, il comando parte subito lì: nessun selettore, nessun clic in più. È la configurazione più comune.

---

## Pulsanti multi-macchina

Attiva due o più destinazioni e il pulsante diventa multi-macchina. Ogni clic apre il [selettore di macchina](../reference/ssh-machines.md#the-machine-picker).

Il selettore elenca ogni destinazione attiva con nome e icona. Scegline una e premi **Esegui**.

![Selettore di macchina](../assets/machine-picker.png)

### Mescolare locale e remoto

Attiva **Locale** insieme a una o più macchine SSH per includere il tuo computer tra le scelte del selettore. Utile per script che funzionano allo stesso modo nei due ambienti.

### La scorciatoia «Tutte le macchine»

Nell'editor dei pulsanti, l'interruttore **Tutte le macchine** in cima all'elenco seleziona in un colpo solo tutte le macchine configurate. Comodo quando vuoi un comando come `df -h` disponibile su tutto il parco senza spuntare casella per casella.

---

## Schemi pratici

### Lo stesso comando su più server

Crea un pulsante con tutte le macchine di destinazione attive. Il selettore ti lascia scegliere ogni volta a quale server chiedere.

### Comandi in parallelo su più server

Il selettore di macchina consente la selezione multipla: spuntane diverse e Commandeck esegue il comando su tutte insieme. I risultati si aprono in **un'unica finestra con un selettore di macchina** (◀ ▶) per passare dall'output di una a quello dell'altra, con uno stato ✓ / ✗ per ciascuna.

### Alternare locale e remoto

Un pulsante con Locale e un server entrambi attivi è utile per provare: esegui prima il comando in locale per verificare che funzioni, poi scegli il server per la distribuzione.

---

## Modalità di output

Tutte e tre le modalità di esecuzione funzionano via SSH. Per le sessioni SSH interattive usa **Apri nel terminale**: Commandeck genera da solo la giusta invocazione `ssh -t`.

Vedi [Modalità di output via SSH](../reference/ssh-machines.md#output-modes-over-ssh) per il confronto completo.
