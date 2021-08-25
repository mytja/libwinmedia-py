"""
libwinmedia.py
~~~~~~~~~~~~~~

Python bindings to libwinmedia.

A tiny library for media playback, tag extraction & system media transport controls on Windows 10.

   >>> from libwinmedia import *
   >>> player = Player()
   >>> playlist = Playlist(
            Media(
                "https://p.scdn.co/mp3-preview/18f50618e8737c8a1f3b50a653023c5576af8955?cid=774b29d4f13844c495f206cafdad9c86",
            ),
            Media(
                "https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86",
            ),
        )
   >>> player.open(playlist)
   >>> player.play()

"""
from .player import Player
from .media import Media
from .nativecontrols import NativeControls, NativeControlsStatus
from .playlist import Playlist

__author__ = "libwinmedia Team"
__version__ = "0.0.1"
__email__ = "mytja@protonmail.com"
