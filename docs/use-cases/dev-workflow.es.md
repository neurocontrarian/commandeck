# Caso de uso: flujo de desarrollo

Esta guía muestra cómo usar Commandeck como paleta de comandos de quien programa. El objetivo: sustituir los comandos de terminal más repetitivos por botones de un clic, organizados por proyecto.

!!! tip "Función Pro"
    Este flujo ejecuta comandos en un servidor remoto por SSH. **Las máquinas SSH, los botones multimáquina y los perfiles de ejecución requieren [Commandeck Pro](../pro.md).** Los botones puramente locales de esta guía funcionan en la versión gratuita.

## El escenario

Trabajas en dos proyectos:

- Un **frontend** (aplicación React, en local)
- Una **API de backend** (Node.js, desplegada en un servidor remoto)

Ejecutas los mismos comandos decenas de veces al día: compilar, probar, desplegar, mirar registros. Commandeck sustituye tu memoria muscular por botones visibles y etiquetados.

---

## Paso 1 — Añade tu servidor como máquina SSH

Para los comandos que se ejecutan en el servidor, añádelo primero:

| Campo | Valor |
|-------|-------|
| Nombre | `Servidor de producción` |
| Anfitrión | `ip-de-tu-servidor` |
| Usuario SSH | `deploy` |
| Ruta de la clave SSH | `~/.ssh/id_ed25519` |

Pulsa **Probar** para comprobar la conexión.

!!! tip "Función Pro"
    Las máquinas SSH requieren [Commandeck Pro](../pro.md).

---

## Paso 2 — Categoría «Frontend»

Crea estos botones con **Categoría: Frontend**.

### Instalar dependencias

```
npm install
```

- Modo de ejecución: **Mostrar la salida** (para ver si algo falla)
- Consejo sobre la carpeta de trabajo: antepón `cd ~/proyectos/miapp &&`

Comando completo: `cd ~/proyectos/miapp && npm install`

---

### Arrancar el servidor de desarrollo

```
cd ~/proyectos/miapp && npm run dev
```

- Modo de ejecución: **Abrir en terminal** — el servidor de desarrollo es interactivo y escribe sin parar

---

### Compilar para producción

```
cd ~/proyectos/miapp && npm run build
```

- Modo de ejecución: **Mostrar la salida** — quieres ver los errores de compilación
- Icono: `package-x-generic-symbolic`

---

### Lanzar las pruebas

```
cd ~/proyectos/miapp && npm test -- --watchAll=false
```

- Modo de ejecución: **Mostrar la salida**
- Descripción emergente: `Ejecutar toda la batería de pruebas una vez`

---

### Análisis de estilo

```
cd ~/proyectos/miapp && npm run lint
```

- Modo de ejecución: **Mostrar la salida**
- Color: `#1c71d8` (azul: informativo)

---

## Paso 3 — Categoría «Backend»

Crea estos botones con **Categoría: Backend** y destino `Servidor de producción`.

### Traer el código más reciente

```
cd ~/app && git pull origin main
```

- Modo de ejecución: **Mostrar la salida**
- Confirmar antes de ejecutar: activado (evita despliegues accidentales)

---

### Reiniciar la API

```
sudo systemctl restart miapp
```

- Modo de ejecución: **Silencioso**
- Confirmar antes de ejecutar: activado

---

### Docker: reconstruir y reiniciar

```
cd ~/app && docker compose down && docker compose up -d --build
```

- Modo de ejecución: **Mostrar la salida**
- Descripción emergente: `Reconstruir los contenedores y reiniciar (unos 30 s)`
- Color: `#26a269` (verde: acción de despliegue)

---

### Seguir los registros de la aplicación

```
sudo journalctl -u miapp -f -n 100
```

- Modo de ejecución: **Abrir en terminal** — `journalctl -f` escribe indefinidamente

---

### Ver los contenedores Docker

```
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

- Modo de ejecución: **Mostrar la salida**

---

### Copia de la base de datos

```
cd ~/app && pg_dump mibd > ~/copias/mibd_$(date +%Y%m%d).sql
```

- Modo de ejecución: **Mostrar la salida**
- Confirmar antes de ejecutar: activado
- Descripción emergente: `Volcar la base de datos de producción en ~/copias/`

---

## Paso 4 — Usa «Mostrar la salida» con criterio

No todos los comandos necesitan **Mostrar la salida**. Una buena regla:

| Usa **Silencioso** para | Usa **Mostrar la salida** para | Usa **Abrir en terminal** para |
|-------------------------|--------------------------------|--------------------------------|
| Reinicios de servicios | Compilaciones y pruebas | Procesos interactivos (`htop`, `vim`, `psql`) |
| Disparadores simples | Comandos que pueden fallar | Flujos largos (`tail -f`, `docker logs -f`) |
| Despliegues en los que confías | Todo lo que escriba algo útil | Sesiones SSH |

---

## Paso 5 — Mudarse a otro servidor

Cuando cambies o migres el servidor no hace falta editar los botones uno a uno. Usa la [selección múltiple](../pro/multiselect.md) para reasignar todos los botones de Backend de golpe:

1. **Ctrl+clic** en cada botón de Backend (o selecciónalos todos con un recuadro): aparece la barra de acciones abajo
2. Pulsa **Máquina** en la barra de acciones
3. Elige el nuevo servidor

Todos los botones seleccionados se actualizan en una sola operación.

---

## Resultado

Dos categorías limpias — Frontend y Backend — en el desplegable superior te dan exactamente los comandos que necesitas. Tu terminal sigue abierta para lo exploratorio; Commandeck se encarga de lo repetitivo.

!!! tip
    Mantén entre 6 y 10 botones por categoría. Con más, navegar se vuelve tan incómodo como la propia terminal.
