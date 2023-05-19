import tkinter as tk
from module.frame.module.audio_frame import AudioFrame


class VideoFrame():
    def __init__(self, root, label_font, listbox_font) -> None:
        self.__frame = tk.Frame(root)
        self.__frame.pack(expand=1, fill='both')
        self.__add_label(label_font)
        self.__add_listbox(listbox_font)

    def __add_label(self, font):
        self.__label = tk.Label(self.__frame, text='動画リスト', font=font)
        self.__label.pack(anchor='nw')

    def __add_listbox(self, font):
        self.__listbox = tk.Listbox(
            self.__frame,
            font=font,
            activestyle='none'
        )
        self.__listbox.pack(fill='both')

    def display_list(self, audio_frame:AudioFrame):
        return audio_frame.display_list(self.__listbox)
    
    def index(self,audio_frame:AudioFrame):
        return audio_frame.index(self.__listbox, self.__label)
