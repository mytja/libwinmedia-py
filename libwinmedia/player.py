from .media import Media
from .library import lib

from ctypes import c_int32, c_float

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

    def closeWindow(self) -> None:
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

    # Not working.
    def setVolumeEventHandler(self, callback) -> None:
        lib.PlayerSetVolumeEventHandler(self.id, callback)

    def setRateEventHandler(self, callback) -> None:
        lib.PlayerSetRateEventHandler(self.id, callback)

    def setIsDoneEventHandler(self, callback) -> None:
        lib.PlayerSetIsCompletedEventHandler(self.id, callback)

    def setPositionEventHandler(self, callback) -> None:
        lib.PlayerSetPositionEventHandler(self.id, callback)

    def setDurationEventHandler(self, callback) -> None:
        lib.PlayerSetDurationEventHandler(self.id, callback)
