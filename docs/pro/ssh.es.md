# SSH y multimáquina

!!! tip "Función Pro"
    Las máquinas SSH y los botones multimáquina requieren [Commandeck Pro](../pro.md).

Esta página cubre el flujo de trabajo propio de Pro para SSH: añadir máquinas, asignarlas a botones y usar el selector de máquina. Para la referencia campo por campo del diálogo de añadir máquina, consulta [Máquinas SSH](../reference/ssh-machines.md).

---

## Añadir tu primera máquina

1. Abre **Menú → Gestionar máquinas**
2. Pulsa **+** para abrir el diálogo de añadir máquina
3. Rellena el nombre, el anfitrión, el usuario SSH y cómo autenticarse: una **clave** SSH (recomendado) o una **contraseña**
4. Pulsa **Probar** para comprobar la conexión
5. Pulsa **Guardar**

La máquina ya está disponible en todos los editores de botones.

!!! note "Clave o contraseña"
    Las máquinas SSH se autentican con una **clave** (recomendado) o con una **contraseña**. Una contraseña guardada vive en el llavero de tu sistema, nunca en texto plano ni en una copia de seguridad. Consulta [Contraseña SSH](../reference/ssh-machines.md#ssh-password).

Para preparar una clave SSH (generar el par y copiarlo al servidor), consulta [Preparar la clave SSH](../reference/ssh-machines.md#ssh-key-setup).

---

## Asignar una máquina a un botón

Abre el editor de botones (crea uno nuevo o haz clic derecho en uno existente → **Editar**).

En la sección **Máquinas de destino**:

- Desactiva **Local** si solo quieres la máquina remota
- Activa la máquina o máquinas que quieras

Pulsa **Guardar**. La descripción emergente del botón muestra ahora el nombre de la máquina de destino.

---

## Botones de una sola máquina

Cuando hay exactamente un destino activado, el comando se ejecuta allí de inmediato: sin selector y sin clic de más. Es la configuración más habitual.

---

## Botones multimáquina

Activa dos o más destinos y el botón se convierte en multimáquina. Cada clic abre el [selector de máquina](../reference/ssh-machines.md#the-machine-picker).

El selector enumera cada destino activado con su nombre y su icono. Elige uno y pulsa **Ejecutar**.

![Selector de máquina](../assets/machine-picker.png)

### Mezclar local y remoto

Activa **Local** junto a una o varias máquinas SSH para incluir tu propio ordenador como opción del selector. Útil para guiones que funcionan igual en ambos entornos.

### El atajo «Todas las máquinas»

En el editor de botones, el interruptor **Todas las máquinas**, arriba de la lista, selecciona de golpe todas las máquinas configuradas. Va bien cuando quieres un comando como `df -h` disponible en todo tu parque sin ir marcando casillas.

---

## Patrones prácticos

### El mismo comando en varios servidores

Crea un botón con todas las máquinas de destino activadas. El selector te deja elegir a qué servidor preguntar cada vez.

### Comandos en paralelo en varios servidores

El selector de máquina admite selección múltiple: marca varias y Commandeck ejecuta el comando en todas a la vez. Los resultados se abren en **una sola ventana con un selector de máquina** (◀ ▶) para pasar de la salida de una a la de otra, con un estado ✓ / ✗ por máquina.

### Alternar entre local y remoto

Un botón con Local y un servidor activados va bien para probar: ejecutas el comando primero en local para comprobar que funciona y luego eliges el servidor para desplegarlo.

---

## Modos de salida

Los tres modos de ejecución funcionan por SSH. Para sesiones SSH interactivas, usa **Abrir en terminal**: Commandeck genera automáticamente la invocación `ssh -t` correcta.

Consulta [Modos de salida por SSH](../reference/ssh-machines.md#output-modes-over-ssh) para la comparación completa.
