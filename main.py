import requests

# Liste des liens des playlists M3U
playlist_urls = [
    'https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/playlists/samsungtvplus/main/filter/raw.m3u',
    'https://raw.githubusercontent.com/Paradise-91/ParaTV/refs/heads/main/playlists/paratv/main/filter/raw.m3u'
]

# Fonction pour télécharger le contenu des playlists
def download_playlist(url):
    try:
        print(f"Téléchargement de {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Vérifie que la requête a réussi
        print(f"Succès pour {url}, récupération de {len(response.text)} octets.")
        return response.text.splitlines()  # Retourne les lignes du fichier
    except requests.RequestException as e:
        print(f"Erreur de téléchargement pour {url}: {e}")
        return []

# Fusionner les playlists
def merge_playlists(playlist_urls):
    merged_playlist = []
    for url in playlist_urls:
        playlist = download_playlist(url)
        if playlist:  # Vérifie si la playlist a bien été téléchargée
            merged_playlist.extend(playlist)
        else:
            print(f"Impossible d'ajouter la playlist depuis {url}")
    print(f"Nombre de lignes après fusion: {len(merged_playlist)}")
    return merged_playlist

# Sauvegarder la playlist fusionnée dans un fichier
def save_merged_playlist(merged_playlist, filename='lahcene.m3u'):
    print("Début de la sauvegarde...")
    try:
        with open(filename, 'w') as file:
            for line in merged_playlist:
                file.write(line + '\n')
        print(f"Playlist fusionnée sauvegardée sous {filename}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")

# Exécution du script
if __name__ == "__main__":
    print("Exécution du script de fusion des playlists...")
    merged_playlist = merge_playlists(playlist_urls)
    if merged_playlist:
        save_merged_playlist(merged_playlist)
    else:
        print("Aucune playlist fusionnée. Le fichier ne sera pas créé.")
