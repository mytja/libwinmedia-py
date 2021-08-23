# libwinmedia-py
Python bindings for [libwinmedia](https://github.com/harmonoid/libwinmedia), a tiny yet powerful media playback library for Windows.

# Installation
You can install latest version from Git using this command:
```shell
pip install git+https://github.com/libwinmedia/libwinmedia-py
```

# Requirements
You need to download a libwinmedia.dll from the [releases page](https://github.com/harmonoid/libwinmedia/releases) and set it up properly. You can either put it somewhere in the %PATH% or set the `LIBWINMEDIA_PATH` enviroment variable.

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

## Parameters
You have access to thses parameters of the `Player`:
- looping
- autoplay
- audio_balance
- rate
- volume
- position

## Callbacks
This library provides callbacks.
Example:
```py
from ctypes import CFUNCTYPE, c_float

@CFUNCTYPE(None, c_float)
def callbackVolume(volume: float):
    print("Volume callback: " + str(volume * 100))

player.setVolumeEventHandler(callbackVolume)
```
### We got these callbacks, which return type:
| Callback function setter | Type, returned from function                                       |
|--------------------------|--------------------------------------------------------------------|
| setVolumeEventHandler    | float (between 0 and 1, thus you might have to multiply it by 100) |
| setRateEventHandler      | float (between 0 and 1, thus you might have to multiply it by 100) |
| setIsDoneEventHandler    | bool                                                               |
| setPositionEventHandler  | int (in miliseconds)                                               |
| setDurationEventHandler  | int (in miliseconds)                                               |

# TODO:
- Implement NativeControls
- Implement Video support
- Implement Video & Audio tags (metadata)

# Support this project
Show some love to this project and consider starring the repository & check out a whole [libwinmedia](https://github.com/libwinmedia) suite

Special thanks to [@alexmercerind](https://github.com/alexmercerind) for [C++ library](https://github.com/libwinmedia/libwinmedia).
Without this library, this project wouldn't exist.

# Documentation
This repository includes an example file, called example.py

In it, there is used almost every function this library provides.

Every function is documented (in code or in this file).