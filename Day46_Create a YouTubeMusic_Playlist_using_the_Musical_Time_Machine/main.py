import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import sys

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
response = requests.get(URL,headers=headers,verify=False)

soup = BeautifulSoup(response.text,'html.parser')
titles = soup.find_all(name="h3",class_="chart-entry__title")
song_titles = []

for title in titles:
    song_titles.append(title.getText())

print(song_titles)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

new_playlist = f"{date} Billboard 100"
for playlist in playlists:
    if playlist["title"] == new_playlist:
        print("Playlist with this name is already exists, try with some other name.")
        sys.exit()
playlistId = yt.create_playlist(new_playlist,"Playlist created using Python script")
for song_title in song_titles:
    try:
        search_results = yt.search(song_title,filter="songs")
        yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
    except Exception as e:
        print(f"Skipped '{song_title}' due to error: {e}")