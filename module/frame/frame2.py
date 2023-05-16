import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.frame.display_list import DisplayList
from module.frame.index_label import IndexLabel
from module.frame.index import Index


class Frame2(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.__create_widget()

    def __create_widget(self):
        self.btm = BottomFrame(self, '実行', '戻る')
        main = MainFrame(self, padx=20)

        label_font = ('meiryo', 10)
        list_font = ('meiryo', 8)

        # ビデオフレーム
        video_frame = tk.Frame(main)
        video_frame.pack(expand=1, fill='both')

        self.video_label = tk.Label(video_frame, text='動画リスト', font=label_font)
        self.video_label.pack(anchor='nw')

        self.video_list = tk.Listbox(
            video_frame,
            font=list_font,
            activestyle='none'
        )
        self.video_list.pack(fill='both')

        # オーディオフレーム
        audio_frame = tk.Frame(main)
        audio_frame.pack(expand=1, fill='both')

        self.audio_label = tk.Label(audio_frame, text='音声リスト', font=label_font)
        self.audio_label.pack(anchor='nw')

        self.audio_list = tk.Listbox(
            audio_frame,
            font=list_font,
            activestyle='none'
        )
        self.audio_list.pack(fill='both')

        label = IndexLabel(self.video_label, self.audio_label)
        self.index = Index(self.video_list, self.audio_list, label)

    def execute_process(self):
        return self.index.execute_process()
    
    def display_list(self):
        return DisplayList(self.video_list, self.audio_list)
