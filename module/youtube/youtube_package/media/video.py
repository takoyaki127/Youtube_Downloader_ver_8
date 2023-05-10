# from module.youtube.youtube_package.media.media import Media
from media import Media

# from module.youtube.youtube_package.download.download import Download
from download.download import Download


class Video(Media):
    file_name = "movie.mp4"

    def __init__(self, info: dict, media: Download):
        super().__init__(info, media)

    def set_bitrate(self, info: dict):
        return f"{info['bitrate']/1000}k"

    def set_filename(self):
        return Video.file_name


if __name__ == "__main__":
    dict_ = {"itag": 10, "bitrate": 10}
    video = Video(dict_)
    pass
