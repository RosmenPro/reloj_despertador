"""Reloj Despertador
Este es un concepto interesante para un proyecto en Python. Las aplicaciones de reloj
despertador son utilizadas por personas en todo el mundo. Para un desarrollador intermedio
en Python, es un programa bastante sencillo en la Línea de Comando (CLI). Sin embargo,
este proyecto no es tu típico reloj despertador. Puedes ingresar en realidad URLs de YouTube
en un archivo de texto y diseñar el programa para leer este archivo en la aplicación. Si
configuras una alarma para un momento específico, el reloj despertador elegirá un enlace
aleatorio de YouTube del archivo de texto y lo reproducirá."""

import datetime
import random
import webbrowser

def reproducir_video_youtube(urls):
    video_url = random.choice(urls)
    print("URL del video de YouTube seleccionada:", video_url)
    print("Abriendo URL de video de YouTube:", video_url)
    webbrowser.open(video_url)
    print("URL de video de YouTube abierta en el navegador.")

def main():
    # Leer las URLs de YouTube desde un archivo de texto
    with open("urls_youtube1.txt", "r") as file:
        urls = file.readlines()

    # Eliminar espacios en blanco y nuevas líneas de cada URL
    urls = [url.strip() for url in urls]
    print("URLs de YouTube cargadas:", urls)

    # Configurar la hora de la alarma (por ejemplo, "07:00")
    hora_alarma = "15:26"
    print("Hora de la alarma configurada:", hora_alarma)

    # Esperar hasta que sea la hora de la alarma
    print("Esperando hasta la hora de la alarma...")
    while datetime.datetime.now().strftime("%H:%M") != hora_alarma:
        pass

    # Cuando es hora de la alarma, reproducir un video de YouTube
    print("¡Es hora de la alarma!")
    reproducir_video_youtube(urls)

if __name__ == "__main__":
    main()