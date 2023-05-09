from module.youtube.youtube_package.list.media_list import MediaList
from module.youtube.youtube_package.media.video import Video


class VideoList(MediaList):

    def __init__(self, list):
        super().__init__(list, "video")

    # 表示する用のリストを生成
    def create_display_list(self):
        display_list = [
            "{:>4}{:>12}     {:}".format(
                element['itag'],
                element["qualityLabel"],
                element['mimeType']
            )for element in self.list
        ]
        return display_list

    def get_video_with_index(self, index):
        return Video(self.list[index])
