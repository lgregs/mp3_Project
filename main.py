import yt_dlp
import urllib.parse as urlparse

def download(url):
    # 1. Analisa a URL para ver se existe o parâmetro 'list'
    parsed_url = urlparse.urlparse(url)
    parametros = urlparse.parse_qs(parsed_url.query)
    
    eh_playlist = 'list' in parametros
    
    # 2. Define dinamicamente onde e como salvar o arquivo
    if eh_playlist:
        print("🧠 Playlist detectada! Organizando em pastas numeradas...")
        # Salva dentro de: Playlists / Nome da Playlist / 01 - Nome da Musica.mp3
        caminho_saida = 'Playlists/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'
    else:
        print("🎵 Musica detectada! Baixando faixa única...")
        # Salva dentro de: Musicas / Nome da Musica.mp3
        caminho_saida = 'Musicas/%(title)s.%(ext)s'

    # 3. Configurações universais do yt-dlp
    opcoes = {
        'format': 'bestaudio/best',
        'ignoreerrors': True,  # Continua baixando mesmo se um vídeo da playlist falhar
        'outtmpl': caminho_saida,
        'writethumbnail': True, # Prepara a capa do álbum
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320', # Qualidade máxima do MP3
            },
            {
                'key': 'EmbedThumbnail',   # Embutir a capa no MP3 (perfeito para o iTunes)
            }
        ],
    }

    # 4. Executa o download
    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print("\n✅ Processo concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro crítico: {e}")


# Substitua esta URL pelo link do YouTube que deseja baixar (pode ser um vídeo ou uma playlist)
url = 'https://youtube.com/playlist?list=OLAK5uy_mw4FTsQlVeKTVFhffMb2t1qIThWg3qsN4&si=HM9EriP6s8unIiaJ'
download(url)