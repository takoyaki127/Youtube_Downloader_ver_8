from abc import ABCMeta, abstractmethod

from module.youtube.youtube_package.download.download import Download


class Media(metaclass=ABCMeta):
    def __init__(self, info: dict, media: Download):
        self.itag = self.__set_itag(info)
        self.bitrate = self.set_bitrate(info)
        self.filename = self.set_filename()
        self.media = media

    def __set_itag(self, info: dict):
        return info["itag"]

    @abstractmethod
    def set_bitrate(self, info: dict):
        pass

    @abstractmethod
    def set_filename(self):
        pass

    def download(self):
        self.media.download(self.itag, self.filename)

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
