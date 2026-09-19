---
description: Domande frequenti su Commandeck — prezzo, privacy, sicurezza con l'IA, piattaforme supportate e differenze rispetto ad alias, script e pannelli web.
---

# Domande frequenti

## Commandeck è gratuito?

L'edizione gratuita è **libera da usare**: comandi e pulsanti locali illimitati, senza
account e senza scadenza. **Pro** è un **acquisto unico da 29 $** (nessun abbonamento: si
compra una volta ed è tuo per sempre) e aggiunge macchine SSH, pulsanti multi-macchina, temi,
backup e ripristino e il server MCP. Ogni versione Pro include una **prova automatica di 14
giorni**, senza carta e senza email. Vedi [Pro e prezzi](pro.md).

## Ho comprato Pro, come lo attivo?

Gratis e Pro sono **due download diversi**. La tua chiave si attiva nell'edizione **Pro**:
[scaricala](download.md), apri **Preferenze**, premi **Attiva Pro** e incolla la chiave. Se
venivi dall'edizione gratuita non preoccuparti: le due condividono la stessa configurazione,
quindi **i tuoi pulsanti e le tue impostazioni restano** automaticamente.

## Perché non usare alias o uno script?

Se vivi nel terminale e i tuoi alias funzionano, forse Commandeck non ti serve. Dà il meglio
in due casi: i comandi che **non** usi abbastanza spesso da ricordarli (la manutenzione una
volta al mese, o quel comando che un'IA ti ha dato tre settimane fa) e le persone che
vogliono un pulsante, non un prompt. I pulsanti sono visibili e ordinati, l'output si apre in
una finestra, la macchina SSH si sceglie al momento del clic e i comandi delicati chiedono
conferma: proprio quello che `history | grep` non fa.

## In cosa è diverso da un pannello web self-hosted?

Alcuni strumenti risolvono un problema simile sotto forma di **servizio web da installare su
un server** (un container da avviare, un file YAML da configurare, una porta da esporre, un
browser per raggiungerlo). Commandeck ha la forma opposta: un'**applicazione desktop sul tuo
computer**. Niente da ospitare, nessuna porta aperta, nessun file di configurazione: modifichi
i pulsanti in un'interfaccia e vengono salvati come TOML sul tuo disco. Più persone possono
comunque agire sullo stesso server: ognuna usa Commandeck sul proprio dispositivo e tiene i
propri pulsanti per quella macchina, così tutta la casa può gestire il server di famiglia.
L'unica differenza vera è dove vivono i pulsanti: sul computer o sul telefono di ciascuno, non
su un server centrale da installare e mantenere.

## Manda dati all'esterno? Telemetria? Account?

Nessuna telemetria, nessun account, nessun cloud, nessun servizio in ascolto. Pulsanti e
macchine sono file TOML sul tuo disco; le chiavi SSH restano dove sono (Commandeck salva il
*percorso*, mai la chiave). L'unico traffico di rete sono le connessioni SSH che configuri
*tu*. Vedi [Sicurezza](reference/security.md).

## Non è pericoloso lasciare che un'IA esegua comandi?

Lo sarebbe se fosse attivo di default, e non lo è. L'esecuzione da parte dell'IA sta dietro a
**tre autorizzazioni separate**: un'impostazione generale (disattivata di fabbrica), una
casella per singolo pulsante («l'IA può eseguirlo») e, per i pulsanti con conferma, una
conferma esplicita in più. I pulsanti in modalità terminale non sono mai eseguibili dall'IA e
ogni esecuzione finisce in un registro di controllo. Il server MCP è solo locale (stdio): non
espone nulla in rete. Dettagli in [Integrazione IA (MCP)](pro/mcp.md).

## È Electron? Quanto pesa?

No: Commandeck è Python + Qt (PySide6) con componenti nativi, non un browser impacchettato.
Linux è distribuito come AppImage, macOS come .dmg e Windows come installer. L'SSH usa
Paramiko, quindi non dipende dall'OpenSSH di sistema.

## Funziona su Wayland?

Sì. Un paio di comodità legate alle finestre sono limitate con onestà: «sempre in primo
piano» funziona su X11 e appare disattivato con la sua spiegazione su Wayland, perché quella
decisione spetta al compositor.

## Quando arriva l'app Android? E iOS?

Un'app Android nativa (un'app completa, con SSH e temi, non un sito travestito) è in test
chiuso e diretta al Play Store. iOS seguirà Android (stesso codice), ancora senza data.

## Cosa succede se il progetto si ferma?

La tua app continua a funzionare. Pro è un acquisto unico con una licenza pensata per
funzionare offline: nessun abbonamento che scade, nessun server da cui dipendano i tuoi
pulsanti. La tua configurazione è un TOML sul tuo disco, senza nulla legato a un server o a
un account.

## Dove viene salvata la configurazione?

| Piattaforma | Posizione |
|-------------|-----------|
| Linux | `~/.config/commandeck/` |
| macOS | `~/Library/Application Support/Commandeck/` |
| Windows | `%APPDATA%\Commandeck\` |

`buttons.toml` è leggibile da una persona: puoi aprirlo, copiarlo o versionarlo come
preferisci. Pro aggiunge [backup e ripristino](pro/backup.md) con un clic.

## Posso usarlo senza nessun server?

Certo: la versione gratuita è esattamente questo, un lanciatore locale per i comandi che
esegui sul tuo computer. L'SSH entra in gioco solo quando aggiungi macchine remote (Pro).

## Ho trovato un problema / ho un'idea. Dove lo scrivo?

Su [GitHub Issues](https://github.com/neurocontrarian/commandeck/issues) per i problemi e su
[Discussions](https://github.com/neurocontrarian/commandeck/discussions) per le idee e per
condividere pulsanti utili. Ogni segnalazione viene letta e i problemi vengono corretti.
