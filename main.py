import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Вставте ваш плеер музыки(например: mpv)
playeer = "python ~/Tmusix/app.py"

# Получаем ключи
try:
    with open('config', 'r') as f:
        lines = f.readlines()
        if len(lines) >= 2:
            client_id = lines[0].strip()
            client_secret = lines[1].strip()
        else:
            print("config does not have enough lines.")
            sys. exit()
except FileNotFoundError:
    print("config not found.")
    sys. exit()
    
# Инициализация клиента Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Функция для поиска треков по запросу
def search_tracks(query, limit=50):
    results = sp.search(q=query, type='track', limit=limit)
    return results['tracks']['items']

# Запрос треков
query = input("Name: ")
tracks = search_tracks(query, limit=50)

# Запись треков в файл и скачивание
with open('music.txt', 'w', encoding='utf-8') as file:
    for i, track in enumerate(tracks, 1):
        name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        url = track['external_urls']['spotify']
        file.write(f"{name} - {artists} - {url}\n")
        os.system(f"spotdl {url} && {playeer} '{artists} - {name}.mp3' && rm '{artists} - {name}.mp3'")
