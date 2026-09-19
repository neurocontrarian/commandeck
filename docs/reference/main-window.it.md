# Finestra principale

![Finestra principale di Commandeck](../assets/main-window.png)

La finestra principale ha tre zone: la **barra in alto**, la **barra di ricerca** e la **griglia dei pulsanti**.

---

## Barra in alto

La barra in alto è sempre visibile. Da sinistra a destra:

### + (Aggiungi pulsante)

Apre l'[editor dei pulsanti](button-editor.md) per crearne uno nuovo. Scorciatoia da tastiera: `Ctrl+N`.

!!! note
    I pulsanti personalizzati sono illimitati in tutte le versioni. [Commandeck Pro](../pro.md) aggiunge macchine SSH, temi e integrazione con l'IA.

### Icona di ricerca

Mostra o nasconde la barra di ricerca. Puoi anche iniziare a scrivere in un punto qualsiasi della finestra perché si apra da sola.

### Menu (≡)

![Menu aperto](../assets/main-window-menu.png)

Apre il menu dell'applicazione:

- **Ricarica i pulsanti** (`F5`): rilegge la griglia dal disco senza riavviare; utile dopo che un'IA (MCP) o un altro programma ha modificato i tuoi pulsanti
- **Preferenze**: apre la finestra delle preferenze (`Ctrl+,`)
- **Gestisci macchine**: apre l'elenco delle macchine (solo Pro)
- **Profili di esecuzione**: apre l'elenco dei profili di esecuzione (solo Pro)
- **Sempre in primo piano**: fa galleggiare la finestra sopra tutte le altre (resta spuntato quando è attivo)
- **Ripristina i valori predefiniti**: salva una copia dei tuoi pulsanti e risemina l'insieme predefinito
- **Mostra il registro di esecuzione**: apre il registro diagnostico che segue ogni clic
- **Informazioni**: versione e dati della licenza
- **Esci**: chiude Commandeck (`Ctrl+Q`)

---

## Filtro per categoria

Quando almeno un pulsante ha una categoria, nella barra in alto compare un **menu delle categorie**, accanto all'icona di ricerca. (Sparisce se nessun pulsante ha una categoria.)

- **Tutte**: l'impostazione predefinita, mostra tutti i pulsanti a prescindere dalla categoria.
- **_(nome della categoria)_**: scegli una categoria per vedere solo i suoi pulsanti.

Il menu mantiene la stessa dimensione compatta per quante categorie tu abbia, così la finestra può stringersi fino a una sola colonna di pulsanti.

Per nascondere del tutto una categoria — così non compare né nel menu né nella griglia — vai in **Preferenze → Categorie** e disattivala. I pulsanti non vengono cancellati.

---

## Barra di ricerca

La barra di ricerca compare sotto la barra in alto quando la attivi. Filtra i pulsanti in tempo reale in base alla loro etichetta. Il filtro si somma a quello di categoria eventualmente attivo.

Premi `Esc` o di nuovo l'icona di ricerca per chiuderla e togliere il filtro.

---

## Griglia dei pulsanti

L'area principale è una griglia di [caselle](#button-tiles) scorrevole. Non esiste nessuna impostazione «colonne»: la griglia si ridispone da sola secondo la larghezza della finestra. Allarga la finestra per avere più colonne, o stringila per averne meno (fino a una sola). Per cambiare la dimensione delle caselle, usa **Preferenze → Aspetto dei pulsanti → Dimensione dei pulsanti**.

Trascina un pulsante per cambiarne la posizione nella griglia.

### Caselle dei pulsanti

Ogni casella mostra:

- Un'**icona** (in alto o al centro, a seconda della dimensione)
- Un'**etichetta** (il nome del pulsante)

Lo sfondo della casella e il colore del testo si possono regolare pulsante per pulsante.

**Clic sinistro** su una casella per eseguire il comando. Se il pulsante ha attivo **Chiedi conferma prima di eseguire**, compare prima una finestra di conferma. Se il pulsante punta a più macchine, compare un [selettore di macchina](ssh-machines.md#the-machine-picker).

**Clic destro** su una casella per aprire il menu contestuale:

![Menu contestuale di un pulsante](../assets/button-context-menu.png)

- **Modifica**: apre l'editor di questo pulsante
- **Duplica**: crea una copia del pulsante
- **Sposta in una categoria**: scrivi o scegli il nome di una categoria per riassegnarlo
- **Elimina**: rimuove definitivamente il pulsante (con conferma)

!!! note
    I pulsanti predefiniti sono modificabili in tutto e da chiunque: rinominali, cambia loro colore, modificane il comando o eliminali, anche nella versione gratuita.

### Selezionare più pulsanti insieme

Non esiste nessun pulsante «modalità selezione». Per lavorare su più pulsanti insieme:

- **Ctrl+clic** sulle caselle per aggiungerle o toglierle dalla selezione, oppure
- **trascina un rettangolo** sulla griglia (clic su un'area vuota e trascina) per selezionare tutte le caselle che tocca.

Appena un pulsante è selezionato, **una barra delle azioni sale dal basso** e mostra quanti ne hai selezionati, con le azioni di gruppo: **Cambia categoria**, **Cambia macchina**, **Elimina** e **✕** per svuotare la selezione.

!!! tip "Funzione Pro"
    Selezionare più pulsanti insieme richiede [Commandeck Pro](../pro.md).

---

## Avvisi a comparsa

Dopo l'esecuzione di un comando, un piccolo avviso sale dal fondo della finestra:

- **Avviso di riuscita**: il comando è andato a buon fine
- **Avviso di errore**: il comando è fallito (codice di uscita diverso da zero)

Per i comandi in modalità **Mostra l'output**, o per qualsiasi comando che fallisca, si apre da sola una finestra con tutto il testo normale e quello di errore.

![Finestra di output con il risultato di un comando](../assets/output-dialog.png)

---

## Quando non c'è nulla da mostrare

Se nessun pulsante corrisponde alla ricerca o al filtro di categoria, compare un'illustrazione con un suggerimento. Non è un errore: vuol dire soltanto che tutti i pulsanti sono filtrati. Premi **Tutte** o cancella la ricerca per rivederli.

Se non hai nessun pulsante (cosa insolita dopo un'installazione nuova), quella schermata ti invita a crearne uno.
