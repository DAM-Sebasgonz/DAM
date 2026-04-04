import yt_dlp

def descargar_musica_sin_drm():
    busqueda = input("Introduce el nombre de la canción y el artista: ").strip()
    
    if not busqueda:
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp4',
            'preferredquality': '320',
        }],
        'outtmpl': 'descargas/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\nBuscando '{busqueda}' en la red...")
            # Añadimos 'ytsearch:' antes de la búsqueda
            ydl.download([f"ytsearch1:{busqueda}"])
            print("\n¡Logrado! Archivo guardado en la carpeta 'descargas'.")
    except Exception as e:
        print(f"Vaya, algo salió mal: {e}")

if __name__ == "__main__":
    descargar_musica_sin_drm()