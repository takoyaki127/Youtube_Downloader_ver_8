import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.frame.create_youtube import CreateYouTube
from module.frame.module.url_frame import URLFrame
from module.frame.module.directory_frame import DirectlyFrame


class Frame1(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.__create_widget()

    def __create_widget(self):
        self.btm = BottomFrame(self, '次へ')
        main = MainFrame(self, padx=20)

        label_font = ('meiryo', 10)
        entry_font = ('meiryo', 13)

        self.__dir_frame = DirectlyFrame(main, label_font, entry_font)
        self.__url_frame = URLFrame(main, label_font, entry_font)

    def entry_val(self):
        return CreateYouTube(self.__url_frame, self.__dir_frame)
