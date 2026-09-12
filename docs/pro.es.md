# Commandeck Pro

Commandeck viene en dos ediciones: **Gratis** (solo ejecución local) y **Pro** (todas las funciones, con SSH e integración con IA).

## Gratis frente a Pro

| | Gratis | Pro |
|--|--------|-----|
| Ejecución local de comandos | Ilimitada | Ilimitada |
| Botones personalizados | Ilimitados | Ilimitados |
| Botones por defecto | Visibles, ejecutables, editables, eliminables | Igual |
| Variables de comando (`{{…}}`) y valores guardados | ✓ | ✓ |
| Máquinas SSH | — | Ilimitadas |
| Botones multimáquina | — | ✓ |
| Selección múltiple y acciones en grupo | — | ✓ |
| Temas de botones (Bold, Phone, Neon, Retro…) | — | ✓ |
| Tema CSS a medida | — | ✓ |
| Perfiles de ejecución | — | ✓ |
| Copia y restauración de la configuración | — | ✓ |
| Servidor MCP (integración con IA) | — | ✓ |
| Ejecución de botones por la IA | — | ✓ |

!!! note
    Gratis y Pro son **descargas distintas**, no el mismo programa desbloqueado con una licencia. La versión gratuita no contiene nada de código Pro.

## Precio

**29 $, pago único. Se compra una vez y es tuyo para siempre.** Sin suscripción y sin renovaciones: la versión que compras sigue funcionando de por vida. Una futura versión mayor (Commandeck 2) sería una compra aparte; todo lo que hayas comprado sigue siendo tuyo.

[Conseguir una licencia →](https://neurocontrarian.lemonsqueezy.com/checkout/buy/9c16845a-8ab6-4a36-b8da-9874d9d64f33){ .md-button .md-button--primary }

## Prueba gratuita de 14 días

La versión Pro incluye una **prueba de 14 días** que empieza sola la primera vez que la abres. Sin clave, sin pago y sin pedirte el correo: todas las funciones Pro están disponibles de inmediato.

Unos días antes de que acabe la prueba, Commandeck te muestra una oferta dentro de la aplicación con un código de descuento. Pasado el día 14, las funciones Pro quedan en solo lectura (en gris): tus botones, tus máquinas y tus ajustes **no se borran nunca**.

Para seguir usando Pro, activa una licencia en **Preferencias → Licencia**.

## Activar la licencia

1. Abre **Preferencias** (`Ctrl+,`)
2. Baja hasta la sección **Licencia**
3. Escribe el correo electrónico usado en la compra
4. Pega tu clave de licencia
5. Pulsa **Activar Pro**

Solo hace falta conexión a internet para la activación inicial. Después, Commandeck funciona perfectamente sin conexión: el uso diario no necesita red. Cuando estés en línea, vuelve a comprobar la licencia de vez en cuando en segundo plano; cuando no lo estés, simplemente sigue activa.

## Desactivar

Para quitar la licencia de un dispositivo: **Preferencias → Licencia → Desactivar la licencia**.

Así se libera una plaza de activación y puedes usar la misma clave en otro dispositivo. Tu licencia Pro permite hasta **3 activaciones simultáneas en ordenadores** (Linux, macOS, Windows) que uses personalmente; consulta [Licencia y dispositivos](pro/license-devices.md) para los detalles.

!!! note "Android es un producto aparte"
    La licencia de escritorio cubre **solo el escritorio** (Linux, macOS, Windows). La aplicación de Android es un producto aparte, disponible en Google Play con su propia facturación, y no está cubierta por la clave de escritorio.

Los límites de la versión gratuita se aplican en cuanto desactivas. Tus botones no se borran; las funciones Pro vuelven en cuanto reactivas.

## Perfiles de ejecución *(Pro)*

Crea contextos de ejecución reutilizables que reúnen un usuario de destino, una carpeta de trabajo y una contraseña de sudo en un único perfil con nombre.

Asigna un perfil a cualquier botón: al ejecutarse, el comando corre con el usuario indicado en la carpeta indicada, con la contraseña de sudo suministrada automáticamente (sin que ninguna terminal la pida).

Los perfiles valen tanto para la ejecución local como para la remota (SSH), incluido el modo **Abrir en terminal**.

Gestiona los perfiles desde el menú → **Gestionar perfiles**.

---

## Copia y restauración *(Pro)*

Exporta e importa toda tu configuración desde **Preferencias**:

- **Copia de botones**: exporta tus botones a un archivo `.cdbackup` (solo los botones)
- **Copia de máquinas**: exporta las definiciones de máquinas SSH a un archivo `.cdmachines` (las claves privadas SSH nunca se incluyen)

La restauración está en la misma sección de Preferencias. Al importar botones se fusionan con los que ya hay por defecto: los botones por defecto añadidos recientemente nunca se pierden.

---

## Integración con IA *(Pro)*

El servidor MCP permite que asistentes de IA como Claude, Cursor u Open WebUI lean, editen y ejecuten tus botones mediante una única conexión segura. Consulta [Integración con IA (MCP)](pro/mcp.md) para la instalación completa y los detalles de seguridad.
