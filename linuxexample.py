import libwinmedia

media = libwinmedia.Media("https://p.scdn.co/mp3-preview/669eef4c25c47eb54c8c0bceee55b94519f3b0c1?cid=774b29d4f13844c495f206cafdad9c86")
player = libwinmedia.Player()
player.open(media)
player.play()
while True:
    pass