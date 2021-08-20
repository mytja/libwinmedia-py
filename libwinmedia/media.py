import os

from .library import lib
from ctypes import POINTER, c_wchar, wstring_at


class Media(object):
    def __init__(self, id: int, uri: str, parse: bool = False):
        self.uri = uri
        self.id = id
        lib.MediaCreate(id, uri, parse)

    def dispose(self) -> None:
        lib.MediaDispose(self.id)

    @property
    def duration(self) -> int:
        return lib.MediaGetDuration(self.id)

    def getMetadata(self) -> str:
        lib.TagsFromMusic.args = [POINTER(c_wchar)]
        lib.TagsFromMusic.restype = POINTER(POINTER(c_wchar))

        return lib.TagsFromMusic(self.uri)

    def extractThumbnail(self, outputFolder: str, outputFile: str) -> None:
        Thumb = lib.TagsExtractThumbnail

        folder = "file://" + outputFolder
        print(folder)
        print(outputFile)
        print(self.uri)

        Thumb(self.uri, "file://" + outputFolder, outputFile, 2, 400)
