---
description: Preguntas frecuentes sobre Commandeck — precio, privacidad, seguridad con la IA, plataformas compatibles y en qué se diferencia de los alias, los scripts y los paneles web.
---

# Preguntas frecuentes

## ¿Commandeck es gratis?

La edición gratuita es **de uso libre**: comandos y botones locales ilimitados, sin cuenta y
sin caducidad. **Pro** es un **pago único de 29 $** (sin suscripción: se compra una vez y es
tuyo para siempre) que añade máquinas SSH, botones multimáquina, temas, copia de seguridad y
el servidor MCP. Todas las versiones Pro incluyen una **prueba automática de 14 días**, sin
tarjeta y sin correo electrónico. Consulta [Pro y precios](pro.md).

## He comprado Pro, ¿cómo lo activo?

Gratis y Pro son **dos descargas distintas**. Tu clave se activa en la edición **Pro**:
[descárgala](download.md), abre **Preferencias**, pulsa **Activar Pro** y pega la clave. Si
venías de la edición gratuita, tranquilo: las dos comparten la misma configuración, así que
**tus botones y ajustes se conservan** automáticamente.

## ¿Por qué no usar alias o un script?

Si vives en la terminal y tus alias te funcionan, quizá no necesites Commandeck. Brilla en
dos situaciones: los comandos que **no** ejecutas lo bastante a menudo como para recordarlos
(el mantenimiento de una vez al mes, o ese comando que te dio una IA hace tres semanas), y
la gente que quiere un botón, no un símbolo del sistema. Los botones están a la vista y
ordenados, la salida se abre en una ventana, el destino SSH se elige al pulsar y los
comandos delicados piden confirmación: eso es justo lo que `history | grep` no hace.

## ¿En qué se diferencia de un panel web autoalojado?

Algunas herramientas resuelven un problema parecido en forma de **servicio web que instalas
en un servidor** (un contenedor que ejecutar, un archivo YAML que configurar, un puerto que
abrir, un navegador para llegar). Commandeck toma la forma contraria: una **aplicación de
escritorio en tu propio ordenador**. Nada que alojar, ningún puerto abierto, ningún archivo
de configuración: editas los botones en una interfaz y se guardan como TOML en tu disco.
Varias personas pueden seguir actuando sobre el mismo servidor: cada una ejecuta Commandeck
en su dispositivo y conserva sus propios botones para esa máquina, así que toda la casa puede
manejar el servidor familiar. La única diferencia real es dónde viven los botones: en el
ordenador o el móvil de cada persona, y no en un servidor central que hay que montar y
mantener.

## ¿Envía datos fuera? ¿Telemetría? ¿Cuenta?

No hay telemetría, ni cuenta, ni nube, ni ningún servicio a la escucha. Los botones y las
máquinas son archivos TOML en tu disco; tus claves SSH se quedan donde están (Commandeck
guarda la *ruta*, nunca la clave). El único tráfico de red son las conexiones SSH que *tú*
configuras. Consulta [Seguridad](reference/security.md).

## ¿No es peligroso dejar que una IA ejecute comandos?

Lo sería si estuviera activado por defecto, y no lo está. La ejecución por IA está detrás de
**tres permisos separados**: un ajuste general (desactivado de fábrica), una casilla por
botón («la IA puede ejecutar este») y, en los botones con confirmación, una confirmación
explícita adicional. Los botones en modo terminal no pueden ser ejecutados por la IA en
ningún caso, y cada ejecución queda escrita en un registro de auditoría. El servidor MCP es
puramente local (stdio): no expone nada en la red. Detalles en
[Integración con IA (MCP)](pro/mcp.md).

## ¿Es Electron? ¿Cuánto pesa?

No: Commandeck es Python + Qt (PySide6) con componentes nativos, no un navegador empaquetado.
Linux se distribuye como AppImage, macOS como .dmg y Windows como instalador. El SSH usa
Paramiko, así que no depende del OpenSSH del sistema.

## ¿Funciona en Wayland?

Sí. Un par de comodidades de ventana están limitadas con honestidad: «siempre visible»
funciona en X11 y aparece desactivado con su explicación en Wayland, porque esa decisión la
toma el compositor.

## ¿Cuándo llega la aplicación de Android? ¿Y iOS?

Una aplicación nativa de Android (una app completa, con SSH y temas, no una web disfrazada)
está en pruebas cerradas camino de Play Store. iOS vendrá después de Android (mismo código),
todavía sin fecha.

## ¿Qué pasa si el proyecto se detiene?

Tu aplicación sigue funcionando. Pro es un pago único con una licencia pensada para
funcionar sin conexión: no hay suscripción que caduque ni servidor del que dependan tus
botones. Tu configuración es un TOML en tu propio disco, sin nada atado a un servidor ni a
una cuenta.

## ¿Dónde se guarda mi configuración?

| Plataforma | Ubicación |
|------------|-----------|
| Linux | `~/.config/commandeck/` |
| macOS | `~/Library/Application Support/Commandeck/` |
| Windows | `%APPDATA%\Commandeck\` |

`buttons.toml` es legible para una persona: puedes leerlo, guardarlo o versionarlo como
quieras. Pro añade [copia de seguridad y restauración](pro/backup.md) en un clic.

## ¿Puedo usarlo sin ningún servidor?

Por supuesto: la versión gratuita es exactamente eso, un lanzador local para los comandos
que ejecutas en tu propio ordenador. El SSH solo entra en juego cuando añades máquinas
remotas (Pro).

## He encontrado un fallo / tengo una idea. ¿Dónde lo cuento?

En [GitHub Issues](https://github.com/neurocontrarian/commandeck/issues) para los fallos y en
[Discussions](https://github.com/neurocontrarian/commandeck/discussions) para las ideas y
para compartir botones útiles. Cada informe se lee, y los fallos se corrigen.
