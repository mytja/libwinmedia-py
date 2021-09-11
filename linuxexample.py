import time

import libwinmedia

print("New media")
media = libwinmedia.Media("/home/mytja/Music/test.mp3")
print("New player")
player = libwinmedia.Player()
print("Open")
player.open(media)
print("Play")
player.play()
print("Sleep")
#while True:
#    pass
time.sleep(3)