from pytube.query import StreamQuery


class Download():
    def __init__(self, media: StreamQuery, output):
        self.media = media
        self.output = output

    # ダウンロード開始
    def download(self,itag,filename):
        self.media.get_by_itag(itag).download(
            output_path=self.output,
            filename=filename
        )
