import yt_dlp
import os

def descargar_musica():
    busqueda = input("Introduce el nombre de la canción y el artista: ").strip()

    if not busqueda:
        print("No introdujiste ningún texto.")
        return

    # Crear la carpeta de descargas si no existe
    os.makedirs("descargas", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',   # ✅ Codec válido para audio
            'preferredquality': '320', # ✅ Calidad en kbps (solo para mp3)
        }],
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nBuscando '{busqueda}'...")
            ydl.download([f"ytsearch1:{busqueda}"])
            print("\n¡Descarga completada! Archivo guardado en 'descargas/'.")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error al descargar: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    descargar_musica()