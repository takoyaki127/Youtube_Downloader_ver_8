import tkinter as tk

from frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from youtube.youtube_object import YoutubeObject


class Frame2(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.video_index = -1
        self.audio_index = -1
        self.create_widget()

    def create_widget(self):
        self.btm = BottomFrame(self, '実行', '戻る')
        main = MainFrame(self, padx=20)

        label_font = ('meiryo', 10)
        list_font = ('meiryo', 8)

        # ビデオフレーム
        video_frame = tk.Frame(main)
        video_frame.pack(expand=1, fill='both')

        video_label = tk.Label(video_frame, text='動画リスト', font=label_font)
        video_label.pack(anchor='nw')

        self.video_list = tk.Listbox(
            video_frame,
            font=list_font,
            activestyle='none'
        )
        self.video_list.pack(fill='both')

        # オーディオフレーム
        audio_frame = tk.Frame(main)
        audio_frame.pack(expand=1, fill='both')

        audio_label = tk.Label(audio_frame, text='音声リスト', font=label_font)
        audio_label.pack(anchor='nw')

        self.audio_list = tk.Listbox(
            audio_frame,
            font=list_font,
            activestyle='none'
        )
        self.audio_list.pack(fill='both')

        self.video_list.bind('<<ListboxSelect>>', self.set_video_index)
        self.audio_list.bind('<<ListboxSelect>>', self.set_audio_index)

    def setList(self, videoList, audioList):
        self.resetList()
        for element in videoList:
            self.video_list.insert(tk.END, element)
        for element in audioList:
            self.audio_list.insert(tk.END, element)

    def resetList(self):
        self.video_list.delete(0, tk.END)
        self.audio_list.delete(0, tk.END)

    def set_video_index(self, event):
        index = self.video_list.curselection()
        if len(index) == 1:
            self.video_index = index[0]

    def set_audio_index(self, event):
        index = self.audio_list.curselection()
        if len(index) == 1:
            self.audio_index = index[0]

    def get_index(self):
        return self.video_index, self.audio_index

    def setList_with_object(self, youtube: YoutubeObject):
        video_list = youtube.video_list.get_display_list()
        audio_list = youtube.audio_list.get_display_list()
        self.setList(video_list, audio_list)
