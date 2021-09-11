import libwinmedia

player = libwinmedia.Player(True)

player.set_position_callback(lambda position: print(f"{position} ms."))
media1 = libwinmedia.Media(
    "https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86"
)
media2 = libwinmedia.Media("test.mp3")
playlist = libwinmedia.Playlist(media1, media2)

player.open(playlist)
