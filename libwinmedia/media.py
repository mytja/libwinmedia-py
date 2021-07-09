from .library import lib

class Media(object):
    def __init__(self, uri: str, parse: bool = False):
        self.uri = uri
        self.id = lib.Media_create(uri, parse)

    def dispose(self) -> None:
        lib.Media_dispose(self.id)

    @property
    def duration(self) -> int:
        return lib.Media_getDuration(self.id)
