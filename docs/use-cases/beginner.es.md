# Caso de uso: guía para principiantes de Linux

Acabas de instalar Commandeck y no sabes muy bien por dónde empezar. Esta guía es para ti. No necesitas conocer ningún comando: Commandeck ya trae decenas de botones listos para usar.

---

## Ya tienes 29 botones

La primera vez que abres Commandeck, la cuadrícula se llena con tres categorías de botones ya preparados:

- **Hardware** (13 botones): disco, memoria, CPU, temperatura, tarjeta gráfica y herramientas de espacio
- **Esenciales de Linux** (12 botones): información del sistema, usuarios, registros, actualizaciones y mantenimiento básico
- **Red** (4 botones): interfaces, conexiones, puertos y servicios a la escucha

Estos botones ya funcionan. No hay nada que configurar.

¿Quieres más? Las herramientas de **Desarrollo** (git, Docker, Python, Node) y otros conjuntos están disponibles como [packs de botones](../packs.md) gratuitos, a un toque. Abre el menú → **Packs de botones** para verlos e instalarlos.

---

## Qué hace cada botón por defecto

### Hardware

| Botón | Qué te muestra |
|-------|----------------|
| **Uso del disco** | Cómo de llena está cada partición (`df -h`) |
| **Uso de memoria** | Consumo de RAM y de intercambio (`free -h`) |
| **Carga de CPU** | La carga actual y los procesos que más gastan |
| **Temperatura** | Temperaturas de CPU y sensores, si `lm-sensors` está instalado |
| **Dispositivos de bloque** | Discos duros, memorias USB y particiones (`lsblk`) |
| **Directorios más grandes** | Las carpetas más voluminosas bajo `/` |
| **GPU NVIDIA** | Estado de la tarjeta NVIDIA (`nvidia-smi`) |
| **GPU AMD** | Detección, actividad y temperatura de la tarjeta AMD |
| **NCDU** | Explorador interactivo del espacio en disco (ofrece instalar `ncdu` si falta) |
| **btop** | Monitor del sistema en vivo (ofrece instalar `btop` si falta) |
| **Ajustes de NVIDIA** | Abre el panel de control de NVIDIA |
| **Información del equipo** | Informe completo del hardware: CPU, memoria, dispositivos |
| **E/S de disco** | Estadísticas de lectura y escritura en disco |

### Esenciales de Linux

| Botón | Qué te muestra |
|-------|----------------|
| **Procesos en marcha** | Todos los procesos, ordenados por uso de CPU |
| **Información del sistema** | Versión del núcleo y distribución de Linux |
| **Usuarios conectados** | Quién está conectado ahora mismo (`w`) |
| **Últimos accesos** | Historial de conexiones |
| **Servicios fallidos** | Servicios que se han caído o no han arrancado |
| **Diario del sistema** | Últimas 50 líneas del registro del sistema |
| **Mensajes del núcleo** | Mensajes del hardware y de los controladores |
| **Vaciar la papelera** | Vacía tu carpeta de papelera |
| **Actualizar el sistema** | Actualiza tu sistema (funciona en Ubuntu, Fedora y Arch) |
| **Reiniciar** | Reinicia el ordenador |
| **Apagar** | Apaga el ordenador |
| **Ver el syslog** | Últimas 50 líneas del registro del sistema |

!!! warning
    **Reiniciar** y **Apagar** llevan activada la opción **Confirmar antes de ejecutar**: aparecerá una ventana pidiéndote confirmación antes de que ocurra nada.

### Red

| Botón | Qué te muestra |
|-------|----------------|
| **Interfaces de red** | Tus direcciones IP y tus tarjetas de red (`ip addr`) |
| **Conexiones activas** | Conexiones TCP establecidas |
| **Puertos abiertos** | Servicios a la escucha en tu máquina |
| **Servicios a la escucha** | Servicios escuchando en puertos TCP |

---

## Empieza pulsando cosas

Pulsa **Uso del disco**. Se abre una pequeña ventana con la información de tus discos. Pulsa **Uso de memoria**. Prueba unos cuantos más.

No puedes romper nada pulsando estos botones: solo leen información. Los dos que sí hacen algo (Reiniciar y Apagar) piden confirmación antes.

---

## Despejar: desinstalar un pack u ocultar una categoría

Los botones por defecto llegan como **packs de botones**. Si un conjunto entero no te sirve, lo más limpio es **desinstalar el pack**: abre el menú → **Packs de botones**, búscalo y pulsa **Desinstalar**. Sus botones desaparecen, y puedes reinstalar el pack cuando quieras con un toque.

Si prefieres solo apartar una categoría de la vista sin quitar nada, puedes ocultarla:

1. Abre **Preferencias → Categorías**
2. Desactiva la categoría

Una categoría oculta y sus botones dejan de verse, pero no se borran: puedes recuperarlos desde el mismo sitio cuando quieras.

---

## Cambiar el nombre o el color de un botón

Los nombres por defecto son funcionales pero genéricos. Puedes renombrarlos o cambiarles el color a tu gusto, y esto es **gratis para todo el mundo**, sin necesidad de Pro.

Clic derecho en cualquier botón → **Editar**:

- Cambia la **Etiqueta** por algo más cercano (`Uso del disco` → `¿Cómo va mi disco?`)
- Elige un **Color** para que los botones importantes destaquen
- Cambia el **Icono** por uno que te diga algo

---

## Crea tu primer botón

Los botones personalizados son **gratuitos e ilimitados**. Aquí tienes uno fácil para empezar:

1. Pulsa `Ctrl+N` (o el **+**)
2. **Etiqueta:** `Mi dirección IP`
3. **Comando:** `hostname -I`
4. **Modo de ejecución:** `Mostrar la salida`
5. Pulsa **Guardar**

Ya tienes una forma de ver tu IP local con un clic.

---

## ¿Y si un botón da error?

Algunos botones necesitan programas que quizá no estén instalados:

- **Temperatura** necesita `lm-sensors` (`sudo apt install lm-sensors`)
- **NCDU** y **btop** se ofrecen a instalarse solos la primera vez que los usas
- Si instalas el pack de **Desarrollo**, sus botones de Docker, Python y Node necesitan esas herramientas instaladas

Si un comando falla, se abre una ventana con el error exacto. Normalmente es un paquete que falta: copia su nombre e instálalo.

---

## Sacarle más partido a Commandeck

Cuando te sientas cómodo con los botones por defecto:

- [Crea botones a medida](../quick-start.md#3-create-your-first-custom-button) para tus comandos frecuentes
- [Ordena con categorías](../reference/main-window.md#category-filter) para agrupar botones relacionados
- [Ajusta la cuadrícula](../reference/preferences.md#button-grid-layout) a tu pantalla
- Plantéate [Commandeck Pro](../pro.md) cuando quieras gestionar un servidor remoto
