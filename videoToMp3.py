import subprocess
import os
import sys

# (REQUIRE FFMPEG.EXE IN THE SAME FOLDER THAT THIS SCRIPT)
def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    """Convierte el vídeo en audio directamente con el comando `ffmpeg`.con la ayuda del módulo de subproceso"""
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if __name__ == "__main__":
    vf = sys.argv[1] # Con esto obtenemos la ruta del archivo con el que se ha decidido abrir el programa
    convert_video_to_audio_ffmpeg(vf)