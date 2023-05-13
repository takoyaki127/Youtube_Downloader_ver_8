from module.youtube.youtube_package.media.media import Media
from module.youtube.youtube_package.download.download import Download
from moviepy.video.io.VideoFileClip import VideoFileClip


class Video(Media):
    file_name = "movie.mp4"

    def __init__(self, info: dict, download: Download):
        super().__init__(info, download, Video.file_name)

    def set_bitrate(self, info: dict):
        return f"{info['bitrate']/1000}k"

    def file_clip(self, tmp):
        return VideoFileClip(tmp + "\\" + self.filename)
