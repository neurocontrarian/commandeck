# Seguridad y cómo funciona

🔰 **En pocas palabras:** Commandeck solo ejecuta los comandos que *tú* escribes y pulsas, en tus propios ordenadores. Nunca guarda tus contraseñas en texto legible, nunca abre tu máquina a la red durante el uso normal y te pide confirmación en todo lo que hayas marcado como importante.

## ¿Por qué fiarse de este proyecto?

- **Se ejecuta en tu ordenador, no en la nube.** No hay ninguna cuenta que crear ni ningún servidor de una empresa guardando tus datos. Todo lo que Commandeck sabe se queda en tu máquina.
- **Pago único.** Pagas una vez y la versión que instalaste sigue funcionando. No hay suscripción que cancelar ni servidor que pueda apagarse un día y dejarte tirado.
- **Nada de telemetría, nunca.** Commandeck no tiene analíticas ni cuentas, y no envía ninguno de tus datos a ninguna parte: lo que pasa en tu máquina se queda en tu máquina.
- **Disponible en 11 idiomas**, y cada uno se mantiene como parte real de la aplicación, no como un añadido de última hora.

## Tus comandos, a la vista y editables

Cada botón muestra su comando en texto claro en el [editor de botones](button-editor.md). No hay nada escondido ni disfrazado: lo que ves es exactamente lo que se ejecuta al pulsar. Commandeck nunca cambia tus comandos a tus espaldas; lo único que añade alguna vez es la carpeta o la cuenta de usuario que tú mismo eliges en un perfil.

## Autenticación SSH

Cuando conectas Commandeck a otro ordenador (Pro), te identificas con una **clave SSH** (recomendado) o con una **contraseña**. En ambos casos, tu contraseña nunca se escribe en el disco de una forma que alguien pueda leer.

- Una contraseña guardada va al almacén seguro que ya trae tu sistema: el mismo cofre protegido que el sistema operativo usa para sus propias contraseñas (Llavero en macOS, Administrador de credenciales en Windows, GNOME Keyring o KWallet en Linux). **Nunca se copia en una copia de seguridad.**
- En algún sistema poco común que no tenga ese almacén seguro, Commandeck recurre a un archivo local cifrado que solo tu cuenta puede abrir, y te avisa claramente de que esa protección es más débil.
- **La primera vez que te conectas a una máquina nueva**, Commandeck te enseña su huella de identidad y te pide que la confirmes. Es la misma comprobación de seguridad que hace la herramienta `ssh` de siempre, pero en una ventana amable en lugar de una terminal.
- Si tu clave SSH está protegida con una frase de paso, Commandeck te lo dice claramente cuando algo hay que desbloquear, en lugar de fallar en silencio.

## Contraseñas de sudo

Algunos comandos necesitan una contraseña de administrador (sudo) para ejecutarse. Si decides guardar una en un [perfil](execution-profiles.md), se trata exactamente igual que una contraseña SSH: se guarda en el almacén seguro de tu sistema y **nunca se escribe en tus archivos de configuración ni en tus copias de seguridad**; ahí solo consta que existe una contraseña, jamás la contraseña. En un sistema sin almacén seguro, se recurre a un archivo cifrado atado a ese ordenador concreto (para que no pueda copiarse a otro), con un aviso claro. Cuando un comando la necesita, Commandeck se la pasa directamente al sistema, así no tienes que reescribirla en una terminal.

## Confirmación por botón

Cualquier botón puede llevar activado **Confirmar antes de ejecutar** (editor de botones → Comportamiento). Con eso encendido, Commandeck te enseña el comando exacto y espera tu visto bueno antes de hacer nada: una buena idea para reinicios, borrados y todo lo que pida contraseña de administrador.

## Acceso de la IA / MCP (Pro)

Commandeck puede conectarse a un asistente de IA para que te ayude a leer y ordenar tus botones. Es completamente opcional y se queda **apagado hasta que tú lo enciendes**. Varios cierres independientes te mantienen al mando:

- El asistente solo puede ver o cambiar tus botones después de que actives *Permitir el acceso MCP* en Preferencias.
- Antes de poder ejecutar un botón por ti, tienen que estar activados **tres** permisos distintos: un interruptor general, uno por botón y — para lo delicado — una confirmación final. Si falta uno solo, no se ejecuta nada.
- Cada acción del asistente se escribe en un registro de tu ordenador, con la hora, el botón, el resultado y lo que tardó, para que siempre puedas ver qué pasó exactamente.
- Cuando lo arranca un asistente de escritorio, la conexión se queda por completo dentro de tu ordenador y no abre ningún puerto de red. (Un complemento opcional, para una herramienta web concreta, sí abre una conexión local: si lo usas, mantenlo dentro de tu red doméstica, detrás del cortafuegos.)

## De qué te protege Commandeck

Commandeck es una **herramienta personal de escritorio**. Da por hecho que quien está sentado delante del ordenador tiene permiso para ejecutar comandos en sus propias máquinas.

Sus protecciones están para evitar *accidentes* y sorpresas: ejecutar algo equivocado por error, que una contraseña guardada se cuele en una copia de seguridad o en una carpeta sincronizada, o que un asistente de IA actúe sin tu permiso. Para eso están las confirmaciones, el almacenamiento seguro de contraseñas y los cierres de la IA.

Lo que **no** intenta hacer es proteger tu ordenador de alguien que ya se ha hecho con tu cuenta o que está sentado delante de tu máquina desbloqueada. Ninguna aplicación de escritorio puede: a esas alturas, esa persona podría ejecutar esos comandos por su cuenta de todas formas. Mantener tu ordenador y tu cuenta seguros (bloqueo de pantalla, una contraseña de acceso robusta) es la base sobre la que Commandeck se apoya.
