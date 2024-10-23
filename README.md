# Reloj Despertador

Este es un proyecto de reloj despertador en Python que permite reproducir aleatoriamente un video de YouTube desde una lista de URLs almacenadas en un archivo de texto. Al configurarse la alarma, el programa seleccionará una URL de la lista y la abrirá en el navegador.

## Descripción

Las aplicaciones de reloj despertador son utilizadas por personas en todo el mundo. Este programa, más allá de ser un reloj despertador típico, permite al usuario ingresar URLs de YouTube en un archivo de texto y configurarlo para reproducir un video aleatorio en el momento programado.

## Funcionalidades

- Cargar URLs de videos de YouTube desde un archivo de texto.
- Configurar una alarma para un momento específico.
- Reproducir un video aleatorio de YouTube al sonar la alarma.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x en tu sistema. No se requieren bibliotecas externas.

## Uso

1. **Crea un archivo de texto** llamado `urls_youtube1.txt` en el mismo directorio que el script. Escribe las URLs de los videos de YouTube que quieres que el reloj despertador use, cada una en una nueva línea.

2. **Ejecuta el script**:

   ```bash
   python reloj_despertador.py
   
   ```
3. **Configura la hora de la alarma** dentro del script. Por defecto, la alarma está configurada para las "15:26". Cambia esta hora a la que desees.

4. **Espera a que suene la alarma.** El programa esperará hasta la hora programada y luego abrirá un video de YouTube aleatorio desde tu archivo.

## Contribuir
Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar este proyecto, no dudes en abrir un issue o crear un pull request.

## Actualizaciones pendientes. 
  . Cambiar hora en un gui para no tener que hacerlo dentro del propio script
