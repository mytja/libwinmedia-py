import time

import libwinmedia

print("New player")
player = libwinmedia.Player()
time.sleep(2)
print("New media")
media = libwinmedia.Media("/home/mytja/Music/test.mp3")
time.sleep(2)
print("new playlist")
playlist = libwinmedia.Playlist(media)
time.sleep(1)
print("Open")
player.open(playlist)
time.sleep(5)
print("Play")
player.play()
print("Sleep")
time.sleep(3)
