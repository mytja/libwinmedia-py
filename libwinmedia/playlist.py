class Playlist:
    medias = []

    def add(self, media) -> None:
        self.medias.append(media)
    
    def remove(self, media) -> None:
        self.medias.remove(media)
    
    def delete(self, i: int) -> None:
        self.medias.pop(i)
    
    def getAllUris(self) -> list:
        uris = []
        for media in self.medias:
            uris.append(media.uri)
        return uris
    
    def getAllIDs(self) -> list:
        ids = []
        for media in self.medias:
            ids.append(media.id)
        return ids