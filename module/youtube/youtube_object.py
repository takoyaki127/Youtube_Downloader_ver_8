from pytube import YouTube

from module.youtube.youtube_package.directory import Directory
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
    def __download(self, video_index, audio_index):
        self.dir.write_settings()   # settings.txtを作成
        self.dir.create_tmp()       # 一時保存用のフォルダを作成

        self.video = self.video_list.get_element(video_index)
        self.audio = self.audio_list.get_element(audio_index)
        
        self.video.download()
        self.audio.download()

    # 動画ファイルと音声ファイルを合成
    def __synthesis(self):
        synthesis = self.dir.synthesis_obj(self.video, self.audio)
        synthesis.execute()

    # 合成前に使ったファイルを削除
    def __remove(self):
        self.dir.remove_tmp(self.video)
        self.dir.remove_tmp(self.audio)

    # ディスプレイリストをtuple(video_list, audio_list)で返す
    def display_list_set(self,frame):
        self.video_list.set_list(frame)
        self.audio_list.set_list(frame)

    # ダウンロードから削除までの一通りを行う
    def execute(self, video_index, audio_index):
        self.__download(video_index, audio_index)
        self.__synthesis()
        self.__remove()
