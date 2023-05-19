from module.youtube.youtube_object import YoutubeObject
from module.frame.module.directory_entry import DirectoryEntry
from module.frame.module.url_frame import URLFrame

class CreateYouTube():
    def __init__(self, url:URLFrame, dir:DirectoryEntry) -> None:
        self.__url = url
        self.__dir = dir

    def create(self):
        url = self.__url.get()
        dir = self.__dir.get()
        return YoutubeObject(url, dir)