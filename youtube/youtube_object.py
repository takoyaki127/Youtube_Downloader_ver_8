from pytube import YouTube
import os

from youtube_package.directory import Directory
from youtube_package.video_list import VideoList
from youtube_package.audio_list import AudioList
from youtube_package.video import Video
from youtube_package.audio import Audio
from youtube_package.synthesis import Synthesis


class YoutubeObject(YouTube):
    def __init__(self, link, dir):
        super().__init__(link)
        self.title = self.arrange_title(self.title)
        self.dir = Directory(dir, self.title)

        list = self.streaming_data["adaptiveFormats"]
        self.video_list = VideoList(list)
        self.audio_list = AudioList(list)

    @staticmethod
    def arrange_title(title: str):
        result = title.translate(str.maketrans({
            "\\": "￥", "/": "／", ":": "：",
            "*": "＊", "?": "？", "\"": "”",
            "<": "＜", ">": "＞", "|": "｜"
        }))
        return result

    def download_with_index(self, video_index, audio_index):
        self.video = Video(self.video_list, video_index)
        self.audio = Audio(self.audio_list, audio_index)
        video_itag = self.video.get_itag()
        audio_itag = self.audio.get_itag()
        output = self.dir.get_tmp()

        self.dir.create_tmp_dir()

        self.download(video_itag, output, self.video.file_name)
        self.download(audio_itag, output, self.audio.file_name)

    def download(self, itag, output, file_name):
        self.streams.get_by_itag(itag).download(
            output_path=output, filename=file_name)

    def synthesis(self):
        video = Synthesis(self.video, self.audio, self.dir)
        video.synthesis()

    def remove(self):
        tmp = self.dir.get_tmp()
        video = self.video.file_name
        audio = self.audio.file_name

        os.remove(tmp + "\\" + video)
        os.remove(tmp + "\\" + audio)


if __name__ == "__main__":
    link = "https://youtu.be/5tc14WHUoMw"
    dir = "D:/Downloads/Youtube_Downloads/tmp"
    object = YoutubeObject(link, dir)

    object.download_with_index(0, 0)
    object.synthesis()
    object.remove()
