import os
from module.youtube.youtube_package.settings import Settings
from module.youtube.youtube_package.download.download import Download
from module.youtube.youtube_package.media.media import Media
from module.youtube.youtube_package.title.title import Title
from module.youtube.youtube_package.synthesis.synthesis import Synthesis


class Directory():
    def __init__(self, download, title):
        self.download = download
        self.tmp = self.download + r"\tmp"
        self.output = self.__create_output(title)

    def __create_output(self, title):
        title = Title.escape(title)
        return self.download + "\\" + title + ".mp4"

    def create_tmp(self):
        if not os.path.isdir(self.tmp):
            os.makedirs(self.tmp)

    def write_settings(self):
        Settings.write_dir(self.download)

    def get_download_obj(self, stream):
        return Download(stream, self.tmp)

    def remove_tmp(self, media: Media):
        media.remove(self.tmp)

    def synthesis_obj(self):
        return Synthesis(self.tmp, self.output)
