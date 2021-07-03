import os

from ctypes import cdll

from .media import MediaFile, Media
from .player import Player

class LibWinMedia:
    def __init__(self):
        libpath = os.path.dirname(os.path.abspath(__file__))
        dllpath = os.path.join(libpath, os.path.join(r"lwmdll", r"libwinmedia.dll"))
        self.lib = cdll.LoadLibrary(dllpath)
        self.playerInstance = self.lib.Player_create()
        self.player = Player(self.playerInstance, self.lib)
    
    def open(self, file: MediaFile) -> None:
        self.file = file
        self.mediaInstance = self.lib.Media_create(self.file.path)
        self.media = Media(self.mediaInstance, self.lib)
        self.lib.Player_open(self.playerInstance, self.mediaInstance)

