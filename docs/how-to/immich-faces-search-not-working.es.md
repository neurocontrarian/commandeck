---
title: ¿Immich no reconoce las caras? Descubre por qué con un clic
description: Las caras no se agrupan y la búsqueda no encuentra nada. Así puedes comprobar las tres causas habituales desde un botón en tu ordenador, sin abrir una terminal en tu servidor.
---

# ¿Immich no reconoce las caras? Descubre por qué con un clic

Subiste unos cientos de fotos. Días después, las caras siguen sin agruparse y buscar «playa» no encuentra nada.

No se ha perdido nada. Tus fotos están a salvo: lo que se ha parado es la parte de Immich que las *mira*. Immich son cuatro programas que trabajan juntos, y las caras y la búsqueda inteligente salen de uno de ellos: la parte de aprendizaje automático. Cuando se para, o la aplicación deja de alcanzarla, Immich sigue funcionando… solo que ya no reconoce nada.

El consejo habitual es entrar por SSH al servidor, listar los contenedores y leer sus registros. Esta es la versión sin nada de eso.

---

## La comprobación en un clic

Commandeck tiene un **pack de botones gratuito para Immich**. Instálalo una vez y tendrás un botón que comprueba las tres causas habituales, una tras otra, y te dice cuál es.

1. Abre Commandeck y añade tu servidor como máquina (su dirección, tu nombre de usuario, tu contraseña o tu clave SSH).
2. Menú **☰ → Paquetes de botones → Linux → Immich (Docker)** → *Instalar*, y elige esa máquina.
3. Pulsa **¿Por qué no funcionan los rostros o la búsqueda?**

Comprueba, en palabras sencillas:

- **¿Está funcionando la parte de caras y búsqueda?** Si está parada, esa es la causa, y lo dice.
- **¿La aplicación llega a ella?** Las dos pueden estar funcionando sin hablarse. Si es así, te indica dónde poner la dirección correcta en los ajustes de Immich.
- **¿Qué ha avisado en las últimas 24 horas?** Sus errores y advertencias recientes, incluidos los que significan que se quedó sin memoria.

Nada que escribir, ningún nombre de contenedor que buscar: el pack encuentra los contenedores de Immich por su imagen, los llamaras como los llamaras.

---

## ¿Las caras van bien, pero falla otra cosa?

El mismo pack responde a las otras preguntas por las que se entra por SSH.

**El disco se llena.** Immich guarda más que tus fotos: miniaturas, copias convertidas de tus vídeos, copias de seguridad de su base de datos. Pulsa **¿Adónde se fue el espacio en disco?**: mide cada cosa, dice qué es y te avisa cuando un disco está casi lleno.

**¿Se hacen de verdad mis copias de seguridad?** Immich puede copiar su base de datos cada noche, si el ajuste está activado y nada se ha roto. Pulsa **¿Se están haciendo las copias de seguridad?**: encuentra la copia más reciente y te dice qué antigüedad tiene, en vez de dejarte suponerlo.

**¿Debo actualizar?** Pulsa **¿Hay una versión más reciente?**: compara tu versión con la más nueva y te avisa cuando el salto es grande, de los que obligan a actualizar también la app del móvil. **Actualizar Immich** se niega a empezar sin una copia de la base de datos de las últimas 24 horas, porque una actualización no se puede deshacer.

---

## El resto del pack

El pack es gratis y tiene trece botones. Los más usados:

| Botón | Responde a |
|---|---|
| **¿Está funcionando Immich?** | Cada una de sus cuatro partes, para qué sirve y por qué se paró una |
| **Errores recientes** | Lo que falló en las últimas 24 horas, cada mensaje una vez — listo para pegar en un foro o en tu asistente de IA |
| **Reiniciar Immich** | El primer paso cuando se atasca: reinicia todas las partes y espera a que la aplicación esté lista |
| **Recursos ahora mismo** | Por qué está ocupado el servidor — normalmente el reconocimiento de caras tras una subida grande |
| **Listar los usuarios** | Cada cuenta, con su correo y si es administradora |

Cada orden se ve antes de instalar, y puedes editar cualquiera después. El pack es para **Immich instalado con Docker** (compose o Portainer). ¿Lo instalaste como plantilla de Unraid, app de TrueNAS o snap? Algunos botones no lo encontrarán.

---

## Actuar sobre tu servidor pasa por SSH

Tu servidor Immich es una máquina distinta de aquella en la que estás sentado, así que estos botones llegan a él por SSH. Esa parte es [Commandeck Pro](../pro.md): **29 $ una vez, para siempre, con 14 días de prueba que no piden tarjeta ni cuenta**. El pack, como todos los packs, es gratis.

Nada sale de tu ordenador: sin cuenta, sin nube, sin ningún servidor nuestro por medio. Tus máquinas y tus contraseñas se quedan en tu dispositivo.

---

**También te puede servir:** [Ver el espacio libre del NAS en un clic](check-disk-space-nas.md) · [Actualizar el servidor sin entrar por SSH](update-server-without-ssh.md) · ¿empiezas ahora? Lee la [guía para principiantes](../use-cases/beginner.md).
