# Caso de uso: gestión de un servidor doméstico

Esta guía monta Commandeck para llevar un servidor doméstico típico: una máquina con Plex, con Pi-hole o que hace de NAS. El objetivo es reducir las tareas de mantenimiento habituales a un solo clic.

!!! tip "Función Pro"
    Esta guía controla una máquina remota por SSH. **Las máquinas SSH, los botones multimáquina y los perfiles de ejecución requieren [Commandeck Pro](../pro.md).** En la versión gratuita puedes crear los mismos botones para que se ejecuten en tu ordenador.

## El escenario

Tienes una Raspberry Pi o un mini-PC en la red de casa. Ejecuta:

- **Plex Media Server**: tu servidor personal de vídeo
- **Pi-hole**: bloqueo de publicidad para toda la red
- **Samba**: compartir archivos por toda la casa

Y estás harto de entrar por SSH cada vez que hay que reiniciar un servicio o mirar el disco.

---

## Paso 1 — Añade el servidor como máquina SSH

Abre **Menú → Gestionar máquinas → +** y rellena:

| Campo | Valor de ejemplo |
|-------|------------------|
| Nombre | `Servidor de casa` |
| Anfitrión | `192.168.1.50` |
| Usuario SSH | `pi` |
| Puerto | `22` |
| Ruta de la clave SSH | `~/.ssh/id_ed25519` |
| Icono | Servidor |

Si todavía no tienes una clave SSH, pulsa **Generar clave SSH** y luego **Copiar la clave al servidor**, e introduce tu contraseña una vez. Después pulsa **Probar** para confirmar que la conexión funciona.

!!! tip "Función Pro"
    Añadir máquinas SSH requiere [Commandeck Pro](../pro.md).

---

## Paso 2 — Crea una categoría «Servidor de casa»

En el editor de botones, todos los botones que crees para este servidor llevarán **Categoría: Servidor de casa**. Así quedan agrupados bajo una entrada propia en el desplegable de categorías.

---

## Paso 3 — Crea los botones

### Mirar el espacio en disco

| Campo | Valor |
|-------|-------|
| Etiqueta | `Uso del disco` |
| Comando | `df -h` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` (tu máquina SSH) |
| Modo de ejecución | `Mostrar la salida` |
| Icono | `drive-harddisk-symbolic` |

Muestra el detalle de cada sistema de archivos del servidor. La ventana de salida se abre sola.

---

### Reiniciar Plex

| Campo | Valor |
|-------|-------|
| Etiqueta | `Reiniciar Plex` |
| Comando | `sudo systemctl restart plexmediaserver` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` |
| Modo de ejecución | `Silencioso` |
| Confirmar antes de ejecutar | Activado |
| Descripción emergente | `Reiniciar el servicio Plex Media Server` |
| Icono | `media-playback-start-symbolic` |

La confirmación evita reinicios accidentales mientras alguien está viendo algo.

---

### Actualizar los paquetes

| Campo | Valor |
|-------|-------|
| Etiqueta | `Actualizar el sistema` |
| Comando | `sudo apt update && sudo apt upgrade -y` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` |
| Modo de ejecución | `Mostrar la salida` |
| Descripción emergente | `Actualizar todos los paquetes instalados` |

El modo `Mostrar la salida` te deja ver qué se ha actualizado.

---

### Vaciar la caché DNS de Pi-hole

| Campo | Valor |
|-------|-------|
| Etiqueta | `Vaciar DNS` |
| Comando | `pihole restartdns` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` |
| Modo de ejecución | `Silencioso` |

---

### Ver el estado de Samba

| Campo | Valor |
|-------|-------|
| Etiqueta | `Estado de Samba` |
| Comando | `sudo systemctl status smbd nmbd` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` |
| Modo de ejecución | `Mostrar la salida` |

---

### Reiniciar el servidor

| Campo | Valor |
|-------|-------|
| Etiqueta | `Reiniciar el servidor` |
| Comando | `sudo systemctl reboot` |
| Categoría | `Servidor de casa` |
| Destino | `Servidor de casa` |
| Modo de ejecución | `Silencioso` |
| Confirmar antes de ejecutar | Activado |
| Color | `#e01b24` (rojo: señal de peligro) |
| Descripción emergente | `Reiniciar el servidor de casa: desconecta a todo el mundo` |

---

## Paso 4 — Multimáquina: ejecutar en varios servidores

Si más adelante añades un segundo servidor (un NAS, otra Pi), puedes configurar botones que apunten a varias máquinas. Por ejemplo, un botón **Actualizar el sistema** que quieras usar en los dos:

1. Abre el editor del botón **Actualizar el sistema**
2. En **Máquinas de destino**, activa tanto `Servidor de casa` como la segunda máquina
3. Guarda

A partir de ahí, al pulsar el botón se abre el [selector de máquina](../reference/ssh-machines.md#the-machine-picker): eliges cuál actualizar, o lo pulsas dos veces para hacer las dos.

---

## Resultado

Al elegir tu categoría **Servidor de casa** en el desplegable superior tienes a un clic todo lo que necesitas. Sin terminal.

!!! tip
    Si andas con el servidor a menudo a lo largo del día, activa **Siempre visible** en el menú. Commandeck se queda a la vista mientras trabajas en otras aplicaciones.

---

## Guías rápidas

Atajos de una sola tarea para lo más habitual:

- [Reiniciar Jellyfin o Plex sin terminal](../how-to/restart-jellyfin-plex-without-terminal.md)
- [Gestionar tu servidor doméstico desde Windows](../how-to/manage-home-server-from-windows.md)
- [Comandos Docker como botones de un clic](../how-to/docker-commands-one-click-buttons.md)
- [Ver el espacio libre del NAS en un clic](../how-to/check-disk-space-nas.md)
- [Actualizar el servidor sin entrar por SSH](../how-to/update-server-without-ssh.md)
