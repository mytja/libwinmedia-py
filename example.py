import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
import libwinmedia
import time

player = libwinmedia.Player()

media = libwinmedia.Media("https://archive.org/download/Kalimba.mp3_377/Kalimba.mp3")

player.open(media)

print("Now playing")
player.play()
time.sleep(5)

print("Rate: " + str(player.rate))
print("Audio balance: " + str(player.audio_balance))
print("Volume: " + str(player.volume))
print("Media duration: " + str(media.duration))
print("Position: " + str(player.position))

time.sleep(3)

player.volume = 80
print("Volume: " + str(player.volume))
print("Position: " + str(player.position))
player.position = 12
print("Position: " + str(player.position))

time.sleep(5)

print("Position: " + str(player.position))
print("Now pausing")
player.pause()
