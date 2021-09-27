class MusicTags:
    @staticmethod
    def get(tags) -> dict:
        return {
            "album": tags[0].decode(),
            "albumArtist": tags[1].decode(),
            "bitrate": int(tags[2].decode()),
            "composers": tags[3].decode(),
            "conductors": tags[4].decode(),
            "duration": int(tags[5].decode()),
            "genre": tags[6].decode(),
            "producers": tags[7].decode(),
            "publisher": tags[8].decode(),
            "rating": int(tags[9].decode()),
            "subtitle": tags[10].decode(),
            "title": tags[11].decode(),
            "trackNumber": int(tags[12].decode()),
            "writers": tags[13].decode(),
            "year": int(tags[14].decode()),
        }

class VideoTags:
    @staticmethod
    def get(tags):
        return {
            "bitrate": tags[0].decode(),
            "directors": tags[1].decode(),
            "duration": tags[2].decode(),
            "height": tags[3].decode(),
            "keywords": tags[4].decode(),
            "longitude": tags[5].decode(),
            "latitude": tags[6].decode(),
            "orientation": tags[7].decode(),
            "producers": tags[8].decode(),
            "rating": tags[9].decode(),
            "subtitle": tags[10].decode(),
            "title": tags[11].decode(),
            "width": tags[12].decode(),
            "writers": tags[13].decode(),
            "year": tags[14].decode(),
        }
