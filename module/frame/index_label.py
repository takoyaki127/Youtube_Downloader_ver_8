from tkinter import Label

class IndexLabel():
    def __init__(self, video:Label, audio:Label) -> None:
        self.__video = video
        self.__audio = audio

    def update_video(self, index):
        self.__video["text"] = self.create_text("動画", index)

    def update_audio(self, index):
        self.__audio["text"] = self.create_text("音声", index)

    @staticmethod
    def create_text(type, index):
        return f"{type}リスト index={index}"