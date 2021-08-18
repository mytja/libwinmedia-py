import ctypes
from ctypes import CFUNCTYPE, c_int32

from . import Player
from .library import lib

class NativeControls:
    def create(self, callback):
        lib.NativeControlsCreate(callback)
