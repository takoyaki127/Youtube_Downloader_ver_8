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
        self.output = self.create_output(title)

    def create_output(self, title):
        title = self.title_escape(title)
        return self.download + "\\" + title + ".mp4"

    def title_escape(self, title):
        return Title.escape(title)

    def get_tmp(self) -> str:
        return self.tmp

    def getOutput(self):
        return self.output

    def create_tmp_dir(self):
        if not os.path.isdir(self.tmp):
            os.makedirs(self.tmp)

    def write_to_settings(self):
        Settings.write_dir(self.download)

    def get_download_obj(self, stream):
        return Download(stream, self.tmp)

    def remove_tmp(self, media: Media):
        media.remove(self.tmp)

    def synthesis_obj(self):
        return Synthesis(self.tmp, self.output)
