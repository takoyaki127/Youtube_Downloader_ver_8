from pytube import YouTube
import os
from multiprocessing import Process

from module.youtube.youtube_package.directory import Directory
from module.youtube.youtube_package.synthesis.synthesis import Synthesis
from module.youtube.youtube_package.list.create_list import CreateList
from module.youtube.youtube_package.title.title import Title


class YoutubeObject(YouTube):
    def __init__(self, link, dir):
        super().__init__(link)
        self.title = Title.escape(self.title)
        self.dir = Directory(dir, self.title)

        # リストを作成
        cl = CreateList(self.streaming_data)
        self.video_list = cl.video()
        self.audio_list = cl.audio()

    # インデックスを使ってダウンロード
    def download_with_index(self, video_index, audio_index):
        self.video = self.video_list.get_video_with_index(video_index)
        self.audio = self.audio_list.get_audio_with_index(audio_index)

        video_itag = self.video.get_itag()
        audio_itag = self.audio.get_itag()
        output = self.dir.get_tmp()

        self.dir.write_to_text_file()
        self.dir.create_tmp_dir()
        self._download(video_itag, output, self.video.file_name)
        self._download(audio_itag, output, self.audio.file_name)

    # itagを使ってダウンロード
    def _download(self, itag, output, file_name):
        self.streams.get_by_itag(itag).download(
            output_path=output, filename=file_name)

    # 動画ファイルと音声ファイルを合成
    def synthesis(self):
        Synthesis(self.video, self.audio, self.dir).execute()

    # 合成前に使ったファイルを削除
    def remove(self):
        tmp_dir = self.dir.get_tmp()

        os.remove(tmp_dir + "\\" + self.video.file_name)
        os.remove(tmp_dir + "\\" + self.audio.file_name)

    # ディスプレイリストをtuple(video_list, audio_list)で返す
    def get_display_lists(self):
        return (
            self.video_list.get_display_list(),
            self.audio_list.get_display_list()
        )

    # ダウンロードから削除までの一通りを行う
    def execute(self, video_index, audio_index):
        self.download_with_index(video_index, audio_index)
        self.synthesis()
        self.remove()

    # ダウンロードから削除までの一通りを行うプロセスを作成
    def prepare_multiprocessing(self,video_index,audio_index):
        return Process(target=self.execute,args=(video_index,audio_index))


def main(link, dir):
    object = YoutubeObject(link, dir)

    object.download_with_index(0, 0)
    object.synthesis()
    object.remove()


if __name__ == "__main__":
    link: str = input("URLを入力->")
    dir: str = "D:/Downloads/Youtube_Downloads/tmp"
    main(link=link, dir=dir)
