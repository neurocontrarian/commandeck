# Caso de uso: pilotar Commandeck desde una IA local

!!! tip "Función Pro"
    La integración con IA (MCP) requiere [Commandeck Pro](../pro.md).

🔰 **La idea:** en lugar de crear los botones a mano, se lo *pides* a un asistente de IA — «añade un botón que reinicie Nginx en la categoría Servidor» — y él lo crea. La IA puede leer tus botones, tus máquinas y tus perfiles y, si se lo permites, ejecutarlos. Funciona con asistentes en la nube como Claude **y** con un modelo totalmente local que corra en tu propio equipo.

Esta página recorre el camino del modelo local de principio a fin con **Open WebUI** y un modelo local (por ejemplo Llama o Gemma). Para la lista completa de clientes y opciones, consulta la [referencia de integración con IA](../pro/mcp.md).

## ¿Por qué local?

Un modelo local mantiene todo dentro de tu máquina: tus botones, tus comandos y los nombres de tus servidores nunca salen de tu red. Ideal para un homelab y para quien cuida su privacidad.

## Paso a paso

### 1. Activa el acceso MCP

**Preferencias → Integración con el escritorio → Permitir el acceso MCP.**

![Permitir el acceso MCP](../assets/preferences-desktop.png)

### 2. Arranca el servidor MCP de Commandeck

El servidor va incluido en la aplicación. Ejecuta tu Commandeck con `--mcp-server`:

```bash
/ruta/a/Commandeck-Pro-VERSION-Linux-x86_64.AppImage --mcp-server
```

!!! warning "Ejecútalo con el usuario que usa Commandeck"
    El servidor lee los botones de **quien lo arranca**. Lánzalo desde una terminal abierta con tu usuario habitual de escritorio, o la IA verá el conjunto de botones equivocado (o vacío).

### 3. Haz de puente hacia Open WebUI con mcpo

Open WebUI habla con las herramientas por HTTP, así que pon delante el proxy [mcpo](https://github.com/open-webui/mcpo):

```bash
mcpo --port 8000 -- /ruta/a/Commandeck-Pro-VERSION-Linux-x86_64.AppImage --mcp-server
```

Después, en Open WebUI: **Panel de administración → Ajustes → Herramientas → +**, tipo **OpenAPI**, URL `http://<ip-de-la-máquina>:8000`. Si Open WebUI corre en otro equipo, usa la IP de la máquina donde se ejecuta mcpo, no `localhost`.

### 4. Habla con tus botones

Abre una conversación, activa la herramienta **commandeck**, pega el [mensaje de sistema recomendado](../pro/mcp.md#recommended-system-prompt) y prueba con:

> *«Enumera mis botones.»*
> *«Añade un botón llamado "Espacio en disco" que ejecute `df -h` en la categoría Sistema.»*

Pulsa **F5** en Commandeck (o **menú → Recargar los botones**) para refrescar la cuadrícula y ver aparecer los botones nuevos, sin reiniciar nada.

⚙️ **Notas para usuarios avanzados**

- **El modelo importa.** La capa de herramientas no depende del modelo, pero la calidad de las llamadas varía mucho. Los modelos ajustados a instrucciones funcionan mejor; los modelos locales pequeños suelen necesitar el mensaje de sistema para llamar a las herramientas de forma fiable.
- **Dejar que la IA *ejecute* botones** es un permiso aparte, con tres puertas (interruptor general + casilla por botón + confirmación opcional). Desactivado de fábrica. Consulta [Permitir que la IA ejecute botones](../pro/mcp.md#allowing-ai-to-run-buttons).
- **Mantener el puente activo:** un servicio de usuario de systemd conserva mcpo en marcha tras un reinicio; consulta la [referencia MCP](../pro/mcp.md).
