# Variabili di comando

Il comando di un pulsante può contenere dei **segnaposto** scritti come `{{chiave}}`. Quando premi il pulsante, Commandeck ti chiede ogni valore, lo inserisce e poi esegue il comando. Il valore vale **solo per quell'esecuzione**: non viene mai salvato.

Così un pacchetto condiviso resta generico (senza dati personali dentro): il pacchetto porta `docker restart {{container}}`, e ognuno scrive il nome del proprio container al momento dell'esecuzione.

## Come funziona

1. Un comando come `docker logs --tail {{lines}} {{container}}` ha due segnaposto.
2. Alla pressione, una piccola finestra chiede **Righe** e **Container**.
3. Scrivi `50` e `jellyfin` → Commandeck esegue `docker logs --tail 50 jellyfin`.
4. Non viene salvato nulla: la volta dopo lo chiede di nuovo.

Un segnaposto si scrive come `{{chiave}}` (lettere, cifre, trattino basso). Gli spazi interni non danno fastidio: anche `{{ container }}` funziona.

![La finestra che chiede i valori di un comando prima di eseguirlo](../assets/variable-prompt.png)

## Variabili standard

Queste chiavi hanno già un'etichetta e una domanda chiare. Riusale, così le persone ricevono sempre le stesse domande. L'elenco **cresce nel tempo**.

| Segnaposto | Chiede | Effetto sul comando |
|---|---|---|
| `{{container}}` | Nome di un container Docker | sostituisce `{{container}}` prima di eseguire |
| `{{service}}` | Nome di un servizio systemd | sostituisce `{{service}}` |
| `{{path}}` | Un percorso di file o cartella | sostituisce `{{path}}` |
| `{{host}}` | Un nome host o un indirizzo IP | sostituisce `{{host}}` |
| `{{port}}` | Un numero di porta | sostituisce `{{port}}` |
| `{{branch}}` | Un nome di ramo Git | sostituisce `{{branch}}` |
| `{{package}}` | Un nome di pacchetto | sostituisce `{{package}}` |
| `{{user}}` | Un nome utente | sostituisce `{{user}}` |
| `{{pid}}` | Un identificativo di processo | sostituisce `{{pid}}` |
| `{{lines}}` | Un numero di righe | sostituisce `{{lines}}` |
| `{{player}}` | Un nome di giocatore | sostituisce `{{player}}` |
| `{{message}}` | Un messaggio | sostituisce `{{message}}` |

## Altre variabili (scritte nel comando)

Puoi scrivere **qualsiasi** chiave direttamente in un comando, per esempio `{{regione}}`. Se non è una variabile standard, Commandeck te la chiede lo stesso all'esecuzione, con un normale campo di testo etichettato con il nome della chiave: così i pacchetti che usano chiavi proprie continuano a funzionare.

Attenzione: il gestore dei **Valori delle variabili** e il selettore **Inserisci variabile** elencano solo le variabili standard qui sopra; da lì non si possono creare chiavi nuove. Le chiavi personali vivono nel testo del comando.

## Valori salvati (più rapidi e più coerenti)

Puoi salvare un elenco di valori per ogni variabile in **Menu → Valori delle variabili** (per esempio `service` → `jellyfin`, `sonarr`). Allora:

- **Mentre crei un pulsante**, il pulsante **Inserisci variabile** (accanto al campo Comando) ti permette di inserire `{{service}}` (che verrà chiesto a ogni esecuzione) **oppure di scegliere un valore salvato per fissarlo** subito nel comando.
- **All'esecuzione**, una variabile con valori salvati mostra un **menu a tendina** con quei valori, e puoi comunque scriverne a mano un altro.

## Non mettere segreti in un comando

Non scrivere mai una password vera o una chiave API in un comando. Se un comando ne ha bisogno, usa un segnaposto (per esempio `{{token}}`) così viene digitata al momento dell'esecuzione e non viene salvata né condivisa in un pacchetto. I pacchetti inviati con un segreto scritto dentro vengono rifiutati automaticamente.
