from pytube import Playlist

URL_PLAYLIST = "https://www.youtube.com/watch?v=VUF_mgdwqqc&list=PLoAQPoE1oG8-r9vuNedK-uKGSLNsA9sPE&ab_channel=Forexcitypro"

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)

print(urls)
