from .media import Media
from .library import lib

from ctypes import c_int32, c_float, c_void_p, CFUNCTYPE


class Player(object):
    media = None

    def __init__(self, id: int, showVideo: bool = False):
        """
        Here you create a player instance.

        Args:
            id (int): A unique ID that is used to separate this player from others
            showVideo (bool, optional): Shows video window - defaults to False

        This function returns:
            None
        """

        self.id = id
        lib.PlayerCreate(self.id, showVideo)

    def open(self, media: Media, autostart: bool = True) -> None:
        """
        Here you provide a Media instance to player

        Args:
            media (Media): A media file in Media instance
            autostart (bool, optional): Autostarts playing the provided Media instance - defaults to True

        This function returns:
            None
        """

        self.media = media

        lib.PlayerOpen(self.id, media.id)
        if autostart:
            self.play()

    def play(self) -> None:
        """
        Here you start playing media currently open in Player instance

        This function has no arguments

        This function returns:
            None
        """

        lib.PlayerPlay(self.id)

    def pause(self) -> None:
        """
        This function pauses currently playing media in Player instance

        This function has no arguments

        This function returns:
            None
        """

        lib.PlayerPause(self.id)

    def dispose(self) -> None:
        """
        This function disposes system resources, and kills this player instance

        This function has no arguments

        This function returns:
            None
        """

        lib.PlayerDispose(self.id)

    def closeWindow(self) -> None:
        """
        This function closes Video player window

        This function has no arguments

        This function returns:
            None
        """

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
        return lib.PlayerGetAudioBalance(self.id)

    @audio_balance.setter
    def audio_balance(self, value: float) -> None:
        lib.PlayerSetVolume.argtypes = [c_int32, c_float]
        lib.PlayerSetAudioBalance(self.id, value)

    @property
    def rate(self) -> float:
        return lib.PlayerGetRate(self.id)

    @rate.setter
    def rate(self, value: float) -> None:
        lib.PlayerSetVolume.argtypes = [c_int32, c_float]
        lib.PlayerSetRate(self.id, value)

    @property
    def volume(self) -> float:
        return lib.PlayerGetVolume(self.id)

    @volume.setter
    def volume(self, value: float) -> None:
        lib.PlayerSetVolume.argtypes = [c_int32, c_float]
        lib.PlayerSetVolume(self.id, value)

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
        lib.PlayerSetVolumeEventHandler(self.id, callback)
