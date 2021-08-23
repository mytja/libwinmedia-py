from .media import Media
from .library import lib
from typing import Callable

from ctypes import CFUNCTYPE, c_bool, c_int32, c_float

player_id = 0


class Player(object):
    """A class for controlling a media player."""

    def __init__(self, showVideo: bool = False):
        """Create a new Player instance.

        Args:
            showVideo (bool, optional): Whether to show the video window. Defaults to False.
        """

        global player_id
        self.id = player_id
        lib.PlayerCreate(self.id, showVideo)
        player_id += 1

        # to prevent callbacks from being garbage collected
        self._callbacks = []

    def open(self, media: Media, autostart: bool = True) -> None:
        """Provide a Media instance to the player.

        Args:
            media (Media): A media file.
            autostart (bool, optional): Whether to autostart playback of the provided media. Defaults to True.
        """

        lib.PlayerOpen(self.id, media.id)
        if autostart:
            self.play()

    def play(self) -> None:
        """Start playing the media that is currently open in the player."""

        lib.PlayerPlay(self.id)

    def pause(self) -> None:
        """Pause the playback of the current media."""

        lib.PlayerPause(self.id)

    def dispose(self) -> None:
        """Release system resources and kill the player instance."""

        lib.PlayerDispose(self.id)
        self._callbacks.clear()

    def close_window(self) -> None:
        """Close the video player window."""

        lib.PlayerCloseWindow(self.id)

    @property
    def looping(self) -> bool:
        return lib.PlayerIsLooping(self.id)

    @looping.setter
    def looping(self, value: bool) -> None:
        lib.PlayerSetIsLooping(self.id, value)

    @property
    def autoplay(self) -> bool:
        return lib.PlayerIsAutoplay(self.id)

    @autoplay.setter
    def autoplay(self, value: bool) -> None:
        lib.PlayerSetAutoplay(self.id, value)

    @property
    def audio_balance(self) -> float:
        lib.PlayerGetAudioBalance.restype = c_float
        return lib.PlayerGetAudioBalance(self.id) * 100

    @audio_balance.setter
    def audio_balance(self, value: float) -> None:
        lib.PlayerSetVolume.argtypes = [c_int32, c_float]
        lib.PlayerSetAudioBalance(self.id, value / 100)

    @property
    def rate(self) -> float:
        lib.PlayerGetRate.restype = c_float
        return lib.PlayerGetRate(self.id) * 100

    @rate.setter
    def rate(self, value: float) -> None:
        lib.PlayerSetRate.argtypes = [c_int32, c_float]
        lib.PlayerSetRate(self.id, value / 100)

    @property
    def volume(self) -> float:
        lib.PlayerGetVolume.restype = c_float
        return lib.PlayerGetVolume(self.id) * 100

    @volume.setter
    def volume(self, value: int) -> None:
        lib.PlayerSetVolume.argtypes = [c_int32, c_float]
        lib.PlayerSetVolume(self.id, value / 100)

    @property
    def position(self) -> int:
        return lib.PlayerGetPosition(self.id)

    @position.setter
    def position(self, value: int) -> None:
        lib.PlayerSeek(self.id, value)

    def seek(self, value: int) -> None:
        self.position = value

    def set_playing_callback(self, callback: Callable[[bool], None]) -> None:
        cb = CFUNCTYPE(None, c_bool)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetIsPlayingEventHandler(self.id, cb)

    def playing_callback(self) -> Callable[[Callable[[bool], None]], None]:
        def wrapper(callback: Callable[[bool], None]) -> None:
            self.set_playing_callback(callback)

        return wrapper

    def set_completed_callback(self, callback: Callable[[bool], None]) -> None:
        cb = CFUNCTYPE(None, c_bool)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetIsCompletedEventHandler(self.id, cb)

    def completed_callback(self) -> Callable[[Callable[[bool], None]], None]:
        def wrapper(callback: Callable[[bool], None]) -> None:
            self.set_completed_callback(callback)

        return wrapper

    def set_buffering_callback(self, callback: Callable[[bool], None]) -> None:
        cb = CFUNCTYPE(None, c_bool)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetIsBufferingEventHandler(self.id, cb)

    def buffering_callback(self) -> Callable[[Callable[[bool], None]], None]:
        def wrapper(callback: Callable[[bool], None]) -> None:
            self.set_buffering_callback(callback)

        return wrapper

    def set_volume_callback(self, callback: Callable[[float], None]) -> None:
        cb = CFUNCTYPE(None, c_float)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetVolumeEventHandler(self.id, cb)

    def volume_callback(self) -> Callable[[Callable[[float], None]], None]:
        def wrapper(callback: Callable[[float], None]) -> None:
            self.set_volume_callback(callback)

        return wrapper

    def set_rate_callback(self, callback: Callable[[float], None]) -> None:
        cb = CFUNCTYPE(None, c_float)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetRateEventHandler(self.id, cb)

    def rate_callback(self) -> Callable[[Callable[[float], None]], None]:
        def wrapper(callback: Callable[[float], None]) -> None:
            self.set_rate_callback(callback)

        return wrapper

    def set_position_callback(self, callback: Callable[[int], None]) -> None:
        cb = CFUNCTYPE(None, c_int32)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetPositionEventHandler(self.id, cb)

    def position_callback(self) -> Callable[[Callable[[int], None]], None]:
        def wrapper(callback: Callable[[int], None]) -> None:
            self.set_position_callback(callback)

        return wrapper

    def set_duration_callback(self, callback: Callable[[int], None]) -> None:
        cb = CFUNCTYPE(None, c_int32)(callback)
        self._callbacks.append(cb)
        lib.PlayerSetDurationEventHandler(self.id, cb)

    def duration_callback(self) -> Callable[[Callable[[int], None]], None]:
        def wrapper(callback: Callable[[int], None]) -> None:
            self.set_duration_callback(callback)

        return wrapper
