# Selezione multipla

!!! tip "Funzione Pro"
    La selezione multipla richiede [Commandeck Pro](../pro.md).

La selezione multipla permette di agire su più pulsanti insieme: cambiarli di categoria, riassegnare la macchina o cancellare un intero gruppo.

![Modalità di selezione multipla con pulsanti selezionati e barra delle azioni](../assets/multiselect.png)

---

## Quando serve

- Hai cambiato server e devi riassegnargli 10 pulsanti
- Vuoi spostare un intero insieme di pulsanti in un'altra categoria
- Hai creato un mucchio di pulsanti temporanei e vuoi cancellarli in blocco
- Hai duplicato diversi pulsanti e devi fare pulizia in fretta

---

## Iniziare una selezione

Non c'è nessuna «modalità selezione» da attivare. Basta cominciare a selezionare:

- **Ctrl+clic** su una casella per aggiungerla alla selezione o toglierla (un clic normale continua a eseguire il comando)
- **Trascina un rettangolo** su un'area vuota della griglia (vedi [Selezione con rettangolo](#rubber-band-selection)) per selezionare tutte le caselle che tocca

Appena un pulsante è selezionato, **una barra delle azioni sale dal basso** e mostra quanti pulsanti hai selezionato e quali azioni di gruppo sono disponibili.

---

## Selezionare i pulsanti

### Ctrl+clic per attivare e disattivare

**Ctrl+clic** su una casella qualsiasi la aggiunge alla selezione; un altro Ctrl+clic la toglie. Le caselle selezionate si evidenziano in blu. (Un clic sinistro normale, senza Ctrl, esegue il comando del pulsante.)

### Selezione con rettangolo

Fai clic e trascina su un'**area vuota** della griglia (non su un pulsante) per disegnare un rettangolo di selezione. Tutti i pulsanti toccati dal rettangolo entrano nella selezione corrente.

!!! tip
    Comincia il trascinamento dai margini della griglia: lo spazio fra le caselle o il bordo esterno. Se parti sopra un pulsante, quello che ottieni è attivare o disattivare quel pulsante invece di disegnare un rettangolo.

### Combinare i due metodi

Puoi mescolare Ctrl+clic e rettangolo liberamente. Prima marca singoli pulsanti con Ctrl+clic, poi aggiungi un gruppo con il rettangolo e infine togline qualcuno con Ctrl+clic.

---

## Azioni di gruppo

La barra in basso mostra le operazioni disponibili appena c'è almeno un pulsante selezionato.

### Elimina

Rimuove definitivamente tutti i pulsanti selezionati. Una finestra di conferma indica quanti sono («Eliminare 5 pulsanti?»). Non si può annullare.

I pulsanti predefiniti (Essenziali di Linux, Sviluppo) si possono eliminare anche nella versione gratuita.

### Categoria

Assegna una categoria a tutti i pulsanti selezionati. Una piccola finestra chiede il nome:

- Scrivi un nome nuovo per creare una categoria
- Scrivi il nome di una categoria esistente per spostarci i pulsanti
- Lascia vuoto e conferma per togliere loro la categoria (i pulsanti restano senza categoria)

### Macchina

Assegna una macchina SSH a tutti i pulsanti selezionati. Un selettore elenca le macchine configurate più **Locale**:

- Scegli una macchina → tutti i pulsanti selezionati puntano solo a quella macchina (le destinazioni precedenti vengono sostituite)
- Scegli **Locale** → tutti i pulsanti selezionati passano all'esecuzione locale

!!! note
    L'azione **Macchina** sostituisce la destinazione di ogni pulsante, non la aggiunge. Se vuoi pulsanti multi-macchina, modificali uno per uno nell'editor dei pulsanti.

---

## Annullare la selezione

Premi la **✕** sulla barra delle azioni per svuotare la selezione corrente. La barra si nasconde e la griglia torna normale. (Un clic normale su un pulsante qualsiasi esegue il suo comando in ogni momento: selezionare i pulsanti non intralcia mai l'uso quotidiano.)
