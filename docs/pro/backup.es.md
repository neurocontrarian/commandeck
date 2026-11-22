# Copia y restauración

!!! tip "Función Pro"
    La copia y restauración de la configuración requiere [Commandeck Pro](../pro.md).

Commandeck ofrece tres formatos de exportación separados — botones, máquinas y valores de variables guardados — deliberadamente aparte por motivos de seguridad.

Los encontrarás en la pestaña **Preferencias → Copia de seguridad**.

![Preferencias — pestaña de copia de seguridad](../assets/preferences-backup.png)

---

## Copia de botones — `.cdbackup`

Este archivo contiene **solo tus botones**:

- `buttons.toml`: todos tus botones y su configuración

**No** contiene tus máquinas, ni tu licencia Pro, ni tus ajustes de Preferencias: importar un `.cdbackup` solo puede cambiar tus botones. (Las máquinas tienen su propio archivo `.cdmachines`, más abajo.)

### Cuándo usarla

- Antes de un cambio importante (borrar muchos botones, reorganizar las categorías)
- Al llevar Commandeck a otro ordenador
- Como instantánea periódica de tu biblioteca de botones

### Exportar

Pulsa **Exportar los botones**. Se abre un selector de archivos: elige dónde guardar el `.cdbackup`.

### Importar

Pulsa **Importar botones** y elige un archivo `.cdbackup`. Commandeck te pregunta cómo importarlo:

- **Reemplazar todo**: quita tus botones actuales y usa los del archivo.
- **Añadir los nuevos**: conserva tus botones actuales y añade solo los del archivo que aún no tienes (se comparan por su comando, así que reimportar el mismo archivo no añade nada).

En ambos casos se hace antes una copia de tus botones, así que la importación se puede deshacer: mira **Restaurar los botones anteriores**, más abajo.

!!! note
    Con **Reemplazar todo**, los botones por defecto de *esta* plataforma que falten en el archivo se vuelven a añadir automáticamente, así que nunca pierdes los de tu sistema.

### Deshacer una importación o un reinicio

**Menú → Restaurar los botones anteriores** recupera tus botones desde la última copia automática (que se hace cada vez que importas o restableces los valores por defecto).

### Funciona entre plataformas

Un `.cdbackup` exportado en **Linux, macOS, Windows o Android se importa en cualquier otro**: el formato es idéntico en todas partes.

Lo que **no** es automáticamente portátil es el *texto del comando* de cada botón: un comando escrito para Linux (por ejemplo `sudo apt upgrade`) no funcionará en Windows, y al revés. Así que una copia es directamente reutilizable cuando el sistema de destino es el mismo. Para pasar de un sistema a otro:

- **Los botones SSH funcionan sin más**: el comando se ejecuta en la *máquina remota*, así que solo depende del sistema de esa máquina y no del aparato desde el que lo lanzas.
- Para los botones **locales**, adapta el comando al sistema nuevo o apóyate en los botones por defecto de la plataforma, que se vuelven a sembrar al importar.

### Cómo influye la etiqueta de sistema en la importación y en las máquinas

Cada botón lleva el sistema para el que está escrito su **comando** (Multiplataforma / Linux / macOS / Windows, se elige en el editor de botones), y cada máquina lleva el **sistema de su anfitrión** (en el editor de máquinas). Eso se usa para dos cosas:

- **La importación conserva las variantes de sistema una al lado de otra.** Un botón cuenta como «ya presente» solo cuando coinciden *a la vez* su comando **y** su sistema con uno que ya tengas. Así que importar un conjunto de botones de Windows en una instalación Linux **los añade** en lugar de chocar con tus botones Linux: acabas teniendo los dos. Reimportar el mismo conjunto sigue sin añadir nada.
- **La propagación solo empareja máquinas compatibles.** Cuando añades una máquina a todos tus botones, se asocia únicamente a los botones cuyo sistema coincide con el de la máquina (o que son multiplataforma). Una máquina Windows nunca acaba en un botón con un comando de Linux. (Linux y macOS se consideran compatibles, porque comparten el mismo conjunto de comandos por defecto.)

Un botón que se queda como **Multiplataforma** (lo normal en los botones que creas tú) se empareja con cualquier máquina; etiquétalo como Linux, macOS o Windows solo cuando su comando sea propio de un sistema.

---

## Copia de máquinas — `.cdmachines`

Este archivo contiene:

- `machines.toml`: todas las definiciones de máquinas SSH (nombre, anfitrión, usuario, puerto, ruta de la clave, icono)

### Lo que NO incluye

Las **claves privadas** SSH nunca se exportan. El archivo solo guarda la ruta al archivo de la clave (`~/.ssh/id_ed25519`), no la clave.

!!! warning
    El archivo `.cdmachines` contiene nombres de anfitrión, direcciones IP, usuarios SSH y números de puerto. Trátalo como cualquier archivo de configuración de red: no lo compartas en público ni lo guardes sin cifrar en un sitio accesible.

### Cuándo usarla

- Al montar Commandeck en un segundo ordenador (las claves SSH hay que copiarlas aparte)
- Como registro de la configuración de tu infraestructura de servidores

### Exportar

Pulsa **Exportar las máquinas**. Elige dónde guardar el archivo `.cdmachines`.

### Importar

Pulsa **Importar máquinas** y elige un archivo `.cdmachines`. Las máquinas se fusionan con las que ya tengas. Las repetidas (misma combinación de anfitrión y usuario) se omiten.

---

## Copia de variables — `.cdvariables`

Este archivo contiene tus **valores de variables guardados**: las respuestas reutilizables de las `{{variables}}` que gestionas desde **Menú → Valores de variables** (por ejemplo, la lista de los nombres de tus contenedores). **No** contiene ni botones ni máquinas.

### Exportar

Pulsa **Exportar las variables**. Elige dónde guardar el archivo `.cdvariables`.

### Importar

Pulsa **Importar variables** y elige un archivo `.cdvariables`. Los valores guardados se fusionan con los tuyos: se añade cualquier valor de una variable que aún no tengas.

---

## Restaurar en un ordenador nuevo

Lista completa para la mudanza:

1. Instala Commandeck en la máquina nueva
2. Copia tus claves privadas SSH a `~/.ssh/` en la máquina nueva (con `scp` o un USB; mantenlas a buen recaudo)
3. Activa tu licencia Pro en Preferencias
4. Importa el archivo `.cdbackup` para recuperar tus botones
5. Importa el archivo `.cdmachines` para recuperar las definiciones de máquinas
6. Importa el archivo `.cdvariables` para recuperar tus valores de variables
7. Prueba cada conexión desde **Menú → Gestionar máquinas → (elige la máquina) → Probar**
