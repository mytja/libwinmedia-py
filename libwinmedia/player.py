from .media import Media
from .library import lib

from ctypes import c_int32, c_float

class Player(object):
    def __init__(self):
        self.id = lib.Player_create()

    def open(self, media: Media) -> None:
        lib.Player_open(self.id, media.id)

    def play(self) -> None:
        lib.Player_play(self.id)

    def pause(self) -> None:
        lib.Player_pause(self.id)

    def dispose(self) -> None:
        lib.Player_dispose(self.id)

    @property
    def looping(self) -> bool:
        return lib.Player_isLooping(self.id)

    @looping.setter
    def looping(self, value: bool) -> None:
        lib.Player_setIsLooping(self.id, value)

    @property
    def autoplay(self) -> bool:
        return lib.Player_isAutoplay(self.id)

    @autoplay.setter
    def autoplay(self, value: bool) -> None:
        lib.Player_setAutoplay(self.id, value)

    @property
    def audio_balance(self) -> float:
        return lib.Player_getAudioBalance(self.id)

    @audio_balance.setter
    def audio_balance(self, value: float) -> None:
        lib.Player_setVolume.argtypes = [c_int32, c_float]
        lib.Player_setAudioBalance(self.id, value)

    @property
    def rate(self) -> float:
        return lib.Player_getRate(self.id)

    @rate.setter
    def rate(self, value: float) -> None:
        lib.Player_setVolume.argtypes = [c_int32, c_float]
        lib.Player_setRate(self.id, value)

    @property
    def volume(self) -> float:
        return lib.Player_getVolume(self.id)

    @volume.setter
    def volume(self, value: float) -> None:
        lib.Player_setVolume.argtypes = [c_int32, c_float]
        lib.Player_setVolume(self.id, value)

    @property
    def position(self) -> int:
        return lib.Player_getPosition(self.id)

    @position.setter
    def position(self, value: int) -> None:
        lib.Player_setPosition(self.id, value)
