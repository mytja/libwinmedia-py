import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
# Place the DLL right next to the script.

import libwinmedia
import time
from ctypes import c_int32, CFUNCTYPE, c_float

player = libwinmedia.Player()

media = libwinmedia.Media("https://archive.org/download/Kalimba.mp3_377/Kalimba.mp3")


@player.volume_callback()
def callback_volume(volume: float):
    print("Volume callback: " + str(volume * 100))


@player.rate_callback()
def callback_rate(rate: float):
    print("Rate callback: " + str(rate * 100))


@CFUNCTYPE(None, c_int32)
def button_native_callback(button: int):
    print("Native button callback: " + str(button))
    if button == 0:
        print("Play")
        player.play()
    if button == 1:
        print("Pause")
        player.pause()
    if button == 6:
        print("Next")
    if button == 7:
        print("Previous")


player.open(media)

nativecontrols = libwinmedia.NativeControls()
nativecontrols.create(button_native_callback)
#nativecontrols.update(player)

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
player.rate = 90
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

media.dispose()
player.dispose()
