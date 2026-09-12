# Gestionar tu servidor doméstico desde Windows

Tú trabajas en un PC con Windows, pero tu servidor de casa lleva Linux: un NAS, un mini-PC, una máquina con Proxmox, una Raspberry Pi. Cada vez que necesita atención te toca elegir entre opciones incómodas: abrir PowerShell y entrar por SSH a mano, instalar PuTTY y acordarte de los comandos, o rebuscar en un panel web que no cubre lo que de verdad necesitas.

Commandeck te da una tercera opción: una aplicación normal de Windows en la que cada tarea del servidor es un botón. Lo pulsas, el comando se ejecuta en tu servidor Linux por SSH y la salida aparece en una ventana. Sin terminal y sin recordar comandos.

![Cuadrícula de Commandeck con botones de servidor doméstico: Espacio en disco, Qué está en marcha, Actualizar el servidor, Reiniciar el multimedia, Carpetas más grandes y un Reiniciar en rojo](../assets/howto-home-server-grid.png)

---

## Por qué encaja en la situación Windows-a-Linux

Hoy muchos servidores domésticos se montan con un asistente de IA como profesor: te dice qué instalar y te da los comandos. Acabas con una máquina Linux que apenas tocas directamente y un montón de comandos repartidos por conversaciones antiguas de ChatGPT o Claude. Volver a encontrarlos cada vez que algo falla es la verdadera lata.

Commandeck es donde esos comandos se convierten en botones. Funciona de forma nativa en Windows (también en Mac y Linux), así que gestionas el servidor Linux desde el escritorio que ya usas todo el día.

---

## Paso 1 — Instala Commandeck en Windows

[Descarga](../download.md) el instalador de Windows y ejecútalo. Es una aplicación de escritorio corriente: no hace falta la línea de comandos ni para instalarla ni para usarla.

---

## Paso 2 — Añade tu servidor una sola vez

Abre **Menú → Gestionar máquinas → +** y rellena los datos de tu servidor:

| Campo | Ejemplo |
|-------|---------|
| Nombre | `Servidor de casa` |
| Anfitrión | `192.168.1.50` |
| Usuario SSH | `pi` |
| Puerto | `22` |
| Clave SSH | pulsa **Generar clave SSH** y luego **Copiar la clave al servidor** |

Si nunca has usado claves SSH, Commandeck lo hace por ti: genera una clave, la copia al servidor (escribes tu contraseña una vez) y después pulsas **Probar** para confirmar que conecta. A partir de ahí no vuelves a escribir ninguna contraseña.

!!! tip "El SSH es Pro"
    Conectarse a otra máquina es una función de [Commandeck Pro](../pro.md): **29 $ una sola vez, tuyo para siempre, con 14 días de prueba gratis y sin tarjeta**. Es la razón principal por la que esta aplicación existe en el caso Windows-a-Linux.

---

## Paso 3 — Convierte tus tareas habituales en botones

Haz un botón para cada cosa que hagas con regularidad en el servidor. Algunas encajan en casi cualquier servidor doméstico:

| Etiqueta | Comando | Modo |
|----------|---------|------|
| `Espacio en disco` | `df -h` | Mostrar la salida |
| `Qué está en marcha` | `docker ps` | Mostrar la salida |
| `Actualizar el servidor` | `sudo apt update && sudo apt upgrade -y` | Mostrar la salida |
| `Reiniciar el multimedia` | `sudo systemctl restart jellyfin` | Silencioso + confirmación |
| `Reiniciar` | `sudo systemctl reboot` | Silencioso + confirmación (rojo) |

Cada botón apunta al servidor que añadiste en el paso 2. Al pulsarlo, el comando se ejecuta **en el servidor** y te muestra el resultado en tu escritorio Windows.

---

## El resultado

Tu servidor doméstico Linux tiene ahora un panel de control en Windows hecho por ti, ajustado exactamente a las tareas que haces. Sin PowerShell, sin PuTTY y sin rebuscar en conversaciones antiguas.

- **Privado por diseño**: sin cuenta, sin nube y sin telemetría. Los comandos van directos de tu PC a tu servidor.
- **Tus botones son archivos normales** en tu propio ordenador: haz copia, llévatelos a otro PC, son tuyos.
- **La misma aplicación en Mac y Linux** si cambias de máquina, y una aplicación nativa de Android para que los mismos botones funcionen desde tu móvil.

---

**Relacionado:** la guía [Gestión de un servidor doméstico](../use-cases/home-server.md) es la versión completa y paso a paso de esto. ¿Varias máquinas? Mira [Gestionar un parque homelab](../use-cases/homelab.md).
