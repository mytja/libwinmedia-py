import os

from .media import MediaFile

from ctypes import c_bool, c_int32, c_float

class Player:
    isLoopingEnabled = False
    isAutoplayEnabled = False

    """
    General commands
    """
    def __init__(self, playerInstance, lib) -> None:
        self.player = playerInstance
        self.lib = lib
    
    def play(self) -> None:
        self.lib.Player_play(self.player)

        # Set some integers and booleans that can only be changed within this class and don't update manually
        self.isLoopingEnabled = self.isLooping()
        self.isAutoplayEnabled = self.isAutoplay()
        self.volume = self.getVolume()
        self.rate = self.getRate()
        self.audioBalance = self.getAudioBalance()

    def pause(self) -> None:
        self.lib.Player_pause(self.player)
    
    def close(self) -> None:
        self.lib.Player_dispose(self.player)
    
    """
    Commands with return value (eg. commands with returning current status of something)
    """
    def isLooping(self) -> bool:
        self.isLoopingEnabled = self.lib.Player_isLooping(self.player)
        return self.isLooping
    
    def isAutoplay(self) -> bool:
        self.isAutoplayEnabled = self.lib.Player_isAutoplay(self.player)
        return self.isAutoplay
    
    def getAudioBalance(self) -> float:
        return self.lib.Player_getAudioBalance(self.player)
    
    def getRate(self) -> float:
        return self.lib.Player_getRate(self.player)
    
    def getVolume(self) -> float:
        return self.lib.Player_getVolume(self.player)

    """
    Commands that set Player preferences
    """
    def setPosition(self, position: int) -> None:
        self.lib.Player_setPosition(self.player, position)
    
    def setVolume(self, volume: float) -> None:
        self.lib.Player_setVolume.argtypes = [c_int32, c_float]
        self.lib.Player_setVolume(self.player, volume)
        self.volume = volume
    
    def setRate(self, rate: float) -> None:
        self.lib.Player_setRate(self.player, rate)
        self.rate = rate
    
    def setAudioBalance(self, balance: float) -> None:
        self.lib.Player_setAudioBalance(self.player, balance)
        self.audioBalance = balance
    
    def setAutoplay(self, autoplay: bool) -> None:
        self.lib.Player_setAutoplay(self.player, autoplay)
        self.isAutoplayEnabled = autoplay

    def setLooping(self, looping: bool) -> None:
        self.lib.Player_setIsLooping(self.player, looping)
        self.isLoopingEnabled = looping