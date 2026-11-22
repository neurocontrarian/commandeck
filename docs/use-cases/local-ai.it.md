# Caso d'uso: pilotare Commandeck da un'IA locale

!!! tip "Funzione Pro"
    L'integrazione con l'IA (MCP) richiede [Commandeck Pro](../pro.md).

🔰 **L'idea:** invece di creare i pulsanti a mano, li *chiedi* a un assistente IA — «aggiungi un pulsante che riavvia Nginx nella categoria Server» — e lui li crea. L'IA può leggere i tuoi pulsanti, le tue macchine e i tuoi profili e, se glielo permetti, eseguirli. Funziona con gli assistenti nel cloud come Claude **e** con un modello del tutto locale che gira sul tuo hardware.

Questa pagina segue il percorso del modello locale dall'inizio alla fine con **Open WebUI** e un modello locale (per esempio Llama o Gemma). Per l'elenco completo dei client e delle opzioni, vedi il [riferimento sull'integrazione IA](../pro/mcp.md).

## Perché locale?

Un modello locale tiene tutto sulla tua macchina: i tuoi pulsanti, i tuoi comandi e i nomi dei tuoi server non escono mai dalla tua rete. Ottimo per un homelab e per chi tiene alla privacy.

## Passo per passo

### 1. Attiva l'accesso MCP

**Preferenze → Integrazione con il desktop → Consenti l'accesso MCP.**

![Consenti l'accesso MCP](../assets/preferences-desktop.png)

### 2. Avvia il server MCP di Commandeck

Il server è incluso nell'applicazione. Avvia il tuo Commandeck con `--mcp-server`:

```bash
/percorso/di/Commandeck-Pro-VERSION-Linux-x86_64.AppImage --mcp-server
```

!!! warning "Avvialo con l'utente che usa Commandeck"
    Il server legge i pulsanti di **chi lo avvia**. Lancialo da un terminale aperto con il tuo utente desktop abituale, altrimenti l'IA vedrà l'insieme di pulsanti sbagliato (o vuoto).

### 3. Fai da ponte verso Open WebUI con mcpo

Open WebUI parla con gli strumenti via HTTP, quindi metti davanti il proxy [mcpo](https://github.com/open-webui/mcpo):

```bash
mcpo --port 8000 -- /percorso/di/Commandeck-Pro-VERSION-Linux-x86_64.AppImage --mcp-server
```

Poi in Open WebUI: **Pannello di amministrazione → Impostazioni → Strumenti → +**, tipo **OpenAPI**, URL `http://<ip-della-macchina>:8000`. Se Open WebUI gira su un altro computer, usa l'IP della macchina su cui gira mcpo, non `localhost`.

### 4. Parla con i tuoi pulsanti

Apri una conversazione, attiva lo strumento **commandeck**, incolla il [prompt di sistema consigliato](../pro/mcp.md#recommended-system-prompt) e prova con:

> *«Elenca i miei pulsanti.»*
> *«Aggiungi un pulsante chiamato "Spazio su disco" che esegue `df -h` nella categoria Sistema.»*

Premi **F5** in Commandeck (oppure **menu → Ricarica i pulsanti**) per aggiornare la griglia e vedere comparire i nuovi pulsanti, senza riavviare nulla.

⚙️ **Note per utenti esperti**

- **Il modello conta.** Lo strato degli strumenti è indipendente dal modello, ma la qualità delle chiamate varia parecchio. I modelli addestrati a seguire istruzioni funzionano meglio; i piccoli modelli locali spesso hanno bisogno del prompt di sistema per usare gli strumenti in modo affidabile.
- **Lasciare che l'IA *esegua* i pulsanti** è un permesso a parte, con tre porte (interruttore generale + casella per pulsante + conferma facoltativa). Disattivato di fabbrica. Vedi [Consentire all'IA di eseguire i pulsanti](../pro/mcp.md#allowing-ai-to-run-buttons).
- **Tenere vivo il ponte:** un servizio utente systemd mantiene mcpo attivo dopo un riavvio; vedi il [riferimento MCP](../pro/mcp.md).
