import libwinmedia
import time
from ctypes import c_int32, CFUNCTYPE


if __name__ == "__main__":
    player = libwinmedia.Player()

    @player.volume_callback()
    def callback_volume(volume: float):
        print(f"Player volume   : {volume}")

    @player.rate_callback()
    def callback_rate(rate: float):
        print(f"Player rate     : {rate}")

    @player.position_callback()
    def callback_position(position: int):
        print(f"Player position : {position}")

    playlist = libwinmedia.Playlist(
        libwinmedia.Media(
            "https://p.scdn.co/mp3-preview/18f50618e8737c8a1f3b50a653023c5576af8955?cid=774b29d4f13844c495f206cafdad9c86"
        ),
        libwinmedia.Media(
            "https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86"
        ),
    )
    player.open(playlist)
    player.play()

    player.volume = 0.5
    player.rate = 1.25
    input()
