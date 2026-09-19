---
description: Convierte los comandos SSH de Batocera en botones. Descubre por qué un juego no arranca, cierra un emulador colgado, arregla una pantalla negra y mira qué llena el disco, sin enchufar un teclado a la máquina que está bajo la tele.
---

# Gestionar tu Batocera sin teclado

Una máquina con Batocera vive debajo del televisor. Tiene un mando, no tiene teclado y no tiene ninguna ventana que te diga qué ha ido mal. Así que el día en que un juego se niega a arrancar, el emulador se cuelga o la pantalla se queda en negro, la respuesta que encuentras en internet es siempre la misma: *«entra por SSH y ejecuta este comando»*.

El consejo funciona. Simplemente encaja mal con una máquina que usas desde el sofá: acabas buscando la dirección IP, abriendo una terminal en otro ordenador y reescribiendo comandos que consultaste hace tres meses.

Commandeck guarda esos comandos como **botones**. Los preparas una vez y luego respondes a la pregunta con un clic, desde tu escritorio.

!!! tip "Función Pro"
    Hablar con otra máquina por SSH necesita [Commandeck Pro](../pro.md), incluido en la prueba de 14 días y sin cuenta. Batocera es gratis y no necesita que le instales nada.

---

## Lo que necesitas

- Una **máquina Batocera en tu red**, encendida, y su **dirección IP** (Batocera la muestra en el menú principal, en *Ajustes de red*).
- El SSH ya viene **activado** en Batocera: no hay nada que instalar ni configurar en la máquina.
- Commandeck en tu ordenador Windows, Mac o Linux.

Batocera te conecta como **root**, así que aquí no hay ningún `sudo` ni contraseña de administrador.

---

## Paso 1 — Añade la máquina

**Menú ☰ → Gestionar máquinas → Añadir** y rellena:

| Campo | Valor |
|-------|-------|
| Nombre | `Batocera` |
| Anfitrión | la IP de tu máquina, por ejemplo `192.168.1.42` |
| Usuario SSH | `root` |
| Puerto | `22` |
| Autenticación | **Contraseña** |
| Contraseña SSH | `linux` |

`linux` es la contraseña de fábrica de Batocera para el usuario `root`: ya la tienes y no hay nada que preparar en la máquina. (Si la cambiaste en los ajustes de Batocera, usa la tuya.)

Pulsa **Probar**. Debería salir en verde, y ya está.

!!! note "Dónde se guarda la contraseña"
    Commandeck nunca la escribe en un archivo legible: va al llavero de tu propio ordenador — Administrador de credenciales en Windows, Llavero en macOS, el servicio de secretos del sistema en Linux. Se escribe una vez, aquí, y nunca más.

---

## Paso 2 — Instala el pack de Batocera

En lugar de escribir los comandos tú, instala el conjunto ya preparado.

**Menú ☰ → Packs de botones → Linux → Batocera → Instalar**, y elige la máquina que acabas de añadir.

Obtienes diecisiete botones, ya redactados como preguntas y no como comandos:

| Botón | Responde a |
|-------|------------|
| **Información del sistema Batocera** | ¿Qué máquina es esta y cuánto lleva encendida? |
| **¿Hay un juego en marcha?** | Qué juego y de qué consola, por su nombre y no por un número de proceso |
| **Depuración (es_launch_stderr.log)** | Por qué el último juego arrancó, o no |
| **Depuración (es_log.txt)** | Qué está haciendo el propio menú: descargas de carátulas, temas, arranques lentos |
| **Ver arrancar un juego en directo** † | El mismo registro, escribiéndose mientras el juego arranca |
| **Espacio libre** | Cómo de lleno está el disco y qué carpetas ocupan sitio |
| **¿Qué sistemas se comen el disco?** | El tamaño de la carpeta de ROMs de cada consola, de mayor a menor |
| **Recorrer el disco (ncdu)** † | Recorre /userdata carpeta a carpeta y borra sobre la marcha |
| **Mis mandos** | Qué mandos se ven, y la batería de los inalámbricos |
| **Desconectar los mandos inalámbricos** | Apaga todos los dispositivos Bluetooth: evita que los mandos se gasten de noche |
| **¿Qué está haciendo mi pantalla?** | La resolución que se está enviando y los modos que acepta tu televisor |
| **Fijar el modo de pantalla** | Fuerza una resolución: el rescate para la pantalla negra |
| **Cerrar el juego en marcha** | Mata un emulador colgado y te devuelve al menú |
| **Reiniciar el menú** | Reinicia EmulationStation sin reiniciar la máquina |
| **Monitor en vivo (htop)** | CPU, memoria y procesos actualizándose mientras juegas |
| **Reiniciar la máquina** / **Apagar la máquina** | De forma limpia, desde tu escritorio |

