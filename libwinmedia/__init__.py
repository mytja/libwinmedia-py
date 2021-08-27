"""Python bindings for libwinmedia.

Use native Windows APIs to play local files and URLs,
control playback, extract metadata, and show native controls.
"""

from .player import Player
from .media import Media
from .nativecontrols import NativeControls, NativeControlsStatus
from .playlist import Playlist

__author__ = "libwinmedia Team"
__version__ = "1.0.0"
__email__ = "mytja@protonmail.com"
