# libwinmedia-py
Python bindings for [libwinmedia](https://github.com/harmonoid/libwinmedia), a tiny yet powerful media playback library for Windows.

This library's goal is to make a beginner-friendly, easy-to-use API with many advanced features.

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
You need to download a libwinmedia.dll from the [releases page](https://github.com/harmonoid/libwinmedia/releases) and set it up properly. You can either put it somewhere in the `%PATH%` or set the `LIBWINMEDIA_PATH` enviroment variable.

Another way to deal with it is to ship libwinmedia.dll with your script and put the directory where your script is located in %PATH% before importing the library:
```py
import os
os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]
```
If libwinmedia.dll is located elsewhere, you can add that path to `os.environ["PATH"]`.

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
| position_callback   | int (in miliseconds)                                               |
| duration_callback   | int (in miliseconds)                                               |

# TODO:
- Implement NativeControls
- Implement Video support

# Support this project
Show some love to this project and consider starring the repository & check out a whole [libwinmedia](https://github.com/libwinmedia) suite

Special thanks to [@alexmercerind](https://github.com/alexmercerind) for [C++ library](https://github.com/libwinmedia/libwinmedia).
Without this library, this project wouldn't exist.

Huge thanks also to [@raitonoberu](https://github.com/raitonoberu) for his massive contributions to Python bindings.
He has brought current easy-to-use design to this library.

# Documentation
This repository includes an example file, called example.py

In it, there is used almost every function this library provides.

Every function is documented (in code or in this file).
