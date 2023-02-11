# from youtube_package.video_list import VideoList


class Video():
    file_name = "movie.mp4"

    def __init__(self, video_info: dict):
        self.itag = video_info["itag"]
        self.bitrate = f"{video_info['bitrate']/1000}k"

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
