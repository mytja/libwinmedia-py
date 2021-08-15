from .library import lib

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
