import requests

# Liste des liens vers les playlists M3U
playlist_urls = [
    'https://raw.githubusercontent.com/lahcene1313/vttv/refs/heads/main/Mon.m3u',
    'https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/playlists/samsungtvplus/main/filter/raw.m3u',
    'https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/playlists/paratv/main/filter/raw.m3u'
]

# Fonction pour télécharger le contenu des playlists
def download_playlist(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie que la requête a réussi
        return response.text.splitlines()  # Retourne les lignes du fichier
    except requests.RequestException as e:
        print(f"Erreur de téléchargement pour {url}: {e}")
        return []

# Fusionner les playlists
def merge_playlists(playlist_urls):
    merged_playlist = []
    
    # Télécharger et fusionner les playlists
    for url in playlist_urls:
        print(f"Téléchargement de {url}...")
        playlist = download_playlist(url)
        merged_playlist.extend(playlist)
    
    return merged_playlist

# Sauvegarder la playlist fusionnée dans un fichier
def save_merged_playlist(merged_playlist, filename='merged_playlist.m3u'):
    with open(filename, 'w') as file:
        for line in merged_playlist:
            file.write(line + '\n')
    print(f"Playlist fusionnée sauvegardée sous {filename}")

# Exécution du script
if __name__ == "__main__":
    merged_playlist = merge_playlists(playlist_urls)
    save_merged_playlist(merged_playlist)
