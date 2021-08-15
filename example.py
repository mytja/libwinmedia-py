import os
import libwinmedia
import time

from ctypes import c_int32, CFUNCTYPE

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

player = libwinmedia.Player(1000, False)

media = libwinmedia.Media(1000, "https://archive.org/download/Kalimba.mp3_377/Kalimba.mp3")


@CFUNCTYPE(None, c_int32)
def callbackVolume(volume: int):
    print("Volume callback: " + str(volume))


@CFUNCTYPE(None, c_int32)
def callbackRate(rate: int):
    print("Rate callback: " + str(rate))


player.open(media)
player.setVolumeEventHandler(callbackVolume)
player.setRateEventHandler(callbackRate)

print("Now playing")
player.play()
time.sleep(5)

print("Rate: " + str(player.rate))
print("Audio balance: " + str(player.audio_balance))
print("Volume: " + str(player.volume))
print("Is looping: " + str(player.looping))
print("Media duration: " + str(media.duration))
print("Position: " + str(player.position))

time.sleep(3)

player.volume = 65
player.looping = True
print("Is looping: " + str(player.looping))
print("Volume: " + str(player.volume))
print("Position: " + str(player.position))
player.position = 12000
print("Position: " + str(player.position))

time.sleep(5)

print("Position: " + str(player.position))
print("Now pausing")
player.pause()
