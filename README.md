# libwinmedia-py
Python bindings for [libwinmedia](https://github.com/harmonoid/libwinmedia), a tiny yet powerful media playback library for Windows and Linux.

This library's goal is to make a beginner-friendly, easy-to-use API with many advanced features.

# Dependencies
This library has NO DEPENDENCIES on Windows, except for C++ library.

Linux on the other hand requires some packages to be installed:
- `pygobject` - This allows us to interact with [GTK](https://www.gtk.org/). This will be automatically installed when you install our library.
- `libgirepository1.0-dev` - This dependency allows us to interact with [GTK](https://www.gtk.org/)
   through [PyGObject](https://pygobject.readthedocs.io/en/latest/index.html)
- `python3-dev` - This is required to build [PyGObject](https://pygobject.readthedocs.io/en/latest/index.html)
- `libwebkit2gtk-4.0-dev` - This is required to summon the player in WebKit.

You can install this dependencies using this command on Debian/Ubuntu based operating systems:
`sudo apt install libgirepository1.0-dev python3-dev libwebkit2gtk-4.0-dev`

After you installed this, you may proceed installing libwinmedia (see next step)

# Installation
You can install latest stable version from PyPI using this command:
```shell
pip install libwinmedia
```

You can install the latest version from Git using this command:
```shell
pip install git+https://github.com/libwinmedia/libwinmedia-py
```
This source might be more stable in some cases, but can be less stable than latest PyPI release

# Requirements
You need to download a libwinmedia.dll for Windows or libwinmedia.so for Linux from the [releases page](https://github.com/harmonoid/libwinmedia/releases) and set it up properly. You can either put it somewhere in the `%PATH%` or set the `LIBWINMEDIA_PATH` environment variable.

On Linux, I recommend using LIBWINMEDIA_PATH environment variable, since there were some troubles finding library in Python `ctypes` library.

Another way to deal with it is to ship libwinmedia shared library with your script and put the directory where your script is located in %PATH% before importing the library:
```py
import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
```
If libwinmedia.dll (or libwinmedia.so) is located elsewhere, you can add that path to `os.environ["PATH"]`.

# Linux limitations
While Linux support is amazing, it comes with some limitations.

For example, you can't use NativeControls class, tags_from_music & tags_from_video functions in Player class.

Otherwise, everything should work!

# Simple start
```py
import libwinmedia

player = libwinmedia.Player()

media = libwinmedia.Media("https://archive.org/download/Kalimba.mp3_377/Kalimba.mp3")

player.open(media)
```

When you don't need any of the created instances, you can dispose them to free up system resources:
```py
player.dispose()
media.dispose()
```

## Important!
The program containing playing media must not exit before player is done playing.

To do this in examples we recommend adding this at the end:
```py
while True:
    pass
```

## Playlists
You can open player (`player.open()`) with `Playlist` instance or with
`Media` instance.

If you open Player with Media, then it will play only one song, but if you open
it with Playlist, then it will create a playlist and play it like that...

Simple example:
```py
import libwinmedia

player = libwinmedia.Player()
media1 = libwinmedia.Media("media1.ogg")
media2 = libwinmedia.Media("media2.ogg")
playlist = libwinmedia.Playlist(media1, media2)

player.open(playlist)
```

## Parameters
You have access to these parameters of the `Player` instance:
- looping
- autoplay
- audio_balance
- rate
- volume
- position

## Callbacks
This library provides callbacks. You need to decorate your functions as follows:
```py
@player.volume_callback()
def callback(volume: float):
    print("Volume callback: " + str(volume * 100))
```

| Callback decorator  | Type, returned from function                                       |
|---------------------|--------------------------------------------------------------------|
| volume_callback     | float (between 0 and 1, thus you might have to multiply it by 100) |
| rate_callback       | float (between 0 and 1, thus you might have to multiply it by 100) |
| completed_callback  | bool                                                               |
| position_callback   | int (in milliseconds)                                              |
| duration_callback   | int (in milliseconds)                                              |

# TODO:
- Implement NativeControls
- Implement Video support

# License
Thanks to [@alexmercerind](https://github.com/alexmercerind). He created one of best libraries for playback, that work with Linux and Windows.

He didn't want to put any restrictions on it, so he used a MIT License.
I also don't want to put any restrictions on Python binding, so I kept MIT License.

You can find license in `LICENSE` file

# Support this project
Show some love to this project and consider starring the repository & check out a whole [libwinmedia](https://github.com/libwinmedia) suite.

While you are at it, you can check also [Harmonoid](https://github.com/harmonoid) project. If you like this library, then share it.

Special thanks to [@alexmercerind](https://github.com/alexmercerind) for [C++ library](https://github.com/libwinmedia/libwinmedia).
Without this library, this project wouldn't exist.

Huge thanks also to [@raitonoberu](https://github.com/raitonoberu) for his massive contributions to Python bindings.
He has brought current easy-to-use design to this library.

# Documentation
This repository includes an example file, called example.py

In it, there is used almost every function this library provides.

Every function is documented (in code or in this file).
