import tkinter as tk

from module.frame.frame1 import Frame1
from module.frame.frame2 import Frame2
from module.frame.frame3 import Frame3
from module.frame.frame4 import Frame4


class Frames():
    def __init__(self, root) -> None:
        # frameを生成
        self.frame1 = Frame1(root)
        self.frame2 = Frame2(root)
        self.frame3 = Frame3(root)
        self.frame4 = Frame4(root)

        self.create_youtube = self.frame1.entry_val()

        # buttonにメソッドをセット
        self.__set_command(root)
        self.frame1.tkraise()

    def __set_command(self, root):
        self.frame1.btm.set_command(self.__display_frame2)
        self.frame2.btm.set_command(self.__execute_download, self.__restart)
        self.frame4.btm.set_command(root.destroy, self.__restart)

    def __display_frame2(self):
        try:
            self.__create_youtube()
            self.frame2.tkraise()
        except Exception as e:
            print(e)

    def __display_frame3(self):
        self.frame3.tkraise()

    def __display_frame4(self):
        self.frame4.tkraise()

    def __restart(self):
        self.frame1.tkraise()
        self.frame1.url_entry.delete(0, tk.END)

    # youtubeオブジェクトを作成して表示用リストに追加
    def __create_youtube(self):
        self.youtube = self.create_youtube.create()
        display_list = self.frame2.display_list()
        self.youtube.display(display_list)

    # マルチプロセスでダウンロードを実行
    def __execute_download(self):
        if process := self.frame2.execute_process():
            process.start(self.youtube, self.__display_frame4)
            self.__display_frame3()
