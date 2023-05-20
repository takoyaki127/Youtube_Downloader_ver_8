from abc import ABCMeta, abstractmethod

class MediaList(metaclass=ABCMeta):
    def __init__(self, list, mimeType, download):
        self.list = self.list_arrange(list, mimeType)
        self.display_list = self.create_display_list()
        self.download = download

    # mimeTypeには"video"か"audio"を入力
    def list_arrange(self, original_list, mimeType):
        arranged_list = list(
            filter(lambda x: mimeType in x["mimeType"], original_list)
        )
        arranged_list.sort(key=lambda x: x["bitrate"], reverse=True)
        return arranged_list

    # 表示用のリストを作成
    @abstractmethod
    def create_display_list(self):
        pass

    @abstractmethod
    def set(self, display):
        pass

    @abstractmethod
    def element(self, index):
        pass
