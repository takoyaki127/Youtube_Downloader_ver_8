from pytube import YouTube
from multiprocessing import Process

from module.youtube.youtube_package.directory import Directory
from module.youtube.youtube_package.synthesis.synthesis2 import Synthesis
from module.youtube.youtube_package.list.create_list import CreateList


class YoutubeObject(YouTube):
    def __init__(self, link, dir):
        super().__init__(link)
        self.dir = Directory(dir, self.title)

        # リストを作成
        cl = CreateList(self.streaming_data,self.streams,self.dir)
        self.video_list = cl.video()
        self.audio_list = cl.audio()

    # インデックスを使ってダウンロード
    def download_with_index(self, video_index, audio_index):
        self.dir.write_to_settings() # settings.txtを作成
        self.dir.create_tmp_dir()

        self.video = self.video_list.get_video_with_index(video_index)
        self.video.download()
        
        self.audio = self.audio_list.get_audio_with_index(audio_index)
        self.audio.download()

    # 動画ファイルと音声ファイルを合成
    def synthesis(self):
        synthesis = self.dir.synthesis_obj()
        synthesis.execute(self.video, self.audio)

    # 合成前に使ったファイルを削除
    def remove(self):
        self.dir.remove_tmp(self.video)
        self.dir.remove_tmp(self.audio)

    # ディスプレイリストをtuple(video_list, audio_list)で返す
    def display_lists_set_to(self,frame):
        frame.setList(
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

