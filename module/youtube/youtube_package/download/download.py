from pytube.query import StreamQuery


class Download():
    def __init__(self, media: StreamQuery, itag, output, filename):
        self.media = media
        self.itag = itag
        self.output = output
        self.filename = filename

    # ダウンロード開始
    def download(self):
        self.media.get_by_itag(self.itag).download(
            output_path=self.output,
            filename=self.filename
        )
