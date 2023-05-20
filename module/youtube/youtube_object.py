from pytube import YouTube

from module.youtube.youtube_package.directory import Directory
from module.youtube.youtube_package.list.create_list import CreateList


class YoutubeObject(YouTube):
    def __init__(self, link, dir):
        super().__init__(link)
        self.__dir = Directory(dir, self.title)

        # リストを作成
        cl = CreateList(self.streaming_data,self.streams,self.__dir)
        self.__video_list = cl.video()
        self.__audio_list = cl.audio()

    # インデックスを使ってダウンロード
    def __download(self, video_index, audio_index):
        self.__dir.write_settings()   # settings.txtを作成
        self.__dir.create_tmp()       # 一時保存用のフォルダを作成

        self.__video = self.__video_list.element(video_index)
        self.__audio = self.__audio_list.element(audio_index)
        
        self.__video.download()
        self.__audio.download()

    # 動画ファイルと音声ファイルを合成
    def __synthesis(self):
        synthesis = self.__dir.create_synthesis(self.__video, self.__audio)
        synthesis.execute()

    # 合成前に使ったファイルを削除
    def __remove(self):
        self.__dir.remove_tmp(self.__video)
        self.__dir.remove_tmp(self.__audio)

    def display(self, display):
        self.__video_list.set(display)
        self.__audio_list.set(display)

    # ダウンロードから削除までの一通りを行う
    def execute(self, video_index, audio_index):
        self.__download(video_index, audio_index)
        self.__synthesis()
        self.__remove()

    def explorer(self):
        return self.__dir.explorer()
