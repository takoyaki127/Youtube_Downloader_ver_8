from pytube.query import StreamQuery

from module.youtube.youtube_package.download.download import Download

# indexからDownloadインスタンスを作成
class IndexToItagConverter():
    def __init__(self, media: StreamQuery, index, output, filename):
        self.media = media
        self.index = index
        self.output = output
        self.filename = filename

    def create_download(self):
        return Download(
            self.media,
            self.__itag(),
            self.output,
            self.filename
        )

    def __itag(self):
        # self.index -> itag に変換して返す処理 
        return 0
