from module.youtube.youtube_package.list.media_list import MediaList
from module.youtube.youtube_package.media.video import Video
from module.frame.display_list import DisplayList

class VideoList(MediaList):

    def __init__(self, list, download):
        super().__init__(list, "video", download)

    # 表示する用のリストを生成
    def create_display_list(self):
        display_list = [
            "{:>4}{:>12}{:^30}{:<20}".format(
                element['itag'],
                element["qualityLabel"],
                self.__mimetype_arrange(element['mimeType'], 0),
                self.__mimetype_arrange(element['mimeType'], 1)
            )for element in self.list
        ]
        return display_list

    @staticmethod
    def __mimetype_arrange(mimetype: str, n):
        return mimetype.split(';')[n]

    def get_element(self, index):
        return Video(self.list[index], self.download)

    def set(self, display:DisplayList):
        display.set_video(self.display_list)