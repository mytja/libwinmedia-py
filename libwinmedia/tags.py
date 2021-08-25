class MusicTags:
    @staticmethod
    def get(tags) -> dict:
        return {
            "album": tags[0],
            "albumArtist": tags[1],
            "bitrate": int(tags[2]),
            "composers": tags[3],
            "conductors": tags[4],
            "duration": int(tags[5]),
            "genre": tags[6],
            "producers": tags[7],
            "publisher": tags[8],
            "rating": int(tags[9]),
            "subtitle": tags[10],
            "title": tags[11],
            "trackNumber": int(tags[12]),
            "writers": tags[13],
            "year": int(tags[14]),
        }

class VideoTags:
    @staticmethod
    def get(tags):
        return {
            "bitrate": tags[0],
            "directors": tags[1],
            "duration": tags[2],
            "height": tags[3],
            "keywords": tags[4],
            "longitude": tags[5],
            "latitude": tags[6],
            "orientation": tags[7],
            "producers": tags[8],
            "rating": tags[9],
            "subtitle": tags[10],
            "title": tags[11],
            "width": tags[12],
            "writers": tags[13],
            "year": tags[14],
        }
