# Integración con IA (MCP)

!!! warning "Experimental"
    La integración con IA es experimental. El soporte de herramientas y el comportamiento cambian según el modelo y el cliente. Los resultados no están garantizados: revisa siempre lo que la IA crea o modifica.

Commandeck incluye un servidor MCP (Model Context Protocol). Una vez configurado, tu asistente de IA puede leer y gestionar tus botones directamente, sin copiar y pegar y sin explicarle tu instalación.

> *«Añade un botón llamado "Reiniciar Nginx" que ejecute `sudo systemctl restart nginx` en la categoría Servidor»*

!!! info "Necesita Commandeck 2.0.17 o posterior (Pro)"
    MCP es una función **Pro**. Las instrucciones de abajo arrancan el servidor desde la propia aplicación con `--mcp-server`, disponible a partir de la **2.0.17**. Mira tu versión en **Menú ☰ → Acerca de**.

## Paso 1 — Activa el acceso MCP en Commandeck

MCP está **desactivado de fábrica**. Actívalo una vez:

**Preferencias → Integración con el escritorio → Permitir el acceso MCP**

![Preferencias — interruptor de acceso MCP](../assets/preferences-mcp.png)

## Paso 2 — Encuentra tu comando MCP de Commandeck

El servidor MCP va incluido en la aplicación: se arranca ejecutando Commandeck con el parámetro `--mcp-server`. El comando exacto depende de cómo lo hayas instalado. Busca el tuyo aquí abajo; lo usarás en tu cliente de IA en el paso 3.

=== "Linux (AppImage)"

    Es la instalación más habitual. Usa el AppImage **Pro** (MCP es una función Pro) y asegúrate de que es ejecutable (`chmod +x` una vez):

    ```bash
    /ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Usa *tu* nombre de archivo y tu ruta reales (la descarga lleva la versión y la arquitectura en el nombre). Truco: arrastra el AppImage a una terminal para obtener su ruta completa.

=== "macOS"

    El ejecutable está dentro del paquete `.app`:

    ```bash
    /Applications/Commandeck.app/Contents/MacOS/Commandeck --mcp-server
    ```

=== "Windows"

    Usa la ruta donde instalaste Commandeck (entre comillas si contiene espacios):

    ```powershell
    "C:\Program Files\Commandeck\Commandeck.exe" --mcp-server
    ```

!!! tip "Pruébalo una vez"
    Al ejecutar el comando directamente debería quedarse esperando entrada (habla JSON-RPC por la entrada y la salida estándar): eso significa que funciona. Pulsa `Ctrl+C` para salir. Si escribe *«the MCP server requires Commandeck Pro»*, estás usando la versión gratuita.

En el resto de esta página, **`<tu comando de Commandeck>`** significa el ejecutable de este paso (por ejemplo, la ruta del AppImage), y **`--mcp-server`** es su parámetro.

## Paso 3 — Configura tu cliente de IA

Elige tu herramienta abajo. La configuración se hace una vez; después funciona sola.

=== "Claude Desktop"

    **Ubicación del archivo de configuración:**

    | Sistema | Ruta |
    |---------|------|
    | Linux | `~/.config/Claude/claude_desktop_config.json` |
    | macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
    | Windows | `%APPDATA%\Claude\claude_desktop_config.json` |

    Añade esto al archivo (créalo si no existe), con tu comando del paso 2:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    En macOS, `command` sería `/Applications/Commandeck.app/Contents/MacOS/Commandeck`; en Windows, la ruta completa a `Commandeck.exe`. Reinicia Claude Desktop: Commandeck aparece como herramienta conectada.

=== "Claude Code"

    Ejecuta esto una vez en una terminal (cambia el comando por el tuyo):

    ```bash
    claude mcp add commandeck /ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Para comprobarlo: `claude mcp list`

