---
title: Comprueba tu configuración de Home Assistant antes de reiniciar
description: Una errata en un archivo YAML y Home Assistant no vuelve tras un reinicio. Aquí tienes un botón de reinicio que comprueba la configuración primero, y se niega si está rota.
---

# Comprueba tu configuración de Home Assistant antes de reiniciar

Copiaste en `configuration.yaml` una automatización sacada de un foro. Reinicias Home Assistant. No vuelve.

Es la forma más común de quedarse sin Home Assistant toda la tarde: una sangría mal puesta, una comilla olvidada, y se niega a arrancar. Home Assistant tiene su propio comprobador de configuración; el truco es usarlo *siempre*, antes de cada reinicio, también el día que tienes prisa.

El consejo habitual es entrar por SSH al servidor y lanzar el comprobador a mano dentro del contenedor. Esta es la versión sin nada de eso.

---

## La comprobación en un clic

Commandeck tiene un **pack de botones gratuito para Home Assistant**. Instálalo una vez y tendrás dos botones que se acuerdan por ti.

1. Abre Commandeck y añade tu servidor como máquina (su dirección, tu nombre de usuario, tu contraseña o tu clave SSH).
2. Menú **☰ → Paquetes de botones → Linux → Home Assistant (Docker)** → *Instalar*, y elige esa máquina.
3. Después de editar un archivo, pulsa **¿Es válida mi configuración?**

Lanza el comprobador de Home Assistant, muestra su informe y termina con un veredicto en una línea:

- **Válida**: reiniciar es seguro.
- **Problemas encontrados**: no reinicies hasta corregirlos; el informe de arriba muestra qué está mal.
- **Arrancará, pero algunas partes se ignorarán**: reiniciar es seguro, las partes indicadas quedan apagadas hasta que las corrijas.

Después, en vez de reiniciar desde la página de Home Assistant, pulsa **Reiniciar Home Assistant**. Comprueba primero la configuración y **se niega a reiniciar si está rota**. Si todo está bien, reinicia Home Assistant y espera a que su página vuelva a responder.

Nada que escribir, ningún nombre de contenedor que buscar: el pack encuentra Home Assistant por su imagen, lo llamaras como lo llamaras.

---

## ¿Ha reiniciado, pero falta algo?

El mismo pack responde a las preguntas que vienen después.

**Una integración no ha vuelto.** Pulsa **¿Qué no llegó a arrancar?**: lista las integraciones que no se cargaron y señala las personalizadas, que son la causa habitual después de una actualización.

**No encuentra la llave Zigbee o Z-Wave.** Pulsa **¿Se detecta mi llave Zigbee o Z-Wave?** Comprueba los dos extremos — ¿la ve el servidor?, ¿se le pasa al contenedor? — y muestra la línea exacta que hay que añadir si no.

**Algo falla una y otra vez.** Pulsa **Errores recientes**: todo lo que ha fallado desde el último arranque, cada mensaje una vez en lugar del mismo aviso 300 veces — listo para pegar en un foro o en tu asistente de IA.

---

## El resto del pack

El pack es gratis y tiene trece botones. Los más usados:

| Botón | Responde a |
|---|---|
| **¿Está funcionando Home Assistant?** | La versión que ejecuta, y si Docker tuvo que reiniciarlo tras fallos |
| **¿Hay una versión más reciente?** | Cuántas versiones mensuales llevas de retraso, y qué notas leer antes de saltar |
| **¿Se están haciendo las copias de seguridad?** | La copia más reciente y su antigüedad |
| **Actualizar Home Assistant** | Se niega a empezar sin una copia de las últimas 24 horas; luego actualiza y espera a que responda |
| **Base de datos y espacio en disco** | Cuánto ha crecido la base del historial, y si el disco está casi lleno |

Cada orden se ve antes de instalar, y puedes editar cualquiera después. El pack es para **Home Assistant Container**, la instalación con Docker. ¿Usas Home Assistant OS (el Green, el Yellow, una imagen para Raspberry Pi, una máquina virtual)? Este pack no es para ti: Home Assistant OS no tiene un Docker al que puedas llegar.

---

## Actuar sobre tu servidor pasa por SSH

Tu servidor Home Assistant es una máquina distinta de aquella en la que estás sentado, así que estos botones llegan a él por SSH. Esa parte es [Commandeck Pro](../pro.md): **29 $ una vez, para siempre, con 14 días de prueba que no piden tarjeta ni cuenta**. El pack, como todos los packs, es gratis.

Nada sale de tu ordenador: sin cuenta, sin nube, sin ningún servidor nuestro por medio. Tus máquinas y tus contraseñas se quedan en tu dispositivo.

---

**También te puede servir:** [Actualizar el servidor sin entrar por SSH](update-server-without-ssh.md) · [Comandos Docker como botones de un clic](docker-commands-one-click-buttons.md) · ¿empiezas ahora? Lee la [guía para principiantes](../use-cases/beginner.md).
