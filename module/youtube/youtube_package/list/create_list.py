from module.youtube.youtube_package.list.video_list import VideoList
from module.youtube.youtube_package.list.audio_list import AudioList


class CreateList():

    def __init__(self, data_list, streams, dir):
        self.__data_list = CreateList.__date_arrange(data_list)
        self.download = dir.get_download_obj(streams)

    @staticmethod
    def __date_arrange(data_list):
        return data_list["adaptiveFormats"]

    def video(self):
        return VideoList(self.__data_list, self.download)

    def audio(self):
        return AudioList(self.__data_list, self.download)
