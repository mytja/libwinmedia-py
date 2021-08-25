import os
# Place the DLL right next to the script.
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import libwinmedia
import time

from ctypes import c_int32, CFUNCTYPE

player = libwinmedia.Player()

media1 = libwinmedia.Media("file://D:/libwinmedia-py/test.mp3")
media2 = libwinmedia.Media(
    "https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86"
)
playlist = libwinmedia.Playlist(media1, media2)


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


player.open(media1)

nativecontrols = libwinmedia.NativeControls(player)
nativecontrols.create(button_native_callback)
nativecontrols.set_status(libwinmedia.NativeControlsStatus.Playing)
nativecontrols.update(media1)

print("Now playing")
player.play()
time.sleep(5)

print("Rate: " + str(player.rate))
print("Audio balance: " + str(player.audio_balance))
print("Volume: " + str(player.volume))
print("Is looping: " + str(player.looping))
# print("Media 1 duration: " + str(media1.duration))
# print("Media 2 duration: " + str(media2.duration))
print("Metadata: " + str(media1.tags_from_music()))
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

player.next()
time.sleep(5)
player.back()
time.sleep(5)

print("Now pausing")
player.pause()

media1.dispose()
media2.dispose()
player.dispose()
