from youtube_package.root_list import RootList


class VideoList(RootList):

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
