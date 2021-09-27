import os
import platform

from .library import lib
from ctypes import POINTER, c_char_p
from .tags import MusicTags, VideoTags

media_id = 0


class Media(object):
    """A class representing a media file."""

    def __init__(self, uri: str, parse: bool = True):
        """Create a new Media instance.

        The URI can be either a local file (e.g. "file://C:/music/track.mp3")
        or an HTTP URL (e.g. "https://www.kozco.com/tech/piano2.wav").

        Args:
            uri (str): A URI of the media.
            parse (bool, optional): Whether to parse the media. Defaults to True. True is required for duration parsing
        """

        global media_id
        self.id = media_id
        if not os.path.isabs(uri) and not ("https" in uri or "http" in uri):
            uri = os.path.join(os.path.dirname(os.path.abspath(uri)), uri)
        self.uri = uri
        if platform.system() != "Linux":
            lib.MediaCreate(self.id, uri.encode("utf-8"), parse)
        media_id += 1

    def dispose(self) -> None:
        """Release system resources and kill the media instance."""

        lib.MediaDispose(self.id)

    @property
    def duration(self) -> int:
        return lib.MediaGetDuration(self.id)

    def tags_from_music(self) -> dict:
        # TODO: add docstring
        lib.TagsFromMusic.args = [c_char_p]
        lib.TagsFromMusic.restype = POINTER(c_char_p)

        meta = lib.TagsFromMusic(self.uri.encode("utf-8"))
        return MusicTags.get(meta)

    def tags_from_video(self) -> dict:
        lib.TagsFromVideo.args = [c_char_p]
        lib.TagsFromVideo.restype = POINTER(c_char_p)

        meta = lib.TagsFromVideo(self.uri.encode("utf-8"))
        return VideoTags.get(meta)

    def extract_thumbnail(self, output_folder: str, output_file: str) -> None:
        """Extract the thumbnail and save it to a file.

        Args:
            output_folder (str): A folder for saving the thumbnail.
            output_file (str): A name of the thumbnail file.
        """
        lib.TagsExtractThumbnail(self.uri.encode(), ("file://" + output_folder).encode(), output_file.encode(), 2, 400)
