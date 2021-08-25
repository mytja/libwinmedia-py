from .library import lib
from ctypes import POINTER, c_wchar, c_wchar_p
from .tags import MusicTags, VideoTags

media_id = 0


class Media(object):
    """A class representing a media file."""

    def __init__(self, uri: str, parse: bool = False):
        """Create a new Media instance.

        The URI can be either a local file (e.g. "file://C:/music/track.mp3")
        or an HTTP URL (e.g. "https://www.kozco.com/tech/piano2.wav").

        Args:
            uri (str): A URI of the media.
            parse (bool, optional): Whether to parse the media. Defaults to False.
        """

        global media_id
        self.id = media_id
        self.uri = uri
        lib.MediaCreate(self.id, uri, parse)
        media_id += 1

    def dispose(self) -> None:
        """Release system resources and kill the media instance."""
        lib.MediaDispose(self.id)

    @property
    def duration(self) -> int:
        return lib.MediaGetDuration(self.id)

    def TagsFromMusic(self) -> dict:
        # TODO: add docstring
        lib.TagsFromMusic.args = [c_wchar_p]
        lib.TagsFromMusic.restype = POINTER(c_wchar_p)

        meta = lib.TagsFromMusic(self.uri)
        return MusicTags.get(meta)

    def TagsFromVideo(self) -> dict:
        lib.TagsFromVideo.args = [c_wchar_p]
        lib.TagsFromVideo.restype = POINTER(c_wchar_p)

        meta = lib.TagsFromVideo(self.uri)
        return VideoTags.get(meta)

    def extract_thumbnail(self, outputFolder: str, outputFile: str) -> None:
        """Extract the thumbnail and save it to a file.

        Args:
            outputFolder (str): A folder for saving the thumbnail.
            outputFile (str): A name of the thumbnail file.
        """
        lib.TagsExtractThumbnail(self.uri, "file://" + outputFolder, outputFile, 2, 400)
