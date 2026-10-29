# Caso d'uso: guida per principianti a Linux

Hai appena installato Commandeck e non sai bene da dove cominciare. Questa guida è per te. Non serve conoscere nessun comando: Commandeck porta già con sé decine di pulsanti pronti all'uso.

---

## Hai già 29 pulsanti

Al primo avvio, Commandeck riempie la griglia con tre categorie di pulsanti già pronti:

- **Hardware** (13 pulsanti): disco, memoria, CPU, temperatura, scheda video e strumenti per lo spazio
- **Essenziali di Linux** (12 pulsanti): informazioni di sistema, utenti, log, aggiornamenti e manutenzione di base
- **Rete** (4 pulsanti): interfacce, connessioni, porte e servizi in ascolto

Questi pulsanti funzionano già. Non c'è nulla da configurare.

Ne vuoi altri? Gli strumenti di **Sviluppo** (git, Docker, Python, Node) e altri insiemi sono disponibili come [pacchetti di pulsanti](../packs.md) gratuiti, con un tocco. Apri il menu → **Pacchetti di pulsanti** per sfogliarli e installarli.

---

## Che cosa fa ogni pulsante predefinito

### Hardware

| Pulsante | Che cosa mostra |
|----------|-----------------|
| **Uso del disco** | Quanto è piena ogni partizione (`df -h`) |
| **Uso della memoria** | Consumo di RAM e di swap (`free -h`) |
| **Carico della CPU** | Il carico attuale e i processi più esigenti |
| **Temperatura** | Temperature di CPU e sensori, se `lm-sensors` è installato |
| **Dispositivi a blocchi** | Dischi fissi, chiavette USB e partizioni (`lsblk`) |
| **Cartelle più grandi** | Le cartelle più voluminose sotto `/` |
| **GPU NVIDIA** | Stato della scheda NVIDIA (`nvidia-smi`) |
| **GPU AMD** | Rilevamento, attività e temperatura della scheda AMD |
| **NCDU** | Esploratore interattivo dello spazio su disco (propone di installare `ncdu` se manca) |
| **btop** | Monitor di sistema in tempo reale (propone di installare `btop` se manca) |
| **Impostazioni NVIDIA** | Apre il pannello di controllo NVIDIA |
| **Informazioni hardware** | Rapporto completo sull'hardware: CPU, memoria, dispositivi |
| **I/O del disco** | Statistiche di lettura e scrittura sul disco |

### Essenziali di Linux

| Pulsante | Che cosa mostra |
|----------|-----------------|
| **Processi attivi** | Tutti i processi, ordinati per uso della CPU |
| **Informazioni di sistema** | Versione del kernel e distribuzione Linux |
| **Utenti collegati** | Chi è collegato in questo momento (`w`) |
| **Ultimi accessi** | Cronologia degli accessi |
| **Servizi in errore** | Servizi caduti o che non sono partiti |
| **Giornale di sistema** | Ultime 50 righe del log di sistema |
| **Messaggi del kernel** | Messaggi dell'hardware e dei driver |
| **Svuota il cestino** | Svuota la tua cartella cestino |
| **Aggiorna il sistema** | Aggiorna il sistema (funziona su Ubuntu, Fedora e Arch) |
| **Riavvia** | Riavvia il computer |
| **Spegni** | Spegne il computer |
| **Leggi il syslog** | Ultime 50 righe del log di sistema |

!!! warning
    **Riavvia** e **Spegni** hanno attiva l'opzione **Chiedi conferma prima di eseguire**: comparirà una finestra che ti chiede conferma prima che accada qualcosa.

### Rete

| Pulsante | Che cosa mostra |
|----------|-----------------|
| **Interfacce di rete** | I tuoi indirizzi IP e le schede di rete (`ip addr`) |
| **Connessioni attive** | Connessioni TCP stabilite |
| **Porte aperte** | Servizi in ascolto sulla tua macchina |
| **Servizi in ascolto** | Servizi in ascolto su porte TCP |

---

## Comincia premendo qualcosa

Premi **Uso del disco**. Si apre una piccola finestra con le informazioni sui tuoi dischi. Premi **Uso della memoria**. Provane qualcun altro.

Premendo questi pulsanti non puoi rompere nulla: si limitano a leggere informazioni. I due che fanno davvero qualcosa (Riavvia e Spegni) chiedono conferma prima.

---

## Fare spazio: disinstallare un pacchetto o nascondere una categoria

I pulsanti predefiniti arrivano sotto forma di **pacchetti di pulsanti**. Se un intero insieme non ti serve, la via più pulita è **disinstallare il pacchetto**: apri il menu → **Pacchetti di pulsanti**, cercalo e premi **Disinstalla**. I suoi pulsanti spariscono, e puoi reinstallare il pacchetto quando vuoi con un tocco.

Se invece preferisci solo togliere una categoria dalla vista senza rimuovere nulla, puoi nasconderla:

1. Apri **Preferenze → Categorie**
2. Disattiva la categoria

Una categoria nascosta e i suoi pulsanti non si vedono più, ma non sono cancellati: puoi riportarli indietro dallo stesso posto quando vuoi.

---

## Cambiare il nome o il colore di un pulsante

I nomi predefiniti sono funzionali ma generici. Puoi rinominarli o cambiarne il colore come preferisci, ed è **gratis per tutti**, senza bisogno di Pro.

Clic destro su un pulsante qualsiasi → **Modifica**:

- Cambia l'**Etichetta** con qualcosa di più familiare (`Uso del disco` → `Quanto è pieno il disco?`)
- Scegli un **Colore** per far risaltare i pulsanti importanti
- Cambia l'**Icona** con una che ti dica qualcosa

---

## Crea il tuo primo pulsante

I pulsanti personalizzati sono **gratuiti e illimitati**. Eccone uno facile per cominciare:

1. Premi `Ctrl+N` (oppure il **+**)
2. **Etichetta:** `Il mio indirizzo IP`
3. **Comando:** `hostname -I`
4. **Modalità di esecuzione:** `Mostra l'output`
5. Premi **Salva**

Ora hai un modo per vedere il tuo IP locale con un clic.

---

## E se un pulsante dà errore?

Alcuni pulsanti hanno bisogno di programmi che potrebbero non essere installati:

- **Temperatura** richiede `lm-sensors` (`sudo apt install lm-sensors`)
- **NCDU** e **btop** propongono di installarsi da soli la prima volta che li usi
- Se installi il pacchetto **Sviluppo**, i suoi pulsanti Docker, Python e Node richiedono quegli strumenti installati

Se un comando fallisce si apre una finestra con l'errore esatto. Di solito è un pacchetto mancante: copia il nome e installalo.

---

## Sfruttare meglio Commandeck

Quando ti sarai trovato a tuo agio con i pulsanti predefiniti:

- [Crea pulsanti su misura](../quick-start.md#3-create-your-first-custom-button) per i tuoi comandi più frequenti
- [Fai ordine con le categorie](../reference/main-window.md#category-filter) per raggruppare i pulsanti affini
- [Regola la griglia](../reference/preferences.md#button-grid-layout) in base al tuo schermo
- Valuta [Commandeck Pro](../pro.md) quando vorrai gestire un server remoto
