# Ver el espacio libre del NAS en un clic

Un disco lleno es lo que rompe un servidor doméstico sin hacer ruido: las descargas se paran, las copias de seguridad fallan, el servidor multimedia deja de añadir archivos y las bases de datos se corrompen. La solución es mirar el espacio *antes* de que se llene, pero ¿quién quiere entrar por SSH en el NAS y escribir `df -h` cada semana?

Commandeck lo convierte en un botón. Un clic y ves exactamente cómo de lleno está cada disco, en una ventana de tu escritorio.

![Ventana de salida de Commandeck con el resultado de df -h y un disco al 94 %](../assets/howto-disk-output.png)

---

## El botón

Clic derecho en la cuadrícula → **Nuevo botón** y rellena:

| Campo | Valor |
|-------|-------|
| Etiqueta | `Espacio en disco` |
| Comando | `df -h` |
| Modo de ejecución | `Mostrar la salida` |
| Icono | `drive-harddisk-symbolic` |
| Descripción emergente | `Cómo de lleno está cada disco` |

Al pulsarlo obtienes una tabla clara: cada disco, su tamaño, cuánto está ocupado y el porcentaje lleno. La columna que importa es **Use%**: cualquier valor cercano al 90 % pide atención.

---

## Otros botones de disco que merecen la pena

| Etiqueta | Comando | Qué te muestra |
|----------|---------|----------------|
| `Carpetas más grandes` | `du -h -d 1 / \| sort -hr \| head -20` | Qué se está comiendo el espacio |
| `Carpetas más grandes (personal)` | `du -h -d 1 ~ \| sort -hr \| head -20` | Lo mismo, dentro de tu carpeta personal |
| `Espacio de Docker` | `docker system df` | Cuánto está usando Docker |
| `Liberar espacio de Docker` | `docker system prune -f` | Recupera imágenes y capas sin usar |

El botón **Carpetas más grandes** es la continuación natural: cuando `Espacio en disco` avisa de que un disco está casi lleno, este te dice *qué* hay que limpiar.

---

## Mirar el NAS o el servidor (y no solo este PC)

Tu NAS es otra máquina, así que la verdadera ventaja es ejecutar estos botones **en el NAS por SSH** mientras estás sentado frente a tu escritorio Windows o Mac. Añade el NAS una vez, apunta los botones hacia él y «mirar el disco del NAS» se convierte en un clic desde el otro lado de la casa.

!!! tip "Las comprobaciones remotas son Pro"
    Llegar a otra máquina por SSH es [Commandeck Pro](../pro.md): **29 $ una sola vez, de por vida, con 14 días de prueba gratis y sin tarjeta**. Mirar el disco de *este* ordenador funciona en la versión gratuita.

---

## Conviértelo en costumbre

El espacio en disco es de esas cosas en las que solo piensas cuando ya es tarde. Con un botón en la cuadrícula, echarle un vistazo cuesta dos segundos, así que lo haces de verdad y detectas el disco que se llena antes de que tumbe el servidor.

- **Sin terminal y sin acordarse de `df -h`**: es un botón.
- **Solo lectura y seguro**: estos botones únicamente *miran*, no cambian nada.
- **Privado**: sin cuenta, sin nube y sin telemetría.

---

**Relacionado:** la guía [Gestión de un servidor doméstico](../use-cases/home-server.md) monta juntos los botones de disco, actualización y reinicio. ¿Acabas de llegar? Mira la [Guía para principiantes](../use-cases/beginner.md).
