from tkinter import Listbox

from module.frame.index_label import IndexLabel
from module.youtube.youtube_package.media.type import Type
from module.youtube.youtube_package.download.execute_process import ExecuteProcess


class Index():
    def __init__(self, video:Listbox, audio:Listbox, label:IndexLabel) -> None:
        self.__video_box = video
        self.__audio_box = audio
        self.__label = label
        self.__video = -1
        self.__audio = -1
        self.__set_bind()

    def __set_bind(self):
        self.__video_box.bind('<<ListboxSelect>>', self.__set_video)
        self.__audio_box.bind('<<ListboxSelect>>', self.__set_audio)

    def __set_video(self, event):
        index = self.__video_box.curselection()
        if len(index) == 1:
            self.__video = index[0]
            self.__update_label(Type.Video)

    def __set_audio(self, event):
        index = self.__audio_box.curselection()
        if len(index) == 1:
            self.__audio = index[0]
            self.__update_label(Type.Audio)

    def __update_label(self, type:type):
        if type == Type.Video:
            self.__label.update_video(self.__video)
            return

        if type == Type.Audio:
            self.__label.update_audio(self.__audio)
            return

    def execute_process(self):
        if self.__video != -1 and self.__audio != -1:
            return ExecuteProcess(self.__video, self.__audio)
        
        return None