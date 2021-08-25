from .library import lib
from ctypes import POINTER, c_wchar, c_wchar_p
from itertools import takewhile

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

    def get_metadata(self) -> str:
        # TODO: add docstring
        lib.TagsFromMusic.args = [c_wchar_p]
        lib.TagsFromMusic.restype = POINTER(c_wchar_p)

        meta = lib.TagsFromMusic(self.uri)

        self.tags = []
        for s in meta:
            if s == None:
                return self.tags
            self.tags.append(s)
            print(s)

        return self.tags

    def extract_thumbnail(self, outputFolder: str, outputFile: str) -> None:
        """Extract the thumbnail and save it to a file.

        Args:
            outputFolder (str): A folder for saving the thumbnail.
            outputFile (str): A name of the thumbnail file.
        """
        lib.TagsExtractThumbnail(self.uri, "file://" + outputFolder, outputFile, 2, 400)
