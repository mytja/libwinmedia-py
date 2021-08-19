import ctypes
import os
from ctypes import CFUNCTYPE, c_int32

from . import Player
from .library import lib


class NativeControlsStatus:
    Closed = 0
    Changing = 1
    Stopped = 2
    Playing = 3
    Paused = 4


class NativeControlsButton:
    Play = 0
    Pause = 1
    Stop = 2
    Record = 3
    FastForward = 4
    Rewind = 5
    Next = 6
    Previous = 7
    ChannelUp = 8
    ChannelDown = 9


class NativeControls:
    def create(self, callback):
        lib.NativeControlsCreate(callback)

    def setStatus(self, player: Player, status: int):
        lib.PlayerNativeControlsSetStatus(player.id, status)

    def update(self, player: Player):
        folder = os.path.dirname(__file__)
        file = "thumbnail.png"
        thumb = os.path.join(folder, file)
        player.media.extractThumbnail(folder, file)
        lib.PlayerNativeControlsUpdate(
            player.id,
            2,
            player.media.getMetadata(),
            thumb
        )

    def clear(self):
        lib.NativeControlsClear()

    def dispose(self):
        lib.NativeControlsDispose()
