from time import sleep
import libwinmedia
from threading import Thread

import gi
"""
Must appear before importing Gtk.
"""
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def main():
    player = libwinmedia.Player(True)
    """
    Ensures object is inserted into the std::unordered_map before calling any Player attribute.
    I will ensure the initialization in C++ itself in future & make this stuff sync.
    """
    sleep(2)
    media = libwinmedia.Media(
        "https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86")
    playlist = libwinmedia.Playlist(media)
    player.open(playlist)
    player.play()


Thread(target=main).start()

"""
This is blocking mainloop of GTK.
This essentially just calls `gtk_main` from C, I exposed it in the library (for no reason).
Since this locks the primary thread, all Player methods are called on another thread.
I'm completely not sure if API will stay like this in future.

All Player methods are completely thread safe however.
"""
if __name__ == "__main__":
    Gtk.main()
    """
    Since Flutter already draws a GTK window, it automatically runs this mainloop (on the main thread).
    I don"t know if Python also has something similar, GTK has Python bindings afterall.

    I still exposed libwinmedia.lib.library.PlayerRun as an alternative to Gtk.main.
    Still Gtk.main() is recommended, otherwise Python console will not respond.
    """


""" 
As a side note, sudo apt install libwebkit2gtk-4.0-dev should be required I believe.
"""
