from youtube_package.video_list import VideoList


class Video():
    file_name = "movie.mp4"

    def __init__(self, video: VideoList, index):
        self.index = index
        self.itag = video.list[self.index]["itag"]
        x = video.list[self.index]['bitrate']
        self.bitrate = f"{video.list[self.index]['bitrate']/1000}k"

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
