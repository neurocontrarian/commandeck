# Caso de uso: gestionar un parque homelab

!!! tip "Función Pro"
    Las máquinas SSH, los botones multimáquina y los perfiles de ejecución requieren [Commandeck Pro](../pro.md).

🔰 **El objetivo:** tienes unas cuantas máquinas en casa — un NAS, una Raspberry Pi, un servidor pequeño — y no paras de escribir los mismos comandos SSH para vigilarlas. Con Commandeck creas los botones una vez y los pulsas desde una sola ventana. Esta página junta las piezas: máquinas, botones multimáquina y perfiles.

## 1. Añade tus máquinas

**Menú ☰ → Gestionar máquinas → Añadir.** Dale a cada una un nombre, un anfitrión, un usuario y una clave SSH.

![Gestionar máquinas](../assets/machines-list.png)

En la primera conexión, Commandeck te muestra la huella digital del anfitrión y te pide que la confirmes (consulta [Seguridad](../reference/security.md)): no hace falta preparar `known_hosts` desde una terminal.

## 2. Un botón, varios servidores

En el [editor de botones](../reference/button-editor.md), dentro de **Máquinas de destino**, activa más de una máquina (puedes incluir **Local**). El botón se convierte en *multimáquina*: cada clic abre el selector para que elijas dónde ejecutarlo.

![Selector de máquina](../assets/machine-picker.png)

!!! example "Botón de revisión rápida"
    Comando `uptime && df -h`, con el NAS, la Pi y el servidor activados. Un solo botón responde a «¿cómo está cada máquina?»: eliges el destino cada vez.

## 3. Reutiliza condiciones de ejecución con perfiles

Si varios botones necesitan la misma cuenta de servicio o la misma carpeta de trabajo, guarda un [perfil de ejecución](../reference/execution-profiles.md) una vez y asócialo — por ejemplo un perfil **Despliegue** (*ejecutar como* `www-data`, carpeta `/var/www/app`) usado por todos los botones web.

## 4. Ordena por categorías

Agrupa los botones en categorías como *NAS*, *Pi* o *Docker* para que la cuadrícula siga siendo legible. Elige una categoría en el desplegable superior para filtrar.

⚙️ **Para administradores de sistemas**

- **En paralelo o en secuencia:** un botón multimáquina se ejecuta en **una** máquina por clic (mediante el selector). Para lanzar el mismo comando en todos los servidores a la vez, pasa por el selector una vez por anfitrión o mantén un botón por máquina dentro de una categoría.
- **Parque con sistemas mezclados:** hoy un botón contiene un solo comando. Si el destino usa un sistema distinto del que espera el comando (PowerShell frente a bash), puede que no funcione: de momento conviene mantener botones separados por sistema.
- **Automatízalo con IA:** apunta un modelo local a Commandeck mediante [MCP](local-ai.md) y pídele que cree máquinas, perfiles y botones para todo tu parque de una sola vez.
