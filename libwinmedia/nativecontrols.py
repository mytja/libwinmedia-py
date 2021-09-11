import os
from typing import Callable

from . import Media, Player
from .library import lib
from ctypes import c_int32, POINTER, CFUNCTYPE, c_char_p


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
    def __init__(self, player: Player):
        self.player = player
        self._callbacks = []

    def create(self, callback: Callable[[int], None]) -> None:
        cb = CFUNCTYPE(None, c_int32)(callback)
        self._callbacks.append(cb)
        lib.PlayerNativeControlsCreate(self.player.id, cb)

    def create_callback(self) -> Callable[[Callable[[int], None]], None]:
        def wrapper(callback: Callable[[int], None]) -> None:
            self.create(callback)

        return wrapper

    def set_status(self, status: int):
        lib.PlayerNativeControlsSetStatus(self.player.id, status)

    def update(self, media: Media):
        folder = os.path.dirname(__file__)
        file = "thumbnail.png"
        thumb = os.path.join(folder, file)
        media.extract_thumbnail(folder, file)

        lib.PlayerNativeControlsUpdate.argtypes = [
            c_int32,
            c_int32,
            POINTER(c_char_p),
            c_char_p,
        ]

        meta = media.tags_from_music()

        metalist = [
            meta["albumArtist"].encode("utf-8"),
            meta["title"].encode("utf-8"),
            "1".encode("utf-8"),
            meta["publisher"].encode("utf-8"),
            meta["title"].encode("utf-8"),
            str(meta["trackNumber"]).encode("utf-8"),
        ]

        metas = (c_char_p * len(metalist))(*metalist)

        lib.PlayerNativeControlsUpdate(self.player.id, 1, metas, thumb)

    def clear(self):
        lib.PlayerNativeControlsClear(self.player.id)

    def dispose(self):
        lib.PlayerNativeControlsDispose(self.player.id)
