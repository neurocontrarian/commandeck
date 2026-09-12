# Integrazione IA (MCP)

!!! warning "Sperimentale"
    L'integrazione con l'IA è sperimentale. Il supporto agli strumenti e il comportamento cambiano da modello a modello e da client a client. I risultati non sono garantiti: rivedi sempre ciò che l'IA crea o modifica.

Commandeck include un server MCP (Model Context Protocol). Una volta configurato, il tuo assistente IA può leggere e gestire direttamente i tuoi pulsanti, senza copia-incolla e senza spiegargli la tua configurazione.

> *«Aggiungi un pulsante chiamato "Riavvia Nginx" che esegue `sudo systemctl restart nginx` nella categoria Server»*

!!! info "Richiede Commandeck 2.0.17 o successivo (Pro)"
    MCP è una funzione **Pro**. Le istruzioni qui sotto avviano il server dall'applicazione stessa con `--mcp-server`, disponibile dalla **2.0.17**. Controlla la tua versione in **Menu ☰ → Informazioni**.

## Passo 1 — Attiva l'accesso MCP in Commandeck

MCP è **disattivato di fabbrica**. Attivalo una volta:

**Preferenze → Integrazione con il desktop → Consenti l'accesso MCP**

![Preferenze — interruttore dell'accesso MCP](../assets/preferences-mcp.png)

## Passo 2 — Trova il tuo comando MCP di Commandeck

Il server MCP è incluso nell'applicazione: si avvia eseguendo Commandeck con il parametro `--mcp-server`. Il comando esatto dipende da come l'hai installato. Trova il tuo qui sotto; lo userai nel tuo client IA al passo 3.

=== "Linux (AppImage)"

    È l'installazione più comune. Usa l'AppImage **Pro** (MCP è una funzione Pro) e assicurati che sia eseguibile (`chmod +x` una volta):

    ```bash
    /percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Usa il *tuo* nome di file e il tuo percorso reali (il download porta versione e architettura nel nome). Trucco: trascina l'AppImage in un terminale per ottenerne il percorso completo.

=== "macOS"

    L'eseguibile sta dentro il pacchetto `.app`:

    ```bash
    /Applications/Commandeck.app/Contents/MacOS/Commandeck --mcp-server
    ```

=== "Windows"

    Usa il percorso in cui hai installato Commandeck (fra virgolette se contiene spazi):

    ```powershell
    "C:\Program Files\Commandeck\Commandeck.exe" --mcp-server
    ```

!!! tip "Provalo una volta"
    Eseguendo il comando direttamente dovrebbe restare in attesa di input (parla JSON-RPC su standard input e output): vuol dire che funziona. Premi `Ctrl+C` per uscire. Se scrive *«the MCP server requires Commandeck Pro»*, stai usando la versione gratuita.

Nel resto di questa pagina, **`<il tuo comando Commandeck>`** indica l'eseguibile di questo passo (per esempio il percorso dell'AppImage), e **`--mcp-server`** è il suo parametro.

## Passo 3 — Configura il tuo client IA

Scegli il tuo strumento qui sotto. La configurazione si fa una volta; dopo funziona da sola.

=== "Claude Desktop"

    **Posizione del file di configurazione:**

    | Sistema | Percorso |
    |---------|----------|
    | Linux | `~/.config/Claude/claude_desktop_config.json` |
    | macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
    | Windows | `%APPDATA%\Claude\claude_desktop_config.json` |

    Aggiungi questo al file (crealo se non esiste), con il comando del passo 2:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    Su macOS `command` sarebbe `/Applications/Commandeck.app/Contents/MacOS/Commandeck`; su Windows, il percorso completo di `Commandeck.exe`. Riavvia Claude Desktop: Commandeck compare come strumento collegato.

=== "Claude Code"

    Esegui questo una volta in un terminale (sostituisci con il tuo comando):

    ```bash
    claude mcp add commandeck /percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Per verificare: `claude mcp list`

=== "Cursor"

    Modifica `~/.cursor/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    Riavvia Cursor.

=== "Windsurf"

    Modifica `~/.codeium/windsurf/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    Riavvia Windsurf.

=== "Continue.dev"

    Aggiungi questo a `.continue/config.yaml` nel tuo progetto:

    ```yaml
    mcpServers:
      - name: commandeck
        command: /percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage
        args:
          - --mcp-server
    ```

    Gli strumenti MCP sono disponibili solo in **modalità Agente**.

=== "Open WebUI (llama.cpp / Ollama)"

    Open WebUI si collega agli strumenti via HTTP, non via stdio. Usa [mcpo](https://github.com/open-webui/mcpo) (il proxy ufficiale di Open WebUI) per fare da ponte con Commandeck.

    !!! warning "Esegui mcpo con lo stesso utente che usa Commandeck"
        Il server legge i pulsanti di **chi lo avvia**. Ogni utente Linux o macOS ha la propria configurazione di Commandeck (`~/.config/commandeck`). Se avvii mcpo con un utente diverso da quello con cui usi Commandeck, l'IA vedrà l'insieme di pulsanti *sbagliato* (o vuoto). Avvia mcpo da un terminale aperto con il tuo utente desktop abituale.

    **Passo 1 — Installa mcpo (una volta):**

    ```bash
    pipx install mcpo
    # niente pipx? anche un ambiente virtuale va benissimo:
    #   python3 -m venv ~/.mcpo-venv && ~/.mcpo-venv/bin/pip install mcpo
    # (il semplice `pip install mcpo` su Linux spesso fallisce con "externally-managed-environment")
    ```

    **Passo 2 — Trova l'IP locale della macchina su cui gira Commandeck (solo se Open WebUI è su un'altra macchina):**

    ```bash
    hostname -I | awk '{print $1}'
    ```

    Annota questo IP: ti servirà al passo 4.

    **Passo 3 — Avvia il proxy (lascia aperto questo terminale):**

    ```bash
    mcpo --port 8000 -- /percorso/completo/di/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Dovresti vedere: `Uvicorn running on http://0.0.0.0:8000`

    !!! tip "Attenzione agli a capo nel copia-incolla"
        Tieni il comando su **una sola riga**. Se incollandolo si spezza in più righe rotte, salvalo come piccolo script: crea `start-mcpo.sh` con la riga qui sopra ed esegui `bash start-mcpo.sh`.

    **Passo 4 — Aggiungi il server di strumenti in Open WebUI:**

    Vai in **Pannello di amministrazione → Impostazioni → Strumenti** (nelle versioni più vecchie: *Integrazioni → Gestisci i server di strumenti*) → **`+`** e compila:

    | Campo | Valore |
    |-------|--------|
    | Tipo | **OpenAPI** |
    | Nome | `commandeck` |
    | URL | `http://<ip-del-passo-2>:8000` |
    | Autenticazione | Nessuna |

    !!! warning "Usa l'IP della macchina, non localhost"
        Se Open WebUI gira su un'altra macchina (per esempio un server di casa), `localhost` punterebbe a quel server e non alla macchina su cui gira mcpo. Usa l'IP del passo 2. Dalla macchina di Open WebUI puoi verificare con `curl http://<quell-ip>:8000/openapi.json` (deve restituire del JSON). Se non lo fa, apri la porta 8000 nel firewall della macchina su cui gira mcpo.

    **Passo 5 — Attiva lo strumento in una conversazione:**

    Apri una nuova conversazione, premi l'icona **`+`** (strumenti) vicino al campo di testo e attiva **commandeck**.

    !!! tip
        Funziona con qualsiasi motore supportato da Open WebUI: llama.cpp, Ollama, API compatibili con OpenAI e così via. Lo strato degli strumenti è indipendente dal modello. Il supporto alle chiamate varia da modello a modello: quelli addestrati a seguire istruzioni di solito funzionano meglio; i piccoli modelli locali possono aver bisogno del [prompt di sistema](#recommended-system-prompt) qui sotto per usarli in modo affidabile.

    ---

    **Quando riavviare mcpo**

    mcpo avvia il server MCP di Commandeck come sottoprocesso all'accensione e ne legge l'elenco degli strumenti **una sola volta**. Riavvia mcpo ogni volta che:

    - **Attivi o disattivi «Consenti l'accesso MCP»** nelle Preferenze (se avvii mcpo prima di attivarlo, vede zero strumenti)
    - Aggiorni Commandeck a una nuova versione

    Per riavviarlo: premi `Ctrl+C` nel terminale di mcpo e torna al passo 3; oppure, con il servizio systemd qui sotto, `systemctl --user restart mcpo-commandeck`.

    ---

    **Passo 6 — (Facoltativo) Far sopravvivere mcpo ai riavvii**

    Crea un servizio utente systemd perché mcpo parta da solo all'accesso (eseguilo **con il tuo utente desktop abituale**):

    ```bash
    mkdir -p ~/.config/systemd/user
    cat > ~/.config/systemd/user/mcpo-commandeck.service << 'EOF'
    [Unit]
    Description=mcpo proxy for the Commandeck MCP server

    [Service]
    ExecStart=%h/.local/bin/mcpo --port 8000 -- %h/Apps/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    Restart=on-failure
    RestartSec=5

    [Install]
    WantedBy=default.target
    EOF

    systemctl --user daemon-reload
    systemctl --user enable --now mcpo-commandeck
    ```

    Comandi utili:

    ```bash
    systemctl --user status mcpo-commandeck    # vedere lo stato
    systemctl --user restart mcpo-commandeck   # riavviare dopo aver attivato MCP o aggiornato
    systemctl --user stop mcpo-commandeck      # fermare
    journalctl --user -u mcpo-commandeck -f    # log in diretta
    ```

    !!! note
        Adatta i percorsi in `ExecStart`: punta alla *tua* AppImage ed esegui `which mcpo` per sapere dov'è mcpo se non è in `~/.local/bin/mcpo` (per esempio dentro un ambiente virtuale).

---

## Prompt di sistema consigliato

Incolla il testo qui sotto nel campo del prompt di sistema del tuo client IA. Prepara il modello a chiamare prima `help`, a seguire i giusti percorsi di ricerca e a scomporre i comandi complessi in pezzi di Commandeck invece di incollarli così come sono.

!!! note "Resta in inglese di proposito"
    Questo testo è rivolto al modello, non a te. I nomi degli strumenti e dei campi sono in inglese: tradurlo rende le chiamate meno affidabili.

```
You are an assistant for Commandeck, a desktop application on Linux, macOS or Windows. Commandeck
lets the user run commands by clicking buttons, like a remote control. You can create, read,
and modify the user's buttons, machines, and profiles using your tools.

Rules:
- Before doing anything, call the help tool to read the instructions.
- When the user explicitly names a button, use get_button(name="X") directly. When you don't
  know the exact name, use list_buttons.
- Never call get_button before create_button.
- For buttons: a duplicate means SAME NAME, not same command. If no button has the exact same
  name, create it without asking.
- For machines: a duplicate means SAME HOST address. Always call list_machines and check by
  host before creating.
- For profiles: a duplicate means same name. Call list_profiles before creating.
- When asked to change a property, always apply the change. Never decide the current value is
  already acceptable.
- In multi-step requests, if a required resource exists, use it and proceed.
- When you need a machine ID or profile ID, always look it up first.
- Write each command in the right shell for its target: PowerShell or cmd for a Windows machine,
  bash/sh for Linux or macOS. Set the button's os field to match. Check each machine's os with
  list_machines; for a local button (no machine) use this computer's OS. Never give a Windows
  machine a bash command, or a Linux/macOS machine a PowerShell command.
- The user can install ready-made button packs from the gallery: call list_packs to see what is
  available and what has updates, then install_pack / update_pack / uninstall_pack to manage them.

When a user asks you to add or refactor a shell command, decompose it before creating a button:
1. `cd /some/path` → Execution Profile working_dir (strip from command)
2. `sudo -u user` wrapper → run_as_user on the profile or button's run_as field
   (strip the wrapper, keep the inner command)
3. Opens an interactive shell (bash, zsh, exec bash) → execution_mode = "terminal"
4. Produces output the user wants to read → execution_mode = "output"; fire-and-forget → "silent"
5. What remains after stripping context wrappers is the command field.

Example: `sudo -u www-data bash -c 'cd /var/www/myapp && git pull'`
→ Create Profile: name="Web Deploy", run_as_user="www-data", working_dir="/var/www/myapp"
→ Create button: command="git pull", execution_mode="output", assign that profile
```

=== "Open WebUI"

    In Open WebUI, vai in **Pannello di amministrazione → Impostazioni → Prompt di sistema** e incolla il testo qui sopra (oppure mettilo nel prompt di sistema della conversazione, nelle impostazioni del modello).

=== "Claude Desktop"

    Claude Desktop non offre un campo per il prompt di sistema. La descrizione dello strumento `help` si spiega da sola per Claude: non serve nessun testo aggiuntivo.

=== "Altri client"

    Incolla il testo nel campo del prompt di sistema o delle istruzioni che il tuo client mette a disposizione, prima di iniziare la conversazione.

---

## Che cosa può fare la tua IA

**Pulsanti**

| Strumento | Descrizione |
|-----------|-------------|
| `help` | Restituisce la guida completa al lavoro: va sempre chiamata per prima |
| `list_buttons` | Elenca tutti i pulsanti, con filtro facoltativo per categoria |
| `get_button` | Dà i dettagli di un pulsante per nome o identificativo |
| `create_button` | Crea un nuovo pulsante (nome, comando, categoria, colore, icona, modalità di esecuzione, profilo, macchine…) |
| `update_button` | Modifica qualsiasi campo di un pulsante esistente; chiama prima `get_button` per ottenerne l'identificativo |
| `execute_button` | Esegue il comando di un pulsante e ne restituisce l'output (disattivato di fabbrica; vedi [Consentire all'IA di eseguire i pulsanti](#allowing-ai-to-run-buttons)) |
| `delete_button` | Elimina un pulsante tramite il suo identificativo |

**Categorie**

| Strumento | Descrizione |
|-----------|-------------|
| `list_categories` | Elenca i nomi di tutte le categorie |

**Macchine SSH** *(funzione Pro)*

| Strumento | Descrizione |
|-----------|-------------|
| `list_machines` | Elenca le macchine SSH configurate (nome, host, utente, porta; mai le chiavi private) |
| `create_machine` | Aggiunge una macchina SSH |
| `update_machine` | Rinomina o riconfigura una macchina SSH; chiama prima `list_machines` per ottenerne l'identificativo |
| `delete_machine` | Elimina una macchina SSH tramite il suo identificativo |

**Profili di esecuzione** *(funzione Pro)*

| Strumento | Descrizione |
|-----------|-------------|
| `list_profiles` | Elenca tutti i profili di esecuzione |
| `get_profile` | Dà i dettagli di un profilo per nome o identificativo |
| `create_profile` | Crea un profilo riutilizzabile (utente di esecuzione, cartella di lavoro) |
| `update_profile` | Modifica un profilo esistente; chiama prima `get_profile` per ottenerne l'identificativo |
| `delete_profile` | Elimina un profilo tramite il suo identificativo |

**Pacchetti di pulsanti** — insiemi già pronti, dalla galleria pubblica

| Strumento | Descrizione |
|-----------|-------------|
| `list_packs` | Elenca i pacchetti della galleria, con i contrassegni `installed` e `update_available` |
| `install_pack` | Installa un pacchetto su alcune macchine (solo pacchetti con firma verificata) |
| `update_pack` | Aggiorna un pacchetto installato mantenendo le tue modifiche, le destinazioni e le posizioni |
| `uninstall_pack` | Rimuove tutti i pulsanti di un pacchetto |
| `export_pack` | Esporta i pulsanti scelti in un file `.cdpack` condivisibile |

**Variabili**

| Strumento | Descrizione |
|-----------|-------------|
| `list_variable_values` | Elenca i tuoi valori salvati per le `{{variabili}}` dei comandi |

!!! warning "Controlla prima di cancellare"
    `delete_button`, `delete_machine` e `delete_profile` sono disponibili via MCP. Verifica sempre l'elemento giusto con `get_button` o `list_machines` prima di chiedere alla tua IA di cancellare qualcosa.

!!! tip "Aggiornare la griglia dopo le modifiche dell'IA"
    Quando l'IA crea o modifica un pulsante, premi **F5** (oppure menu → Ricarica i pulsanti) per aggiornare la griglia senza riavviare Commandeck.

!!! tip "Consiglio per modificare i pulsanti"
    Se l'IA dice di non riuscire a modificare un pulsante, chiedile di chiamare prima `get_button` con il nome del pulsante per ottenerne l'identificativo e poi `update_button` con quell'identificativo.

---

## Consentire all'IA di eseguire i pulsanti

Di fabbrica la tua IA può **leggere e modificare** i pulsanti, ma non **eseguirli**. Per lasciarle davvero lanciare dei comandi devi dare il permesso a tre livelli: se anche uno solo è disattivato, l'esecuzione viene bloccata.

**1. Interruttore generale** — *Preferenze → Integrazione con il desktop → Consenti l'esecuzione da parte dell'IA*

Disattivato di fabbrica. È l'interruttore principale di tutta la funzione.

**2. Permesso per singolo pulsante** — *Modifica un pulsante → Comportamento → Consenti all'IA di eseguire questo pulsante*

Disattivato di fabbrica su ogni pulsante, compresi quelli che avevi già. Attivalo solo per i pulsanti i cui comandi ti senti tranquillo a lasciare in mano a un'IA: controlli di sola lettura (`df -h`, `systemctl status`), operazioni ripetibili senza danno, distribuzioni sicure.

**3. Conferma** — *Modifica un pulsante → Comportamento → Chiedi conferma prima di eseguire*

Con questa attiva, l'IA non può eseguire il pulsante in silenzio. Riceve una risposta `requires_confirmation` con il comando esatto e l'istruzione di mostrartelo e aspettare la tua approvazione prima di richiamare con `confirmed=true`. Consigliato per qualsiasi comando delicato (riavvii, cancellazioni, sudo).

**Registro di controllo:** ogni esecuzione via MCP viene aggiunta a `~/.config/commandeck/.mcp_executions.log` con data e ora, nome del pulsante, macchina di destinazione, codice di uscita e durata.

**Limitazioni:**

- I pulsanti in modalità `Apri nel terminale` non si possono eseguire via MCP: in un contesto IA senza interfaccia non esiste nessun terminale. Se ci prova, l'IA riceve un errore.
- L'output restituito all'IA è limitato (4 KB di output standard e 2 KB di errori) per non riempirle il contesto. L'output completo resta nel registro, se ti serve.
- I pulsanti con più destinazioni obbligano l'IA a indicare su quale macchina eseguire. Se non lo fa, il server le restituisce l'elenco delle destinazioni valide e le chiede di chiarire.

---

## Sicurezza

Il server MCP usa il **trasporto stdio**: quando un client (Claude Desktop, Cursor…) lo avvia direttamente, gira come sottoprocesso e comunica solo tramite standard input e output. Non viene aperta nessuna porta di rete, e solo il processo che l'ha avviato può parlargli.

Quando usi **mcpo** (Open WebUI) una porta HTTP (la 8000) *viene* aperta sulla macchina su cui gira mcpo. Assicurati che quella porta non sia esposta a reti di cui non ti fidi: tienila sulla rete locale, dietro il firewall.

!!! warning
    Con l'accesso MCP attivo, il tuo assistente IA può creare, modificare ed eliminare pulsanti. Disattiva l'interruttore nelle Preferenze quando non ti serve. L'**esecuzione** dei pulsanti è una funzione a parte da autorizzare; vedi [Consentire all'IA di eseguire i pulsanti](#allowing-ai-to-run-buttons).
