---
description: Convierte en botones los comandos de Jellyfin que siempre acabas buscando — por qué se entrecorta, qué llena el disco, el registro que pide el soporte, reiniciar y actualizar — tanto en Docker como en una instalación de sistema.
---

# Mantener Jellyfin en forma sin aprender Docker

Jellyfin es la parte del servidor doméstico que se nota, porque es la que usa toda la casa. Cuando una película se entrecorta, cuando una carpeta nueva no aparece o cuando el disco se llena sin avisar, la respuesta que encuentras en internet siempre es un comando, y nunca es el mismo dos veces.

Commandeck guarda esos comandos como **botones**. Instalas el pack, lo apuntas a tu servidor y cada pregunta se convierte en un toque.

!!! tip "Función Pro"
    Hablar con tu servidor por SSH necesita [Commandeck Pro](../pro.md), incluido en la prueba de 14 días y sin cuenta. Los packs son gratuitos.

---

## Primero: ¿Docker o instalación de sistema?

Hay dos packs de Jellyfin, porque hay dos formas de usarlo. Si eliges el que no es, todos los botones responderán «no encontrado».

| Instalaste Jellyfin… | Tu pack |
|---|---|
| con **Docker** o **docker compose** (una pila de Portainer, la tienda de aplicaciones del NAS) | **Jellyfin (Docker)** |
| desde los **paquetes** de tu distribución (`apt install jellyfin`, un .deb, un script) | **Jellyfin (systemd)** |

Si no lo tienes claro, instala el de Docker y pulsa **¿Jellyfin está en marcha?**. Si te dice que no existe ningún contenedor con ese nombre, tienes la instalación de sistema.

---

## Puesta en marcha

1. **Menú ☰ → Gestionar máquinas → Añadir**: nombre, IP del servidor, tu usuario SSH, puerto 22. Elige **Contraseña** o **Clave SSH** para la autenticación y pulsa **Probar**.
2. **Menú ☰ → Packs de botones → Linux → Jellyfin (Docker o systemd) → Instalar**, y elige esa máquina.

Eso es todo. No se instala nada en el servidor.

---

## Qué responden los botones

| Botón | Responde a |
|---|---|
| **¿Jellyfin está en marcha?** | En marcha, parado o reiniciándose en bucle |
| **¿Por qué está ocupado Jellyfin?** | Qué está haciendo ahora mismo, casi siempre una conversión |
| **Recursos ahora mismo** | CPU y memoria, para saber si el límite es la máquina |
| **Errores recientes** | Solo las líneas de error, sacadas de un registro largo |
| **Registro reciente completo** | Las últimas 60 líneas en bruto, cuando los errores no bastan |
| **Seguir el registro en vivo** † | El registro escribiéndose mientras le das al play |
| **¿Quién está usando los discos?** | Qué proceso está castigando el disco |
| **Espacio y caché de conversión** | Cómo de lleno está el disco y cuánto se come la caché |
| **Aceleración por hardware** | Si tu tarjeta gráfica se está usando de verdad |
| **Complementos instalados** | Qué está cargado y qué no ha podido cargarse |
| **Reiniciar Jellyfin** | La solución de la mitad de los problemas |
| **Actualizar Jellyfin** | Descargar y reiniciar, de forma limpia |
| **Vaciar la caché de conversión** | Recupera espacio sin tocar tus películas |
| **Consola dentro del contenedor** † | Solo Docker, para las respuestas que empiezan por «ejecuta esto dentro del contenedor» |

† Abren una terminal en tu ordenador, así que estos dos son solo de escritorio.

---

## Las tres noches en que lo vas a usar

### «Se entrecorta todo el rato»

Pulsa **¿Por qué está ocupado Jellyfin?**. Si está convirtiendo, la película se está transformando sobre la marcha: eso es lo que calienta el servidor y vacía el búfer. Después, **Aceleración por hardware** te dice si ese trabajo lo hace la tarjeta gráfica o lo hace el procesador solo, que es la diferencia entre una película fluida y una entrecortada.

Si quieres verlo en directo, **Seguir el registro en vivo** sigue escribiendo mientras alguien le da al play, así ves empezar la conversión en tiempo real.

### «No arranca» / «la biblioteca está vacía»

**¿Jellyfin está en marcha?** primero: un contenedor que se reinicia en bucle se parece mucho a un servidor caído. Luego **Errores recientes**, que saca las líneas de error de un registro demasiado largo para leerlo. Nueve de cada diez veces, **Reiniciar Jellyfin** cierra el asunto.

### «El disco está lleno»

**Espacio y caché de conversión** te muestra cómo de lleno está el disco y cuánto ocupan los archivos temporales de conversión. **Vaciar la caché de conversión** borra esos archivos y nada más: nunca tus películas, nunca tus ajustes. No lo pulses mientras alguien está viendo algo.

---

## Desde el sofá, también

Los mismos botones funcionan en el móvil: Commandeck para Android está [en pruebas cerradas](../android-beta.md) y lee los mismos packs, por la red de casa o por tu propia VPN.

---

## Relacionado

- [Reiniciar Jellyfin o Plex sin terminal](../how-to/restart-jellyfin-plex-without-terminal.md): la versión de un solo botón, y el equivalente para Plex
- [Packs de botones](../packs.md): qué es un pack y cómo funciona instalarlo
- [Gestión de un servidor doméstico](home-server.md): la misma idea aplicada al resto del servidor
