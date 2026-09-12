# Actualizar el servidor sin entrar por SSH

Mantener al día un servidor doméstico es la tarea que todo el mundo aplaza: hay que entrar por SSH, acordarse de si toca `apt` o `dnf`, lanzar la actualización y quizá reiniciar. Así que se va dejando, y un servidor sin actualizar es el que acaba con un agujero de seguridad o se rompe en la siguiente gran actualización.

Commandeck convierte «actualizar el servidor» en un botón que pulsas desde tu escritorio. La actualización se ejecuta por SSH en el propio servidor; tú solo miras la salida.

![Ventana de salida de Commandeck mostrando una actualización apt en curso, con los paquetes desempaquetándose y configurándose](../assets/howto-update-output.png)

---

## El botón de actualización

Elige el comando que corresponda al Linux de tu servidor:

| Tipo de servidor | Comando |
|------------------|---------|
| **Ubuntu / Debian / Raspberry Pi OS** | `sudo apt update && sudo apt upgrade -y` |
| **Fedora / CentOS / Rocky** | `sudo dnf upgrade -y` |
| **Arch** | `sudo pacman -Syu --noconfirm` |
| **Conjunto Docker** | `docker compose pull && docker compose up -d` |

Crea el botón:

| Campo | Valor |
|-------|-------|
| Etiqueta | `Actualizar el servidor` |
| Comando | *(el de la tabla de arriba)* |
| Modo de ejecución | `Mostrar la salida` |
| Confirmar antes de ejecutar | **Activado** |
| Descripción emergente | `Actualizar todos los paquetes del servidor` |

**Mostrar la salida** te deja ver la actualización mientras ocurre y saber qué ha cambiado. **Confirmar antes de ejecutar** te pide un «sí o no» antes de empezar.

---

## Una rutina de actualización segura, en tres botones

Las actualizaciones salen mejor como una pequeña secuencia. Haz un botón para cada paso:

1. **`Espacio en disco`** → `df -h`: asegúrate de que hay sitio antes de actualizar.
2. **`Actualizar el servidor`** → el comando de arriba: lanza la actualización.
3. **`Reiniciar si hace falta`** → `sudo systemctl reboot` (silencioso + confirmación, en rojo): solo si la actualización lo pide.

Ahora actualizar es: clic, clic, listo. Sin terminal y sin intentar recordar los comandos exactos.

---

## Esto se ejecuta en el servidor, por SSH

La gracia está en hacerlo **desde tu escritorio de cada día** — Windows, Mac o Linux — mientras los comandos corren en el servidor. Añades el servidor una vez y el botón llega hasta él por SSH cada vez.

!!! tip "El SSH es Pro"
    Ejecutar botones en una máquina remota es [Commandeck Pro](../pro.md): **29 $ una sola vez, de por vida, con 14 días de prueba gratis y sin tarjeta**. Actualizar *este* ordenador funciona en la versión gratuita.

---

## Por qué así sí se hace

- **Sin fricción, se hace de verdad.** Un botón que se pulsa en dos segundos es un servidor que se mantiene al día.
- **Ves la salida**: nada de actualizaciones a ciegas, miras lo que ha cambiado.
- **Una confirmación** antes de que nada se ejecute, y un botón de reinicio aparte que controlas tú.
- **Privado**: sin cuenta, sin nube y sin telemetría. Directo de tu escritorio a tu servidor.

---

**Relacionado:** la guía [Gestión de un servidor doméstico](../use-cases/home-server.md) construye la cuadrícula de mantenimiento completa. Para mirar el espacio antes, consulta [Ver el espacio libre del NAS](check-disk-space-nas.md).
