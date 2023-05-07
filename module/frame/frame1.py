import tkinter as tk
from tkinter import filedialog

from module.youtube.youtube_package.directory import read_dir
from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.youtube.youtube_object import YoutubeObject


class Frame1(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        default_dir = read_dir()
        self.create_widget(default_dir)

    def create_widget(self, default_dir):
        self.btm = BottomFrame(self, '次へ')
        main = MainFrame(self, padx=20)

        label_font = ('meiryo', 10)
        entry_font = ('meiryo', 13)

        # ディレクトリ指定のフレーム
        dir_frame = tk.Frame(main)
        dir_frame.pack(expand=1, fill='x')

        self.img = tk.PhotoImage(file="./img/folder_icon.png")
        dir_label = tk.Label(dir_frame, text='ディレクトリを指定', font=label_font)
        dir_label.pack(anchor='nw')
        dir_btn = tk.Button(
            dir_frame,
            image=self.img,
            command=self.dirdialog_clicked
        )
        dir_btn.pack(side='right', ipadx=10)

        self.dir_str = tk.StringVar(value=default_dir)
        self.dir_entry = tk.Entry(
            dir_frame,
            textvariable=self.dir_str,
            font=entry_font
        )
        self.dir_entry.pack(side='right', expand=1, fill='x')

        # URL指定のフレーム
        url_frame = tk.Frame(main)
        url_frame.pack(expand=1, fill='x')

        url_label = tk.Label(url_frame, text='URLを入力', font=label_font)
        url_label.pack(anchor='nw')

        self.paste_img = tk.PhotoImage(file="./img/paste_icon.png")
        url_btn = tk.Button(
            url_frame,
            text='ペースト',
            image=self.paste_img,
            command=self.paste_url
        )
        url_btn.pack(side='right', ipadx=10)

        self.url_str = tk.StringVar()
        self.url_entry = tk.Entry(
            url_frame,
            textvariable=self.url_str,
            font=entry_font
        )
        self.url_entry.pack(side='right', expand=1, fill='x')

    # ファイルダイアログを表示、指定したフォルダをセット
    def dirdialog_clicked(self):
        iDirPath = filedialog.askdirectory()
        if iDirPath != "":
            self.dir_str.set(iDirPath)

    # クリップボードの文字をセット
    def paste_url(self):
        try:
            self.url_str.set(self.clipboard_get())
        except Exception:
            print("ペーストできません")

    def get_url(self):
        return self.url_str.get()

    def get_dir(self):
        return self.dir_str.get()

    def create_object(self):
        url = self.get_url()
        dir = self.get_dir()
        return YoutubeObject(url, dir)
