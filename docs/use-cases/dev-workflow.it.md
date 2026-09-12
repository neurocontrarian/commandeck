# Caso d'uso: flusso di sviluppo

Questa guida mostra come usare Commandeck come tavolozza di comandi per chi programma. L'obiettivo: sostituire i comandi da terminale più ripetitivi con pulsanti da premere, organizzati per progetto.

!!! tip "Funzione Pro"
    Questo flusso esegue comandi su un server remoto via SSH. **Le macchine SSH, i pulsanti multi-macchina e i profili di esecuzione richiedono [Commandeck Pro](../pro.md).** I pulsanti puramente locali di questa guida funzionano nella versione gratuita.

## Lo scenario

Lavori su due progetti:

- Un **frontend** (applicazione React, in locale)
- Un'**API di backend** (Node.js, distribuita su un server remoto)

Esegui gli stessi comandi decine di volte al giorno: compilare, testare, distribuire, leggere i log. Commandeck sostituisce la memoria delle dita con pulsanti visibili ed etichettati.

---

## Passo 1 — Aggiungi il server come macchina SSH

Per i comandi che girano sul server, aggiungilo per primo:

| Campo | Valore |
|-------|--------|
| Nome | `Server di produzione` |
| Host | `ip-del-tuo-server` |
| Utente SSH | `deploy` |
| Percorso della chiave SSH | `~/.ssh/id_ed25519` |

Premi **Prova** per verificare il collegamento.

!!! tip "Funzione Pro"
    Le macchine SSH richiedono [Commandeck Pro](../pro.md).

---

## Passo 2 — Categoria «Frontend»

Crea questi pulsanti con **Categoria: Frontend**.

### Installare le dipendenze

```
npm install
```

- Modalità di esecuzione: **Mostra l'output** (per vedere se qualcosa fallisce)
- Suggerimento sulla cartella di lavoro: anteponi `cd ~/progetti/miaapp &&`

Comando completo: `cd ~/progetti/miaapp && npm install`

---

### Avviare il server di sviluppo

```
cd ~/progetti/miaapp && npm run dev
```

- Modalità di esecuzione: **Apri nel terminale** — il server di sviluppo è interattivo e scrive di continuo

---

### Compilare per la produzione

```
cd ~/progetti/miaapp && npm run build
```

- Modalità di esecuzione: **Mostra l'output** — vuoi vedere gli errori di compilazione
- Icona: `package-x-generic-symbolic`

---

### Lanciare i test

```
cd ~/progetti/miaapp && npm test -- --watchAll=false
```

- Modalità di esecuzione: **Mostra l'output**
- Suggerimento: `Esegue una volta l'intera batteria di test`

---

### Analisi dello stile

```
cd ~/progetti/miaapp && npm run lint
```

- Modalità di esecuzione: **Mostra l'output**
- Colore: `#1c71d8` (blu: informativo)

---

## Passo 3 — Categoria «Backend»

Crea questi pulsanti con **Categoria: Backend** e destinazione `Server di produzione`.

### Scaricare il codice più recente

```
cd ~/app && git pull origin main
```

- Modalità di esecuzione: **Mostra l'output**
- Chiedi conferma prima di eseguire: attivo (evita distribuzioni accidentali)

---

### Riavviare l'API

```
sudo systemctl restart miaapp
```

- Modalità di esecuzione: **Silenzioso**
- Chiedi conferma prima di eseguire: attivo

---

### Docker: ricostruire e riavviare

```
cd ~/app && docker compose down && docker compose up -d --build
```

- Modalità di esecuzione: **Mostra l'output**
- Suggerimento: `Ricostruisce i container e riavvia (circa 30 s)`
- Colore: `#26a269` (verde: azione di distribuzione)

---

### Seguire i log dell'applicazione

```
sudo journalctl -u miaapp -f -n 100
```

- Modalità di esecuzione: **Apri nel terminale** — `journalctl -f` scrive all'infinito

---

### Vedere i container Docker

```
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

- Modalità di esecuzione: **Mostra l'output**

---

### Backup del database

```
cd ~/app && pg_dump miodb > ~/backup/miodb_$(date +%Y%m%d).sql
```

- Modalità di esecuzione: **Mostra l'output**
- Chiedi conferma prima di eseguire: attivo
- Suggerimento: `Scarica il database di produzione in ~/backup/`

---

## Passo 4 — Usa «Mostra l'output» con criterio

Non tutti i comandi hanno bisogno di **Mostra l'output**. Una buona regola:

| Usa **Silenzioso** per | Usa **Mostra l'output** per | Usa **Apri nel terminale** per |
|------------------------|-----------------------------|--------------------------------|
| Riavvii di servizi | Compilazioni e test | Processi interattivi (`htop`, `vim`, `psql`) |
| Comandi di semplice avvio | Comandi che possono fallire | Flussi lunghi (`tail -f`, `docker logs -f`) |
| Distribuzioni di cui ti fidi | Tutto ciò che scrive qualcosa di utile | Sessioni SSH |

---

## Passo 5 — Trasferirsi su un altro server

Quando cambi o migri il server non serve modificare i pulsanti uno per uno. Usa la [selezione multipla](../pro/multiselect.md) per riassegnare in blocco tutti i pulsanti del Backend:

1. **Ctrl+clic** su ogni pulsante del Backend (o selezionali tutti con un rettangolo): compare la barra delle azioni in basso
2. Premi **Macchina** nella barra delle azioni
3. Scegli il nuovo server

Tutti i pulsanti selezionati vengono aggiornati in una sola operazione.

---

## Risultato

Due categorie pulite — Frontend e Backend — nel menu in alto ti danno esattamente i comandi che ti servono. Il terminale resta aperto per il lavoro esplorativo; Commandeck si occupa della parte ripetitiva.

!!! tip
    Tieni fra i 6 e i 10 pulsanti per categoria. Con più di così, muoversi diventa scomodo quanto il terminale.
