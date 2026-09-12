# Installazione

Commandeck funziona su **Linux, macOS e Windows**. Ogni rilascio pubblica insieme i file per
tutte e tre le piattaforme:
**[GitHub Releases](https://github.com/neurocontrarian/commandeck/releases/latest)** — quel
link punta sempre alla versione più recente, quindi conviene salvarlo tra i preferiti.

Tutte le versioni **Pro** includono una **prova gratuita di 14 giorni**: senza account e
senza carta. La prova parte da sola al primo avvio.

---

## Linux (AppImage)

Un solo file, nessuna installazione. Scaricalo, rendilo eseguibile e avvialo. L'AppImage è
**autonomo**: contiene già Python, Qt e tutte le dipendenze, quindi non c'è nulla da
installare sul sistema.

| File | Quando usarlo |
|------|---------------|
| `Commandeck-Linux-x86_64.AppImage` | **Gratis — Intel/AMD.** |
| `Commandeck-Linux-ARM64.AppImage` | **Gratis — ARM64** (Raspberry Pi 4+, server ARM, macchina virtuale su Apple Silicon). |
| `Commandeck-Pro-Linux-x86_64.AppImage` | **Pro — Intel/AMD.** Prova di 14 giorni inclusa. |
| `Commandeck-Pro-Linux-ARM64.AppImage` | **Pro — ARM64.** Prova di 14 giorni inclusa. |

Non sai che processore hai? Esegui `uname -m`: `x86_64` è Intel/AMD, `aarch64` è ARM.

```bash
chmod +x Commandeck-*.AppImage
./Commandeck-*.AppImage
```

Se all'avvio la tua distribuzione segnala che manca il plugin di piattaforma Qt, installa
`libxcb-cursor0`:

=== "Debian / Ubuntu / Linux Mint"

    ```bash
    sudo apt install libxcb-cursor0
    ```

=== "Fedora"

    ```bash
    sudo dnf install xcb-util-cursor
    ```

=== "Arch Linux"

    ```bash
    sudo pacman -S xcb-util-cursor
    ```

---

## macOS (Apple Silicon)

| File | Quando usarlo |
|------|---------------|
| `Commandeck-macOS-AppleSilicon.dmg` | **Gratis.** |
| `Commandeck-Pro-macOS-AppleSilicon.dmg` | **Pro.** Prova di 14 giorni inclusa. |

Apri il `.dmg` e trascina **Commandeck** sulla cartella **Applicazioni**: rilascia quando la
cartella si evidenzia. Poi **espelli il disco** comparso sulla Scrivania: un'app avviata dal
`.dmg` stesso non funzionerà.

> **I Mac con Intel non sono ancora supportati**: la versione è per Apple Silicon (M1 o
> successivi).

L'app **non è ancora firmata digitalmente**, quindi al primo avvio macOS mostra *«Apple non ha
potuto verificare che Commandeck non contenga malware»*. Servono tre passaggi:

1. Fai clic su **OK**, mai *Sposta nel Cestino*.
2. Apri **Impostazioni di Sistema → Privacy e sicurezza** e scorri fino alla sezione
   *Sicurezza*: una riga *«Commandeck» è stato bloccato* propone **Apri comunque**. Fai clic e
   conferma con Touch ID o la tua password. Quella riga compare solo subito dopo un tentativo
   di avvio.
3. **Riavvia Commandeck.** Lo stesso avviso ricompare, ma stavolta con un pulsante in più:
   **Apri comunque**. Fai clic. È l'ultima volta che lo vedrai.

> Da macOS 15 in poi, il clic destro sull'app → *Apri* non funziona più per un'app non firmata.
> Le Impostazioni di Sistema sono l'unica strada.

Se il pulsante non compare, la stessa cosa dal Terminale:

```bash
xattr -dr com.apple.quarantine /Applications/Commandeck.app
```

---

## Windows (x86_64)

| File | Quando usarlo |
|------|---------------|
| `Commandeck-Windows-x64.exe` | **Gratis** — installer (collegamento nel menu Start e disinstallazione). |
| `Commandeck-Pro-Windows-x64.exe` | Installer **Pro**. Prova di 14 giorni inclusa. |

Avvia l'installer. **Non è ancora firmato digitalmente**, quindi SmartScreen potrebbe
avvisarti: clicca **Ulteriori informazioni → Esegui comunque**.

---

## Aggiornare

Per aggiornare, scarica l'installer più recente da
[commandeck.app](https://commandeck.app) (o dalla
[pagina dei rilasci](https://github.com/neurocontrarian/commandeck/releases/latest)) e
installalo sopra la versione attuale: i tuoi pulsanti e le tue impostazioni restano.
