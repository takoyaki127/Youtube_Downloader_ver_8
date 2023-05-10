import os
from module.youtube.youtube_package.settings import Settings


class Directory():
    def __init__(self, download, title):
        self.download = download
        self.tmp = self.download + r"\tmp"
        self.output = self.download + "\\" + title + ".mp4"

    def get_tmp(self) -> str:
        return self.tmp

    def getOutput(self):
        return self.output

    def create_tmp_dir(self):
        if not os.path.isdir(self.tmp):
            os.makedirs(self.tmp)

    def write_to_settings(self):
        Settings.write_dir(self.download)
