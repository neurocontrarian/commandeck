# Reiniciar Jellyfin o Plex sin terminal

Tu servidor multimedia ha dejado de responder en mitad de una película, o ha dejado de detectar los archivos nuevos, y la solución de siempre es «reiniciar el servicio». Pero eso significa abrir una terminal, acordarse del comando `systemctl` exacto y escribirlo sin equivocarse. Hay una forma más rápida: convertir ese comando en un botón que se pulsa.

Es justo lo que hace Commandeck, una aplicación de escritorio para Windows, Mac y Linux. Configuras el botón una vez y, a partir de ahí, reiniciar Jellyfin o Plex es un solo clic, con el resultado a la vista en una ventana.

![Cuadrícula de Commandeck con los botones rojos «Reiniciar Jellyfin» y «Reiniciar Plex» junto a Escanear biblioteca, Registros de Jellyfin y Espacio en disco](../assets/howto-restart-media.png)

!!! tip "Ya existe un conjunto preparado para Jellyfin"
    Esta página crea un botón a mano, que es la mejor manera de aprender. Si usas Jellyfin y
    quieres los otros trece — por qué se entrecorta, qué le llena el disco, qué registro
    mirar — instala el pack:
    [Mantener Jellyfin en forma sin aprender Docker](../use-cases/jellyfin.md).

---

## El comando que hay detrás del botón

En la mayoría de servidores domésticos, el comando de reinicio es uno de estos:

| Servidor | Comando |
|----------|---------|
| **Jellyfin** | `sudo systemctl restart jellyfin` |
| **Plex** | `sudo systemctl restart plexmediaserver` |
| **Jellyfin (Docker)** | `docker restart jellyfin` |
| **Plex (Docker)** | `docker restart plex` |

Si montaste el servidor con la ayuda de un asistente de IA, este es el comando que te dio. Commandeck es el lugar donde ese comando deja de vivir en una conversación antigua y se convierte en un botón.

---

## Crear el botón

Clic derecho en la cuadrícula → **Nuevo botón** (o pulsa `Ctrl+N`) y rellena:

| Campo | Valor |
|-------|-------|
| Etiqueta | `Reiniciar Jellyfin` |
| Comando | `sudo systemctl restart jellyfin` |
| Modo de ejecución | `Silencioso` |
| Confirmar antes de ejecutar | **Activado** |
| Color | `#e01b24` (rojo: avisa de que «esto reinicia algo») |
| Descripción emergente | `Reiniciar el servidor multimedia Jellyfin` |

**Confirmar antes de ejecutar** es la red de seguridad: muestra un «¿seguro?» para que nunca reinicies el servidor por accidente mientras alguien está viendo algo.

Con eso basta para un servidor que corre **en este mismo ordenador**. Pulsas el botón, confirmas y listo.

---

## Ejecutarlo en otra máquina (tu NAS o mini-PC)

Casi todo el mundo tiene Jellyfin o Plex en un equipo aparte — un NAS, una Raspberry Pi, un mini-PC — y no en el portátil de cada día. Commandeck puede llegar a esa máquina por SSH y ejecutar allí el botón, de modo que reinicias tu servidor multimedia **desde el escritorio en el que estás sentado**.

Añades el servidor una vez (su dirección y tu usuario) y apuntas el botón hacia él. A partir de ahí es el mismo clic único.

!!! tip "Esta parte es Pro"
    Controlar otra máquina por SSH es una función de [Commandeck Pro](../pro.md): **29 $ una sola vez, tuyo para siempre, con 14 días de prueba gratis y sin tarjeta**. La versión gratuita ejecuta botones en tu propio ordenador. Consulta [Máquinas SSH](../reference/ssh-machines.md) para configurarlo.

---

## Por qué esto gana a abrir una terminal

- **Nada que recordar.** El comando exacto vive en el botón, no en tu cabeza ni en una conversación vieja con una IA.
- **Ninguna errata en un comando delicado.** Haces clic; no reescribes `systemctl` a las once de la noche.
- **Una confirmación** evita los reinicios accidentales.
- **Privado por diseño.** Commandeck no tiene cuenta, ni nube, ni telemetría. El comando va directamente de tu ordenador a tu servidor y a ningún otro sitio.

Una vez que el botón existe, la próxima vez que Jellyfin se ponga tonto lo arreglas en un clic: sin terminal y sin buscar nada.

---

**Relacionado:** ¿montando un servidor entero? La guía [Gestión de un servidor doméstico](../use-cases/home-server.md) recorre paso a paso el SSH y una cuadrícula completa. ¿Nuevo en Commandeck? Empieza por la [Guía para principiantes](../use-cases/beginner.md).
