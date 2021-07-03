import os

class MediaFile:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.extension = self.filename.split(".")[-1]

class Media:
    def __init__(self, mediaInstance, lib):
        self.media = mediaInstance
        self.lib = lib

        #self.duration = self.getDuration()
    
    def dispose(self):
        self.lib.Media_dispose(self.media)
    
    # Currently very very buggy
    def getDuration(self) -> int:
        return self.lib.Media_getDuration(self.media)
