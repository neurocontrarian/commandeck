# Temi dei pulsanti

!!! tip "Funzione Pro"
    I temi dei pulsanti richiedono [Commandeck Pro](../pro.md). La versione gratuita resta sul tema **Bold**.

I temi dei pulsanti cambiano lo stile visivo di tutte le caselle della griglia. Scegline uno in **Preferenze → Aspetto dei pulsanti → Tema dei pulsanti**.

---

## Temi disponibili

I temi sono sei. **Bold** e **Neon** conservano il colore proprio di ogni pulsante; **Cards**, **Phone keys**, **Retro** e **Tron** applicano uno stile uniforme e ignorano i colori dei singoli pulsanti.

### Bold (predefinito)

Caselle a tinta piena con molto contrasto: il colore di sfondo di ogni pulsante come riempimento uniforme e testo bianco in grassetto. È lo stile predefinito e funziona bene sia in modalità chiara sia in modalità scura.

![Tema Bold](../assets/theme-bold.png)

### Cards

Caselle chiare in stile scheda, con un bordo morbido nella tinta d'accento. Pulito e neutro: una buona scelta se i colori di Bold ti sembrano troppo forti.

![Tema Cards](../assets/theme-cards.png)

### Phone keys

Tasti compatti e arrotondati con un'ombra leggera, che ricordano la tastiera di un telefono o di una calcolatrice. Rende meglio con pulsanti di dimensione piccola o media.

![Tema Phone keys](../assets/theme-phone.png)

### Neon

Il colore proprio di ogni pulsante su fondo nero: bordo e alone luminosi in quel colore, con il testo ciano. Si ravviva al passaggio del mouse. Ottimo in modalità scura.

![Tema Neon](../assets/theme-neon.png)

!!! note
    L'alone di Neon si apprezza soprattutto in funzione: passando il mouse su un pulsante, il bordo si illumina.

### Tron

Caselle nere con contorni e testo ciano brillante, con un'aria da griglia luminosa. Ignora i colori dei singoli pulsanti: tutte le caselle condividono lo stesso stile neon su nero.

![Tema Tron](../assets/theme-tron.png)

### Retro

Monocromatico ambra con un bordo netto e spostato, ispirato ai vecchi terminali. Ignora i colori dei singoli pulsanti: tutte le caselle si assomigliano di proposito.

![Tema Retro](../assets/theme-retro.png)

---

## CSS personalizzato

!!! tip "Funzione Pro"
    Il CSS personalizzato richiede [Commandeck Pro](../pro.md).

Per un controllo visivo completo, carica il tuo foglio di stile. Indica il percorso in **Preferenze → Aspetto dei pulsanti → File CSS personalizzato → Sfoglia**. Commandeck usa i **fogli di stile di Qt (QSS)**: una sintassi simile al CSS, ma con i selettori propri di Qt e meno proprietà rispetto al CSS del web.

Quando viene caricato un foglio di stile personale, si applica sopra al tema scelto. Puoi combinare un tema di base con piccole modifiche oppure scrivere un tema intero da zero.

### Elementi su cui puoi agire

Un pulsante è un `QFrame` chiamato `ButtonTile` che contiene una `QLabel` chiamata `TileLabel`. I suoi stati (in esecuzione, riuscito, errore, selezionato) sono esposti come **proprietà dinamiche**, che si selezionano con `[proprietà="valore"]`:

```css
/* The tile container */
QFrame#ButtonTile {
  background: #1e1e2e;
  border-radius: 12px;
  border: 2px solid rgba(255, 255, 255, 0.15);
}

/* Hover state */
QFrame#ButtonTile:hover {
  border-color: rgba(137, 180, 250, 0.8);
}

/* Pressed state */
QFrame#ButtonTile:pressed {
  background: #181825;
}

/* The label text */
QFrame#ButtonTile QLabel#TileLabel {
  color: #cdd6f4;
  font-weight: bold;
  font-size: 13px;
}

/* Running state (command is executing) */
QFrame#ButtonTile[running="true"] {
  background: #313244;
}

/* Success flash */
QFrame#ButtonTile[success="true"] {
  border-color: #a6e3a1;
}

/* Failure flash */
QFrame#ButtonTile[error="true"] {
  border-color: #f38ba8;
}

/* Selected (multi-select) */
QFrame#ButtonTile[selected="true"] {
  border-color: #89b4fa;
}
```

Premi **Esporta modello** nelle Preferenze per scaricare un file di partenza con tutti i selettori disponibili e i loro valori predefiniti commentati.

!!! note
    I fogli di stile di Qt non sono il CSS del web: **non** esistono `transform`, `box-shadow`, le transizioni di `opacity`, l'unità `rem` né `max-width` / `max-height`. Usa colori pieni, bordi e `border-radius`; e indica le dimensioni in pixel.
