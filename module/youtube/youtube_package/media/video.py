from module.youtube.youtube_package.media.media import Media
# from media import Media


class Video(Media):
    file_name = "movie.mp4"

    def __init__(self, info: dict):
        super().__init__(info)

    def set_bitrate(self, info: dict):
        return f"{info['bitrate']/1000}k"


if __name__ == "__main__":
    dict_ = {"itag": 10, "bitrate": 10}
    video = Video(dict_)
    pass