=== "Cursor"

    Edita `~/.cursor/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    Reinicia Cursor.

=== "Windsurf"

    Edita `~/.codeium/windsurf/mcp_config.json`:

    ```json
    {
      "mcpServers": {
        "commandeck": {
          "command": "/ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage",
          "args": ["--mcp-server"]
        }
      }
    }
    ```

    Reinicia Windsurf.

=== "Continue.dev"

    Añade esto a `.continue/config.yaml` en tu proyecto:

    ```yaml
    mcpServers:
      - name: commandeck
        command: /ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage
        args:
          - --mcp-server
    ```

    Las herramientas MCP solo están disponibles en **modo Agente**.

=== "Open WebUI (llama.cpp / Ollama)"

    Open WebUI se conecta a las herramientas por HTTP, no por stdio. Usa [mcpo](https://github.com/open-webui/mcpo) (el proxy oficial de Open WebUI) para hacer de puente con Commandeck.

    !!! warning "Ejecuta mcpo con el mismo usuario que usa Commandeck"
        El servidor lee los botones de **quien lo arranca**. Cada usuario de Linux o macOS tiene su propia configuración de Commandeck (`~/.config/commandeck`). Si ejecutas mcpo con un usuario distinto del que usas para Commandeck, la IA verá el conjunto de botones *equivocado* (o vacío). Arranca mcpo desde una terminal abierta con tu usuario habitual de escritorio.

    **Paso 1 — Instala mcpo (una vez):**

    ```bash
    pipx install mcpo
    # ¿sin pipx? un entorno virtual también funciona bien:
    #   python3 -m venv ~/.mcpo-venv && ~/.mcpo-venv/bin/pip install mcpo
    # (`pip install mcpo` a secas suele fallar en Linux con "externally-managed-environment")
    ```

    **Paso 2 — Averigua la IP local de la máquina donde corre Commandeck (solo si Open WebUI está en otra máquina):**

    ```bash
    hostname -I | awk '{print $1}'
    ```

    Apunta esa IP: la necesitarás en el paso 4.

    **Paso 3 — Arranca el proxy (deja esta terminal abierta):**

    ```bash
    mcpo --port 8000 -- /ruta/completa/a/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    ```

    Deberías ver: `Uvicorn running on http://0.0.0.0:8000`

    !!! tip "Cuidado con los saltos de línea al pegar"
        Mantén el comando en **una sola línea**. Si al pegarlo se parte en varias líneas rotas, guárdalo mejor como un pequeño guion: crea `start-mcpo.sh` con la línea de arriba y ejecuta `bash start-mcpo.sh`.

    **Paso 4 — Añade el servidor de herramientas en Open WebUI:**

    Ve a **Panel de administración → Ajustes → Herramientas** (en versiones antiguas: *Integraciones → Gestionar servidores de herramientas*) → **`+`** y rellena:

    | Campo | Valor |
    |-------|-------|
    | Tipo | **OpenAPI** |
    | Nombre | `commandeck` |
    | URL | `http://<ip-del-paso-2>:8000` |
    | Autenticación | Ninguna |

    !!! warning "Usa la IP de la máquina, no localhost"
        Si Open WebUI corre en otra máquina (por ejemplo, un servidor de casa), `localhost` apuntaría a ese servidor y no a la máquina donde está mcpo. Usa la IP del paso 2. Desde la máquina de Open WebUI puedes comprobar la ruta con `curl http://<esa-ip>:8000/openapi.json` (debería devolver JSON). Si no, abre el puerto 8000 en el cortafuegos de la máquina donde corre mcpo.

    **Paso 5 — Activa la herramienta en una conversación:**

    Empieza una conversación nueva, pulsa el icono **`+`** (herramientas) junto al campo de texto y activa **commandeck**.

    !!! tip
        Esto funciona con cualquier motor compatible con Open WebUI: llama.cpp, Ollama, APIs compatibles con OpenAI, etc. La capa de herramientas no depende del modelo. El soporte de llamadas a herramientas varía según el modelo: los ajustados a instrucciones suelen funcionar mejor; los modelos locales pequeños pueden necesitar el [mensaje de sistema](#recommended-system-prompt) de abajo para llamarlas de forma fiable.

    ---

    **Cuándo hay que reiniciar mcpo**

    mcpo arranca el servidor MCP de Commandeck como subproceso al iniciarse y lee su lista de herramientas **una sola vez**. Reinicia mcpo cada vez que:

    - **Actives o desactives «Permitir el acceso MCP»** en Preferencias (si arrancas mcpo antes de activarlo, ve cero herramientas)
    - Actualices Commandeck a una versión nueva

    Para reiniciarlo: pulsa `Ctrl+C` en la terminal de mcpo y vuelve al paso 3; o, con el servicio de systemd de abajo, `systemctl --user restart mcpo-commandeck`.

    ---

    **Paso 6 — (Opcional) Que mcpo sobreviva a los reinicios**

    Crea un servicio de usuario de systemd para que mcpo arranque solo al iniciar sesión (ejecútalo **con tu usuario habitual de escritorio**):

    ```bash
    mkdir -p ~/.config/systemd/user
    cat > ~/.config/systemd/user/mcpo-commandeck.service << 'EOF'
    [Unit]
    Description=mcpo proxy for the Commandeck MCP server

    [Service]
    ExecStart=%h/.local/bin/mcpo --port 8000 -- %h/Apps/Commandeck-Pro-2.0.17-Linux-x86_64.AppImage --mcp-server
    Restart=on-failure
    RestartSec=5

    [Install]
    WantedBy=default.target
    EOF

    systemctl --user daemon-reload
    systemctl --user enable --now mcpo-commandeck
    ```

    Comandos útiles:

    ```bash
    systemctl --user status mcpo-commandeck    # ver el estado
    systemctl --user restart mcpo-commandeck   # reiniciar tras activar MCP o actualizar
    systemctl --user stop mcpo-commandeck      # parar
    journalctl --user -u mcpo-commandeck -f    # registros en vivo
    ```

    !!! note
        Ajusta las rutas de `ExecStart`: apunta a *tu* AppImage y ejecuta `which mcpo` para saber dónde está mcpo si no es `~/.local/bin/mcpo` (por ejemplo, dentro de un entorno virtual).

---

## Mensaje de sistema recomendado

Pega el texto de abajo en el campo de mensaje de sistema de tu cliente de IA. Prepara al modelo para que llame primero a `help`, siga los flujos de búsqueda correctos y descomponga los comandos complejos en piezas de Commandeck en lugar de pegarlos tal cual.

!!! note "Se deja en inglés a propósito"
    Este texto va dirigido al modelo, no a ti. Los nombres de las herramientas y los campos son ingleses: tradúcelo y las llamadas se vuelven menos fiables.

```
You are an assistant for Commandeck, a desktop application on Linux, macOS or Windows. Commandeck
lets the user run commands by clicking buttons, like a remote control. You can create, read,
and modify the user's buttons, machines, and profiles using your tools.

Rules:
- Before doing anything, call the help tool to read the instructions.
- When the user explicitly names a button, use get_button(name="X") directly. When you don't
  know the exact name, use list_buttons.
- Never call get_button before create_button.
- For buttons: a duplicate means SAME NAME, not same command. If no button has the exact same
  name, create it without asking.
- For machines: a duplicate means SAME HOST address. Always call list_machines and check by
  host before creating.
- For profiles: a duplicate means same name. Call list_profiles before creating.
- When asked to change a property, always apply the change. Never decide the current value is
  already acceptable.
- In multi-step requests, if a required resource exists, use it and proceed.
- When you need a machine ID or profile ID, always look it up first.
- Write each command in the right shell for its target: PowerShell or cmd for a Windows machine,
  bash/sh for Linux or macOS. Set the button's os field to match. Check each machine's os with
  list_machines; for a local button (no machine) use this computer's OS. Never give a Windows
  machine a bash command, or a Linux/macOS machine a PowerShell command.
- The user can install ready-made button packs from the gallery: call list_packs to see what is
  available and what has updates, then install_pack / update_pack / uninstall_pack to manage them.

When a user asks you to add or refactor a shell command, decompose it before creating a button:
1. `cd /some/path` → Execution Profile working_dir (strip from command)
2. `sudo -u user` wrapper → run_as_user on the profile or button's run_as field
   (strip the wrapper, keep the inner command)
3. Opens an interactive shell (bash, zsh, exec bash) → execution_mode = "terminal"
4. Produces output the user wants to read → execution_mode = "output"; fire-and-forget → "silent"
5. What remains after stripping context wrappers is the command field.

Example: `sudo -u www-data bash -c 'cd /var/www/myapp && git pull'`
→ Create Profile: name="Web Deploy", run_as_user="www-data", working_dir="/var/www/myapp"
→ Create button: command="git pull", execution_mode="output", assign that profile
```

=== "Open WebUI"

    En Open WebUI, ve a **Panel de administración → Ajustes → Mensaje de sistema** y pega el texto de arriba (o ponlo en el mensaje de sistema de la conversación, dentro de los ajustes del modelo).

=== "Claude Desktop"

    Claude Desktop no ofrece un campo de mensaje de sistema. La descripción de la herramienta `help` se explica por sí sola para Claude: no hace falta ningún texto extra.

=== "Otros clientes"

    Pega el texto en el campo de mensaje de sistema o de instrucciones que ofrezca tu cliente, antes de empezar la conversación.

---

## Qué puede hacer tu IA

**Botones**

| Herramienta | Descripción |
|-------------|-------------|
| `help` | Devuelve la guía completa de trabajo: hay que llamarla siempre primero |
| `list_buttons` | Enumera todos los botones, con filtro opcional por categoría |
| `get_button` | Da los detalles de un botón por nombre o identificador |
| `create_button` | Crea un botón nuevo (nombre, comando, categoría, color, icono, modo de ejecución, perfil, máquinas…) |
| `update_button` | Modifica cualquier campo de un botón existente; llama antes a `get_button` para obtener su identificador |
| `execute_button` | Ejecuta el comando de un botón y devuelve su salida (desactivado de fábrica; consulta [Permitir que la IA ejecute botones](#allowing-ai-to-run-buttons)) |
| `delete_button` | Borra un botón por su identificador |

**Categorías**

| Herramienta | Descripción |
|-------------|-------------|
| `list_categories` | Enumera los nombres de todas las categorías |

**Máquinas SSH** *(función Pro)*

| Herramienta | Descripción |
|-------------|-------------|
| `list_machines` | Enumera las máquinas SSH configuradas (nombre, anfitrión, usuario, puerto; nunca las claves privadas) |
| `create_machine` | Añade una máquina SSH |
| `update_machine` | Renombra o reconfigura una máquina SSH; llama antes a `list_machines` para obtener su identificador |
| `delete_machine` | Borra una máquina SSH por su identificador |

**Perfiles de ejecución** *(función Pro)*

| Herramienta | Descripción |
|-------------|-------------|
| `list_profiles` | Enumera todos los perfiles de ejecución |
| `get_profile` | Da los detalles de un perfil por nombre o identificador |
| `create_profile` | Crea un perfil reutilizable (usuario de ejecución, carpeta de trabajo) |
| `update_profile` | Modifica un perfil existente; llama antes a `get_profile` para obtener su identificador |
| `delete_profile` | Borra un perfil por su identificador |

**Packs de botones** — conjuntos ya preparados, desde la galería pública

| Herramienta | Descripción |
|-------------|-------------|
| `list_packs` | Enumera los packs de la galería, con las marcas `installed` y `update_available` |
| `install_pack` | Instala un pack en unas máquinas (solo packs con firma verificada) |
| `update_pack` | Actualiza un pack instalado conservando tus cambios, tus destinos y tus posiciones |
| `uninstall_pack` | Quita todos los botones de un pack |
| `export_pack` | Exporta los botones elegidos a un archivo `.cdpack` que se puede compartir |

**Variables**

| Herramienta | Descripción |
|-------------|-------------|
| `list_variable_values` | Enumera tus valores guardados para las `{{variables}}` de los comandos |

!!! warning "Revisa antes de borrar"
    `delete_button`, `delete_machine` y `delete_profile` están disponibles por MCP. Verifica siempre el elemento correcto con `get_button` o `list_machines` antes de pedirle a tu IA que borre nada.

!!! tip "Refrescar la cuadrícula tras los cambios de la IA"
    Cuando la IA crea o modifica un botón, pulsa **F5** (o menú → Recargar los botones) para refrescar la cuadrícula sin reiniciar Commandeck.

!!! tip "Consejo para modificar botones"
    Si la IA dice que no puede modificar un botón, pídele que llame primero a `get_button` con el nombre del botón para obtener su identificador y luego a `update_button` con ese identificador.

---

## Permitir que la IA ejecute botones

De fábrica, tu IA puede **leer y editar** botones, pero no **ejecutarlos**. Para dejarle disparar comandos de verdad tienes que dar tu permiso en tres niveles; con que uno esté desactivado, la ejecución se bloquea.

**1. Interruptor general** — *Preferencias → Integración con el escritorio → Permitir la ejecución por la IA*

Desactivado de fábrica. Es el interruptor maestro de toda la función.

**2. Permiso por botón** — *Editar un botón → Comportamiento → Permitir que la IA ejecute este botón*

Desactivado de fábrica en todos los botones, incluidos los que ya tenías. Actívalo solo en los botones cuyos comandos te resulte cómodo dejar en manos de una IA: comprobaciones de solo lectura (`df -h`, `systemctl status`), operaciones que se pueden repetir sin daño, despliegues seguros.

**3. Confirmación** — *Editar un botón → Comportamiento → Confirmar antes de ejecutar*

Con esto activado, la IA no puede ejecutar el botón en silencio. Recibe una respuesta `requires_confirmation` con el comando exacto y la instrucción de enseñártelo y esperar tu aprobación antes de volver a llamar con `confirmed=true`. Recomendado para cualquier comando delicado (reinicios, borrados, sudo).

**Registro de auditoría:** cada ejecución por MCP se añade a `~/.config/commandeck/.mcp_executions.log` con la fecha y hora, el nombre del botón, la máquina de destino, el código de salida y la duración.

**Limitaciones:**

- Los botones en modo `Abrir en terminal` no se pueden ejecutar por MCP: no hay ninguna terminal en un contexto de IA sin interfaz. La IA recibe un error si lo intenta.
- La salida que se devuelve a la IA está limitada (4 KB de salida estándar y 2 KB de errores) para no llenar su contexto. La salida completa sigue estando en el registro si la necesitas.
- Los botones con varios destinos obligan a la IA a indicar en qué máquina ejecutar. Si no lo hace, el servidor le devuelve la lista de destinos válidos y le pide que aclare.

---

## Seguridad

El servidor MCP usa **transporte stdio**: cuando un cliente (Claude Desktop, Cursor…) lo arranca directamente, funciona como subproceso y se comunica solo por la entrada y la salida estándar. No se abre ningún puerto de red, y solo el proceso que lo arrancó puede hablar con él.

Cuando usas **mcpo** (Open WebUI) *sí* se abre un puerto HTTP (el 8000) en la máquina donde corre mcpo. Asegúrate de que ese puerto no queda expuesto a redes en las que no confías: déjalo en tu red local, detrás del cortafuegos.

!!! warning
    Con el acceso MCP activado, tu asistente de IA puede crear, modificar y borrar botones. Desactiva el interruptor en Preferencias cuando no lo necesites. La **ejecución** de botones es una función aparte que hay que autorizar; consulta [Permitir que la IA ejecute botones](#allowing-ai-to-run-buttons).
