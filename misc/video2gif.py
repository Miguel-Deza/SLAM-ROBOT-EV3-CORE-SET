import os
from moviepy.editor import VideoFileClip

# Ruta de la carpeta donde están los videos
input_folder = 'videos/sensors-motors'
# Ruta de la carpeta donde se guardarán los GIFs
output_folder = 'videos/sensors-motors/gifs'

# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Recorre todos los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        # Crea la ruta completa del video
        video_path = os.path.join(input_folder, filename)
        
        # Define el nombre del archivo GIF
        gif_filename = f"{os.path.splitext(filename)[0]}.gif"
        gif_path = os.path.join(output_folder, gif_filename)

        # Carga el video y convierte a GIF
        clip = VideoFileClip(video_path)
        clip.write_gif(gif_path)

        print(f"Convertido {filename} a {gif_filename}")

print("Conversión completa.")
