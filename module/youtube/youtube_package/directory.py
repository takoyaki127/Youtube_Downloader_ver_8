import os
from module.youtube.youtube_package.settings import Settings
from module.youtube.youtube_package.download.download import Download
from module.youtube.youtube_package.media.media import Media
from module.youtube.youtube_package.title.title import Title
from module.youtube.youtube_package.synthesis.synthesis import Synthesis


class Directory():
    def __init__(self, download, title):
        self.__download = download
        self.__tmp = self.__download + r"/tmp"
        self.__output = self.__create_output(title)

    def __create_output(self, title):
        title = Title.escape(title)
        return self.__download + "/" + title + ".mp4"

    def create_tmp(self):
        if not os.path.isdir(self.__tmp):
            os.makedirs(self.__tmp)

    def write_settings(self):
        Settings.write_dir(self.__download)

    def get_download_obj(self, stream):
        return Download(stream, self.__tmp)

    def remove_tmp(self, media: Media):
        media.remove(self.__tmp)

    def synthesis_obj(self, video, audio):
        return Synthesis(self.__tmp, self.__output, video, audio)
