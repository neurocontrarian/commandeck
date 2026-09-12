# Comandos Docker como botones de un clic

Si tu servidor doméstico ejecuta aplicaciones en Docker — Jellyfin, Immich, Pi-hole, Nextcloud, el conjunto *arr — convives con un puñado de comandos `docker` que reescribes una y otra vez: ver qué está en marcha, reiniciar un contenedor, mirar los registros, actualizar el conjunto. No son difíciles, pero es fácil equivocarse y cansa teclearlos siempre.

Commandeck convierte cada uno en un botón. Lo pulsas, el comando se ejecuta (en este ordenador o en tu servidor por SSH) y la salida aparece en una ventana.

![Categoría «Docker» de Commandeck: Qué está en marcha, Reiniciar contenedor, Ver registros, Estadísticas, Actualizar el conjunto y Liberar espacio](../assets/howto-docker.png)

---

## Los comandos Docker que merece la pena convertir en botones

| Tarea | Comando | Modo sugerido |
|-------|---------|---------------|
| Ver qué está en marcha | `docker ps` | Mostrar la salida |
| Ver todo (incluido lo parado) | `docker ps -a` | Mostrar la salida |
| Reiniciar un contenedor | `docker restart jellyfin` | Silencioso + confirmación |
| Ver los registros de un contenedor | `docker logs --tail 100 jellyfin` | Mostrar la salida |
| Consumo de recursos en directo | `docker stats --no-stream` | Mostrar la salida |
| Actualizar un conjunto compose | `docker compose pull && docker compose up -d` | Mostrar la salida + confirmación |
| Liberar espacio en disco | `docker system prune -f` | Mostrar la salida + confirmación |
| Espacio ocupado por Docker | `docker system df` | Mostrar la salida |

El botón de «actualizar el conjunto» es el que más gusta: descarga las imágenes más recientes y lo reinicia todo, en un clic en vez de dos comandos escritos en el orden correcto.

---

## Crea una categoría «Docker»

Crea los botones de arriba y pon `Docker` en el campo **Categoría** de cada uno. Se agruparán bajo una sola entrada del desplegable de categorías, así que todos tus controles de contenedores quedan en un mismo sitio ordenado.

En los ejemplos, cambia `jellyfin` por el nombre de tu contenedor (`docker ps` te muestra los nombres).

!!! tip "Un solo botón para cualquier contenedor"
    Con una [variable de comando](../reference/command-variables.md), un único botón **Reiniciar contenedor** puede preguntar *cuál* cada vez: escribes o eliges el nombre y ejecuta `docker restart {{contenedor}}`. Un botón los cubre todos.

---

## Ejecútalos en tu servidor, no solo en local

Docker suele estar en el servidor — el NAS o el mini-PC — y no en tu portátil. Apunta los botones a esa máquina y se ejecutarán por SSH, de modo que gestionas tus contenedores desde el escritorio en el que estás.

!!! tip "En remoto = Pro"
    Ejecutar botones en otra máquina por SSH es [Commandeck Pro](../pro.md): **29 $ una sola vez, de por vida, con 14 días de prueba gratis y sin tarjeta**. Los botones que ejecutan Docker en *este* ordenador funcionan en la versión gratuita.

---

## Por qué los botones ganan a reescribir

- **El comando correcto, en el orden correcto, siempre** — sobre todo el «actualizar el conjunto», que son dos pasos.
- **Sin memorizar nombres de contenedores ni parámetros**: van dentro del botón.
- **Una confirmación** en los destructivos (`prune`, reinicios) para que nada ocurra por accidente.
- **Privado**: sin cuenta, sin nube y sin telemetría; el comando va directo a tu máquina.

Monta la categoría una vez y todo tu Docker se convierte en un panel de botones que cualquiera en casa podría usar.

---

**Relacionado:** consulta la guía [Gestión de un servidor doméstico](../use-cases/home-server.md) para el montaje completo, o la de [Flujo de desarrollo](../use-cases/dev-workflow.md) si son contenedores de desarrollo.
