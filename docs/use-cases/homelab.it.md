# Caso d'uso: gestire un parco homelab

!!! tip "Funzione Pro"
    Le macchine SSH, i pulsanti multi-macchina e i profili di esecuzione richiedono [Commandeck Pro](../pro.md).

🔰 **L'obiettivo:** hai qualche macchina in casa — un NAS, un Raspberry Pi, un piccolo server — e continui a scrivere gli stessi comandi SSH per controllarle. Con Commandeck crei i pulsanti una volta e li premi da un'unica finestra. Questa pagina mette insieme i pezzi: macchine, pulsanti multi-macchina e profili.

## 1. Aggiungi le tue macchine

**Menu ☰ → Gestisci macchine → Aggiungi.** Dai a ciascuna un nome, un host, un utente e una chiave SSH.

![Gestisci macchine](../assets/machines-list.png)

Alla prima connessione Commandeck mostra l'impronta digitale dell'host e ti chiede di confermarla (vedi [Sicurezza](../reference/security.md)): non serve preparare `known_hosts` da un terminale.

## 2. Un pulsante, più server

Nell'[editor dei pulsanti](../reference/button-editor.md), sotto **Macchine di destinazione**, attiva più di una macchina (puoi includere anche **Locale**). Il pulsante diventa *multi-macchina*: a ogni clic si apre il selettore per scegliere dove eseguirlo.

![Selettore di macchina](../assets/machine-picker.png)

!!! example "Pulsante di controllo rapido"
    Comando `uptime && df -h`, con NAS, Pi e server tutti attivati. Un solo pulsante risponde a «come sta ogni macchina?»: scegli la destinazione ogni volta.

## 3. Riusa le condizioni di esecuzione con i profili

Se più pulsanti hanno bisogno dello stesso account di servizio o della stessa cartella di lavoro, salva una volta un [profilo di esecuzione](../reference/execution-profiles.md) e collegalo — per esempio un profilo **Deploy** (*esegui come* `www-data`, cartella `/var/www/app`) usato da tutti i pulsanti web.

## 4. Fai ordine con le categorie

Raggruppa i pulsanti in categorie come *NAS*, *Pi* o *Docker* perché la griglia resti leggibile. Scegli una categoria nel menu in alto per filtrare.

⚙️ **Per gli amministratori di sistema**

- **In parallelo o in sequenza:** un pulsante multi-macchina viene eseguito su **una** macchina per clic (tramite il selettore). Per lanciare lo stesso comando su tutti i server insieme, passa dal selettore una volta per host oppure tieni un pulsante per macchina dentro una categoria.
- **Parco con sistemi misti:** oggi un pulsante contiene un solo comando. Se la destinazione usa un sistema diverso da quello che il comando si aspetta (PowerShell contro bash), potrebbe non funzionare: per ora conviene tenere pulsanti separati per sistema.
- **Automatizza con l'IA:** collega un modello locale a Commandeck tramite [MCP](local-ai.md) e chiedigli di creare macchine, profili e pulsanti per tutto il parco in una volta sola.
