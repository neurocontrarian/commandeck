---
title: ¿Plex se come todo el procesador? Esta es la razón
description: El servidor se calienta y la película se entrecorta. Plex está rehaciendo el vídeo en vez de enviarlo tal cual. Descubre en un clic por qué y qué cambiar, sin terminal.
---

# ¿Plex se come todo el procesador? Esta es la razón

La película se entrecorta. El ventilador se dispara. El servidor, silencioso toda la semana, está de pronto al 100 %.

Casi siempre ocurre lo mismo: **Plex está rehaciendo el vídeo, imagen a imagen, en lugar de enviar el archivo tal cual.** Plex lo llama transcodificar. Pasa cuando el aparato con el que ves no sabe leer el archivo original: formato equivocado, imagen demasiado grande, o un subtítulo que hay que incrustar.

Tu servidor puede hacer ese trabajo de dos maneras. El chip gráfico lo hace sin apenas calentarse. El procesador lo hace al 100 % y a duras penas. La mayoría de los servidores domésticos van por el camino lento sin que su dueño lo sepa.

---

## Saberlo en un clic

Commandeck ofrece un **pack de botones gratuito para Plex**: uno para Plex en Docker y otro para Plex instalado en la propia máquina. Instálalo, apúntalo a tu servidor y dos botones responden.

**1. «Why is Plex busy?»** — dice si hay una conversión en marcha, sobre qué archivo y lo que cuesta:

```
=== Converting a video right now? ===
Yes - Plex is converting a video right now.
  File: Sintel
  CPU:  98.0% for that one process
```

**2. «Why is the graphics chip not used?»** — comprueba una a una las cuatro razones por las que Plex vuelve en silencio al procesador:

```
=== 1. Is there a graphics chip to use? ===
No /dev/dri/renderD* on this machine.

=== 2. Is Plex allowed to open it? ===
The device belongs to group: render
The plex user is NOT in that group. Fix it with: sudo usermod -aG render plex

=== 3. Is the setting ticked? ===
Plex has never been given the setting.
Settings > Transcoder > Use hardware acceleration when available.

=== 4. What the log says the last time it converted ===
Nothing about hardware in the recent log.
```

También recuerda lo que ninguna orden puede comprobar: la conversión por hardware necesita un **Plex Pass** activo. Sin él, Plex usa el procesador y nunca lo menciona.

---

## Las cuatro causas y qué hacer con cada una

**El chip no está, o no está compartido.** En un mini-PC o un NAS sí está: casi todos los procesadores Intel de los últimos diez años llevan uno. Si tu Plex va en un contenedor Docker, hay que entregarle el dispositivo: añade `devices: - /dev/dri:/dev/dri` a tu archivo compose, o marca la casilla equivalente en tu gestor de contenedores. Si Plex va dentro de un contenedor Proxmox, el dispositivo debe pasarse desde el anfitrión.

**Plex no tiene permiso para abrirlo.** El chip pertenece a un grupo, normalmente `render` o `video`, y la cuenta con la que corre Plex debe estar en él. El botón muestra la orden exacta para tu máquina.

**El ajuste está desactivado.** Plex no lo activa solo: *Ajustes → Transcodificador → Usar aceleración por hardware cuando esté disponible*.

**No hay Plex Pass.** La conversión por hardware es una función de pago. Esa no es un fallo, y ninguna orden la esquiva.

---

## A veces la solución es no convertir nada

La conversión más rápida es la que no ocurre. Dos cosas que probar antes de comprar nada:

- **Baja la calidad en el aparato que está viendo.** Si el reproductor pide «Original», Plex envía el archivo intacto y no hace nada.
- **Mira qué se está convirtiendo.** Si el botón dice que la imagen se «copia tal cual» y solo cambia el sonido, tu servidor apenas trabaja: ese es el caso bueno y no hay nada que arreglar.

Y una trampa que conviene conocer: un disco casi lleno lo ralentiza todo, conversiones incluidas. El botón **Space & conversion cache** del pack te avisa con palabras claras cuando alguno de tus discos se está quedando sin sitio.

---

## Conseguir los botones

Menú **☰ → Packs de botones → Linux → Plex (Docker)** o **Plex (system install)**, gratis como todos los packs. Elige el que corresponda a cómo está instalado Plex en tu servidor: los dos usan órdenes completamente distintas.

Llegar a tu servidor por SSH es [Commandeck Pro](../pro.md): **29 $ una vez, para siempre, con 14 días de prueba sin tarjeta ni cuenta**. Nada sale de tu ordenador: sin cuenta, sin nube, sin ningún servidor nuestro por medio.

---

**También te puede servir:** [¿Plex no muestra tus películas nuevas?](plex-not-showing-new-movies.md) · [Ver el espacio libre del NAS en un clic](check-disk-space-nas.md) · ¿empiezas ahora? Lee la [guía para principiantes](../use-cases/beginner.md).
