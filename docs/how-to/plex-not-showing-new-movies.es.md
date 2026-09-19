---
title: ¿Plex no muestra tus películas nuevas? Haz que vuelva a mirar
description: Copiaste una película en la carpeta y Plex la ignora. Así puedes hacer que Plex recorra de nuevo tus bibliotecas, desde un botón en tu ordenador y sin abrir una terminal.
---

# ¿Plex no muestra tus películas nuevas? Haz que vuelva a mirar

Copiaste una película en tu carpeta de películas. Abres Plex. No está.

No hay nada roto. Plex solo conoce los archivos que ha *mirado*, y no vigila tus carpetas a cada segundo, sobre todo cuando la carpeta está en un NAS, en una carpeta compartida en red o dentro de Docker, donde la señal que avisa de que «ha llegado un archivo nuevo» a menudo nunca le llega.

La solución es decirle que vuelva a mirar. En un servidor, el consejo habitual es entrar por SSH y ejecutar un comando con un número de biblioteca que antes hay que averiguar. Esta es la versión sin nada de eso.

---

## La solución de un clic

Commandeck ofrece un **pack de botones gratuito para Plex**. Instálalo una vez y tendrás un botón que le pide a Plex recorrer otra vez todas tus bibliotecas —películas, series, música— nombrando cada una a su paso.

1. Abre Commandeck y añade tu servidor como máquina (su dirección, tu nombre de usuario, tu contraseña o tu clave SSH).
2. Menú **☰ → Packs de botones → Linux → Plex (Docker)** → *Instalar*, y elige esa máquina. (¿Plex instalado directamente en la máquina en vez de en un contenedor? Coge **Plex (system install)**: los mismos botones, con órdenes distintas por debajo.)
3. Pulsa **Look for new films and episodes**.

```
Películas... looked through.
Series... looked through.
Música... looked through.

Plex lee los archivos nuevos en segundo plano; van apareciendo a medida que avanza.
```

Nada que escribir, ningún número de biblioteca que buscar. La película nueva aparece en Plex unos segundos después; una biblioteca grande tarda unos minutos.

---

## Si aun así no aparece

Tres razones explican casi todos los casos, y el mismo pack responde a las tres.

**El disco está lleno.** Plex necesita sitio para escribir lo que aprende de un archivo. Con el disco al 100 %, un análisis puede terminar sin añadir nada y, en el peor caso, dañar el catálogo de Plex. Pulsa **Space & conversion cache**: lee todas las carpetas que Plex puede ver y te avisa con palabras claras si alguna está casi llena.

**Plex no puede leer el archivo.** Una película copiada desde otro ordenador suele conservar los permisos de aquel. Pulsa **What Plex reported**: si Plex no ha podido abrir algo, lo dice ahí, una sola vez, en lugar de quedar enterrado entre miles de líneas de su propio parloteo.

**El catálogo está dañado.** Es raro, pero explica un Plex que olvida películas o pierde las marcas de visto. Pulsa **Is the database healthy?**: revisa una *copia* de la base de datos de Plex, así que no cambia nada, y te dice qué ha encontrado.

---

## El resto del pack

El pack es gratuito y tiene quince botones. Los más usados:

| Botón | Responde a |
|---|---|
| **Is Plex running?** | Si está en marcha y, si se paró, por qué |
| **Why is Plex busy?** | Un vídeo convirtiéndose, un análisis en curso, o ninguna de las dos |
| **What Plex reported** | Todos los mensajes que escribió Plex, cada uno una vez, con cuántas veces se repitió |
| **Why is the graphics chip not used?** | Las cuatro razones por las que Plex convierte el vídeo por la vía lenta |
| **Restart Plex** | El primer gesto cuando algo se queda colgado |
| **Clear the conversion cache** | Borra solo el vídeo convertido temporal, nunca tus películas |

Cada comando se ve antes de instalar, y puedes modificarlos todos después.

---

## Actuar sobre tu servidor pasa por SSH

Tu servidor Plex es una máquina distinta de aquella en la que estás sentado, así que estos botones llegan a él por SSH. Esa parte es [Commandeck Pro](../pro.md): **29 $ una vez, para siempre, con 14 días de prueba que no piden tarjeta ni cuenta**. El pack, como todos los packs, es gratis.

Nada sale de tu ordenador: sin cuenta, sin nube, sin ningún servidor nuestro por medio. Tus máquinas y tus contraseñas se quedan en tu dispositivo.

---

**También te puede servir:** [Reiniciar Jellyfin o Plex sin la terminal](restart-jellyfin-plex-without-terminal.md) · [Ver el espacio libre del NAS en un clic](check-disk-space-nas.md) · ¿empiezas ahora? Lee la [guía para principiantes](../use-cases/beginner.md).
