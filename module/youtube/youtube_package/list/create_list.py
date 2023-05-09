from module.youtube.youtube_package.list.video_list import VideoList
from module.youtube.youtube_package.list.audio_list import AudioList


class CreateList():

    def __init__(self, data_list):
        self.__data_list = CreateList.__date_arrange(data_list)

    @staticmethod
    def __date_arrange(data_list):
        return data_list["adaptiveFormats"]

    def video(self):
        return VideoList(self.__data_list)

    def audio(self):
        return AudioList(self.__data_list)
