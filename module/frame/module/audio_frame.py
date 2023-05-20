import tkinter as tk
from module.frame.module.display_list import DisplayList
from module.frame.module.index import Index
from module.frame.module.index_label import IndexLabel

class AudioFrame():
    def __init__(self, root, label_font, listbox_font) -> None:
        self.__frame = tk.Frame(root)
        self.__frame.pack(expand=1, fill='both')
        self.__add_label(label_font)
        self.__add_listbox(listbox_font)

    
    def __add_label(self, font):
        self.__label = tk.Label(self.__frame, text='音声リスト', font=font)
        self.__label.pack(anchor='nw')

    def __add_listbox(self, font):
        self.__listbox = tk.Listbox(
            self.__frame,
            font=font,
            activestyle='none'
        )
        self.__listbox.pack(fill='both')

    def display_list(self, video_listbox):
        return  DisplayList(video_listbox ,self.__listbox)
    
    def index(self, video_listbox, video_label:tk.Label):
        label = IndexLabel(video_label, self.__label)
        return Index(video_listbox, self.__listbox, label)