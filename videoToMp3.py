import subprocess
import os
import sys

# (REQUIRE FFMPEG.EXE IN THE SAME FOLDER THAT THIS SCRIPT)
def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    """Convierte el vídeo en audio directamente con el comando `ffmpeg`.con la ayuda del módulo de subproceso"""
    filename, ext = os.path.splitext(video_file)

    # Subprocess lo que hace es ejecutar un comando, en este caso lo que hay en [] es el comando a ejecutar
    # Dicho comando es una llamada al ffmpeg.exe con los parametros -y -i y los parametros que respectan al archivo
    # Es por esto que el archivo ffmpeg.exe debe de estar en la misma carpeta que el script
    process=subprocess.Popen(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in process.stdout:
       print(line)

if __name__ == "__main__":
    vf = sys.argv[1] # Con esto obtenemos la ruta del archivo con el que se ha decidido abrir el programa
    convert_video_to_audio_ffmpeg(vf)
