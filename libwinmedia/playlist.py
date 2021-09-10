from typing import List

from .media import Media


class Playlist:
    def __init__(self, *medias: Media):
        self.medias = list(medias)

    def add(self, media) -> None:
        self.medias.append(media)

    def remove(self, media) -> None:
        self.medias.remove(media)

    def delete(self, i: int) -> None:
        self.medias.pop(i)

    @property
    def uris(self) -> List[str]:
        uris = []
        for media in self.medias:
            uris.append(media.uri)
        return uris

    @property
    def ids(self) -> List[int]:
        ids = []
        for media in self.medias:
            ids.append(media.id)
        return ids

    @property
    def length(self) -> int:
        return len(self.medias)
