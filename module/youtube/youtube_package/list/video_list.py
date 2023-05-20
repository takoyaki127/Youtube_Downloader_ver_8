from module.youtube.youtube_package.list.media_list import MediaList
from module.youtube.youtube_package.media.video import Video
from module.frame.module.display_list import DisplayList
from module.youtube.youtube_package.list.create_video_list import CreateVideoList

class VideoList(MediaList):

    def __init__(self, list, download):
        super().__init__(list, "video", download)

    # 表示する用のリストを生成
    def create_display_list(self):
        return CreateVideoList.create(self.list)

    def get_element(self, index):
        return Video(self.list[index], self.download)

    def set(self, display:DisplayList):
        display.set_video(self.display_list)