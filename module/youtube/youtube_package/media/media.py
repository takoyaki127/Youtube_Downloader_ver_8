from abc import ABCMeta, abstractmethod


class Media(metaclass=ABCMeta):
    def __init__(self, info: dict):
        self.itag = self.__set_itag(info)
        self.bitrate = self.set_bitrate(info)

    def __set_itag(self, info: dict):
        return info["itag"]

    @abstractmethod
    def set_bitrate(self, info: dict):
        pass

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
