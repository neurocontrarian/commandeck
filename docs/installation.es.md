# Instalación

Commandeck funciona en **Linux, macOS y Windows**. Cada versión publica los archivos de las
tres plataformas juntos:
**[GitHub Releases](https://github.com/neurocontrarian/commandeck/releases/latest)** — ese
enlace siempre apunta a la versión más reciente, así que guárdalo en favoritos.

Todas las versiones **Pro** incluyen una **prueba gratuita de 14 días**: sin cuenta y sin
tarjeta. La prueba empieza sola en el primer arranque.

---

## Linux (AppImage)

Un solo archivo, sin instalación. Descárgalo, hazlo ejecutable y ábrelo. El AppImage es
**autónomo**: lleva dentro Python, Qt y todas las dependencias, así que no hay nada que
instalar en el sistema.

| Archivo | Cuándo usarlo |
|---------|---------------|
| `Commandeck-Linux-x86_64.AppImage` | **Gratis — Intel/AMD.** |
| `Commandeck-Linux-ARM64.AppImage` | **Gratis — ARM64** (Raspberry Pi 4+, servidor ARM, máquina virtual en Apple Silicon). |
| `Commandeck-Pro-Linux-x86_64.AppImage` | **Pro — Intel/AMD.** Prueba de 14 días incluida. |
| `Commandeck-Pro-Linux-ARM64.AppImage` | **Pro — ARM64.** Prueba de 14 días incluida. |

¿No sabes qué procesador tienes? Ejecuta `uname -m`: `x86_64` es Intel/AMD, `aarch64` es ARM.

```bash
chmod +x Commandeck-*.AppImage
./Commandeck-*.AppImage
```

Si tu distribución avisa de que falta el complemento de plataforma de Qt al arrancar,
instala `libxcb-cursor0`:

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

| Archivo | Cuándo usarlo |
|---------|---------------|
| `Commandeck-macOS-AppleSilicon.dmg` | **Gratis.** |
| `Commandeck-Pro-macOS-AppleSilicon.dmg` | **Pro.** Prueba de 14 días incluida. |

Abre el `.dmg` y arrastra **Commandeck** sobre la carpeta **Aplicaciones**: suelta cuando la
carpeta se resalte. Después **expulsa el disco** que apareció en el escritorio: una app abierta
desde el propio `.dmg` no funcionará.

> **Los Mac con Intel todavía no son compatibles**: la versión es para Apple Silicon (M1 o
> posterior).

La aplicación **aún no está firmada digitalmente**, así que en el primer arranque macOS muestra
*«Apple no ha podido verificar si Commandeck contiene software malicioso»*. Hacen falta tres pasos:

1. Pulsa **OK**, nunca *Mover a la papelera*.
2. Abre **Ajustes del Sistema → Privacidad y seguridad** y baja hasta la sección *Seguridad*:
   una línea *«Commandeck» se ha bloqueado* ofrece **Abrir igualmente**. Púlsala y confirma con
   Touch ID o tu contraseña. Esa línea solo aparece justo después de intentar abrir la app.
3. **Vuelve a abrir Commandeck.** Reaparece el mismo aviso, pero esta vez con un botón más:
   **Abrir igualmente**. Púlsalo. Es la última vez que lo verás.

> A partir de macOS 15, hacer clic derecho sobre la app → *Abrir* ya no funciona con apps sin
> firmar. Los Ajustes del Sistema son el único camino.

Si el botón no aparece, lo mismo desde el Terminal:

```bash
xattr -dr com.apple.quarantine /Applications/Commandeck.app
```

---

## Windows (x86_64)

| Archivo | Cuándo usarlo |
|---------|---------------|
| `Commandeck-Windows-x64.exe` | **Gratis** — instalador (acceso directo en el menú Inicio y desinstalador). |
| `Commandeck-Pro-Windows-x64.exe` | Instalador **Pro**. Prueba de 14 días incluida. |

Ejecuta el instalador. **Todavía no está firmado digitalmente**, así que SmartScreen puede
avisarte: pulsa **Más información → Ejecutar de todas formas**.

---

## Actualizar

Para actualizar, descarga el instalador más reciente desde
[commandeck.app](https://commandeck.app) (o desde la
[página de versiones](https://github.com/neurocontrarian/commandeck/releases/latest)) e
instálalo encima de la versión actual: tus botones y tus ajustes se conservan.
