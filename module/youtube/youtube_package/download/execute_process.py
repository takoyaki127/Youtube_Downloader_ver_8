from module.youtube.youtube_object import YoutubeObject
from multiprocessing import Process
from threading import Thread


class ExecuteProcess():
    def __init__(self, video_index, audio_index) -> None:
        self.__video = video_index
        self.__audio = audio_index

    def start(self, youtube: YoutubeObject, display_frame=None):
        p = Process(
            target=youtube.execute,
            args=(self.__video, self.__audio))
        p.start()

        Thread(target=self.__wait, args=(p, display_frame)).start()

    def __wait(self, p: Process, display_frame):
        p.join()
        if display_frame:
            display_frame()
