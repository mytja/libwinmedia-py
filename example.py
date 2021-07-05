import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
import libwinmedia
import time

player = libwinmedia.Player()

media = libwinmedia.Media("https://www.kozco.com/tech/organfinale.mp3")

player.open(media)

print("Now playing")
player.play()
time.sleep(5)

print("Rate: " + str(player.rate))
print("Audio balance: " + str(player.audio_balance))
print("Volume: " + str(player.volume))

time.sleep(3)

player.volume = 80
print("Volume: " + str(player.volume))

# print("Media duration: " + str(media.duration))

time.sleep(3)

print("Now pausing")
player.pause()
