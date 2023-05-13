from pytube.query import StreamQuery


class Download():
    def __init__(self, stream: StreamQuery, output):
        self.__stream = stream
        self.__output = output

    def download(self, itag, filename):
        self.__stream.get_by_itag(itag).download(
            output_path=self.__output,
            filename=filename
        )
