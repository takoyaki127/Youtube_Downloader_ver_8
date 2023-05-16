from tkinter import StringVar
from module.youtube.youtube_object import YoutubeObject

class CreateYouTube():
    def __init__(self, url:StringVar, dir:StringVar) -> None:
        self.__url = url
        self.__dir = dir

    def create(self):
        url = self.__url.get()
        dir = self.__dir.get()
        return YoutubeObject(url, dir)