† Abren una terminal en tu ordenador, así que estos tres son solo de escritorio.

Todos los packs son gratuitos. Solo la conexión SSH es una función Pro.

---

## Los cuatro momentos en que lo vas a usar de verdad

### «Este juego no arranca»

Pulsas A, la pantalla parpadea y vuelves al menú. Batocera ha anotado lo que pasó, pero el archivo está en la máquina.

Pulsa **Depuración (es_launch_stderr.log)**. Saca primero las líneas sospechosas del último arranque — una BIOS que falta, un formato de ROM no admitido, un problema de permisos — y te dice claramente cuando ahí no hay nada raro. Después pulsa **Copiar**: eso es exactamente lo que los foros de Batocera te piden que pegues cuando pides ayuda.

Si el problema es el menú y no un juego — un sistema que no aparece, un tema que se ha roto, una descarga de carátulas atascada — usa **Depuración (es_log.txt)**. Ese es el segundo archivo que pide el soporte.

EmulationStation solo escribe ese segundo registro cuando se sube su nivel de detalle, así que si está apagado el botón te dice dónde encenderlo y te enseña, mientras tanto, los registros que sí existen.

### «Se ha colgado»

El mando no hace nada y el emulador se ha quedado clavado en pantalla. **Cerrar el juego en marcha** te dice qué juego está cerrando, lo mata y comprueba después que de verdad has vuelto al menú. Si no basta, **Reiniciar el menú** reconstruye la interfaz sin reiniciar del todo.

### «La pantalla está negra» o «la imagen está cortada»

**¿Qué está haciendo mi pantalla?** muestra la resolución que se está enviando ahora y la lista de modos que tu televisor acepta de verdad. **Fijar el modo de pantalla** fuerza uno de ellos: escribes el nombre del modo y, si te equivocas, el botón se niega a cambiar nada y te enseña la lista válida.

### «Los mandos vuelven a estar sin batería»

Un mando inalámbrico olvidado en la alfombra mantiene su radio despierta y amanece vacío. **Desconectar los mandos inalámbricos** corta todas las conexiones Bluetooth de la máquina y el mando se apaga solo unos segundos después. También es la forma educada de soltar un mando cuando un juego se ha colgado con él. Para volver a encenderlo, su botón central.

---

### «Me he quedado sin espacio»

**Espacio libre** muestra cómo de lleno está el disco y las carpetas más grandes en GB o TB. **¿Qué sistemas se comen el disco?** lo desglosa consola por consola, así ves que un sistema se está llevando medio disco antes de empezar a borrar nada.

---

## Desde el sofá, también

Los mismos botones existen en el móvil: Commandeck para Android está [en pruebas cerradas](../android-beta.md) y lee los mismos packs. Funciona por la red de casa, o por tu propia VPN si la tienes. Nada pasa por un servicio en la nube, porque no hay servicio en la nube.

---

## Conviene saber sobre Batocera

Batocera no es un servidor Linux normal, y eso cambia qué comandos tienen sentido:

- **Eres root.** Ningún `sudo` ni contraseña de administrador en ninguna parte.
- **El sistema es de solo lectura fuera de `/userdata`.** Lo que cambies en otro sitio desaparece en el siguiente reinicio.
- **No hay `systemctl` ni `journalctl`.** Los registros son archivos normales; por eso los dos botones de depuración leen archivos en lugar de preguntar a un servicio.
- **Las herramientas a pantalla completa** (`htop`, `ncdu`, un registro en directo) necesitan una terminal de verdad donde dibujarse. Un botón se la da: su modo es **Abrir en terminal**, y Commandeck abre `ssh -t` hacia la máquina en una ventana de terminal de tu ordenador. El pack trae tres: *Ver arrancar un juego en directo*, *Recorrer el disco (ncdu)* y *Monitor en vivo (htop)*.
- Esos tres son **solo de escritorio**: un móvil no tiene terminal que abrir, así que no aparecen en la cuadrícula en Android. Todos los demás botones del pack funcionan en ambos.
- Todo lo que pudiera **borrar un disco** se ha dejado fuera del pack a propósito.

---

## Relacionado

- [Packs de botones](../packs.md): qué es un pack y cómo funciona instalarlo
- [Máquinas SSH](../reference/ssh-machines.md): añadir máquinas, puertos y resolución de problemas
- [Gestionar un parque homelab](homelab.md): la misma idea con varias máquinas
- [Inicio rápido](../quick-start.md): si este es tu primer botón
