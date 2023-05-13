import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.youtube.youtube_object import YoutubeObject


class Frame2(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.video_index = -1
        self.audio_index = -1
        self.create_widget()

    def set_youtube(self, youtube: YoutubeObject):
        self.youtube = youtube

    def create_widget(self):
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

        self.video_list.bind('<<ListboxSelect>>', self.set_video_index)
        self.audio_list.bind('<<ListboxSelect>>', self.set_audio_index)

    def update_video_label(self):
        self.video_label["text"] = f"動画リスト index= {self.video_index}"

    def update_audio_label(self):
        self.audio_label["text"] = f"音声リスト index= {self.audio_index}"
    
    def set_video_list(self,video_list):
        self.reset_video_list()
        for element in video_list:
            self.video_list.insert(tk.END, element)

    def set_audio_list(self,audio_list):
        self.reset_audio_list()
        for element in audio_list:
            self.audio_list.insert(tk.END, element)

    def reset_video_list(self):
        self.video_list.delete(0, tk.END)

    def reset_audio_list(self):
        self.audio_list.delete(0, tk.END)

    def set_video_index(self, event):
        index = self.video_list.curselection()
        if len(index) == 1:
            self.video_index = index[0]
            self.update_video_label()

    def set_audio_index(self, event):
        index = self.audio_list.curselection()
        if len(index) == 1:
            self.audio_index = index[0]
            self.update_audio_label()

    def create_process(self,youtube:YoutubeObject):
        return youtube.prepare_multiprocessing(
            self.video_index,
            self.audio_index
        )

    def canDownload(self):
        if self.video_index != -1 and self.audio_index != -1:
            return True
        return False


