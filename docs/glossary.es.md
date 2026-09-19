# Glosario

¿Hay palabras de este wiki que no te suenan? Aquí están explicadas en lenguaje llano.

**Comando**
: Una línea de texto que le dice al ordenador qué hacer — por ejemplo, `df -h` muestra el espacio libre en disco. Commandeck ejecuta el comando por ti cuando pulsas un botón, así no tienes que escribirlo.

**Botón (casilla)**
: Cada cuadrado de la cuadrícula de Commandeck. Un botón guarda un comando y lo ejecuta al pulsarlo.

**Intérprete de comandos (shell)**
: El programa que lee y ejecuta los comandos. En Linux y macOS suele ser `bash` o `zsh`; en Windows es **PowerShell**. Commandeck usa el que corresponde a tu sistema automáticamente.

**Terminal**
: La ventana de texto negra donde normalmente se escriben los comandos. Commandeck existe precisamente para que puedas evitarla, aunque un botón puede abrir una si eliges el modo «Abrir en terminal».

**Categoría**
: Una etiqueta que agrupa botones relacionados (por ejemplo, *Red* o *Hardware*). Las categorías aparecen como pestañas sobre la cuadrícula para filtrar lo que ves.

**SSH** *(Pro)*
: Una forma segura de ejecutar comandos en otro ordenador a través de la red — por ejemplo, gestionar el servidor de casa desde tu portátil. Commandeck usa SSH para enviar el comando de un botón a una máquina remota.

**Máquina** *(Pro)*
: Un ordenador remoto que has añadido a Commandeck (su dirección, su usuario y su clave SSH). Un botón puede apuntar a una o a varias máquinas.

**sudo / ejecutar como usuario**
: `sudo` ejecuta un comando con permisos de administrador; *ejecutar como usuario* lo ejecuta con una cuenta concreta (por ejemplo, una cuenta de servicio como `www-data`). Commandeck puede encargarse de ello mediante un [perfil de ejecución](reference/execution-profiles.md).

**Perfil de ejecución** *(Pro)*
: Un conjunto guardado de «condiciones de ejecución» — con qué usuario y en qué carpeta — que puedes reutilizar en varios botones. Consulta [Perfiles de ejecución](reference/execution-profiles.md).

**Salida**
: Lo que el comando devuelve por escrito (por ejemplo, las cifras de espacio en disco). Un botón puede mostrarla en una ventana, ejecutarse en silencio o abrir una terminal.

**AppImage**
: Una aplicación de Linux en un solo archivo: la descargas, la haces ejecutable y la abres. Sin instalación y sin tocar nada del sistema.

**MCP** *(Pro)*
: El puente que permite a un asistente de IA leer y gestionar tus botones por ti. Consulta [Integración con IA](pro/mcp.md).

**Gratis frente a Pro**
: La versión **gratuita** ejecuta comandos locales ilimitados y botones personalizados ilimitados. **Pro** añade máquinas SSH, botones multimáquina, temas, perfiles, copia de seguridad e integración con IA, con una prueba gratuita de 14 días.
