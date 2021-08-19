from ctypes import CFUNCTYPE, c_int32

import libwinmedia
import os

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

player = libwinmedia.Player(1000, False)

media = libwinmedia.Media(1000, "file://D:/libwinmedia-py/test.mp3", False)
print(media.getMetadata())
media.extractThumbnail("D:/libwinmedia-py/", "test.png")

print("Now playing")
player.open(media)


@CFUNCTYPE(None, c_int32)
def buttonNativeCallback(button: int):
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

nativecontrols = libwinmedia.NativeControls()
nativecontrols.create(buttonNativeCallback)
nativecontrols.update(player)
nativecontrols.setStatus(player, libwinmedia.NativeControlsStatus.Playing)

while True:
    continue

