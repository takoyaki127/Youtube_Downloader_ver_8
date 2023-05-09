import tkinter as tk
from threading import Thread

# from module.gui import Application

from module.frame.frame1 import Frame1
from module.frame.frame2 import Frame2
from module.frame.frame3 import Frame3
from module.frame.frame4 import Frame4


class Frames():
    def __init__(self, root) -> None:
        self.frame1 = Frame1(root)
        self.frame2 = Frame2(root)
        self.frame3 = Frame3(root)
        self.frame4 = Frame4(root)

        self.__set_command(root)
        self.frame1.tkraise()

    def __set_command(self, root):
        self.frame1.btm.set_command(self.__display_frame2)
        self.frame2.btm.set_command(self.execute_download, self.restart)
        self.frame4.btm.set_command(root.destroy, self.restart)

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

    def restart(self):
        self.frame1.tkraise()
        self.frame1.url_entry.delete(0, tk.END)

    def __create_youtube(self):
        self.youtube = self.frame1.create_object()
        lists = self.youtube.get_display_lists()
        self.frame2.setList(lists[0], lists[1])

    def execute_download(self):
        if self.frame2.canDownload():
            p = self.frame2.create_process(self.youtube)
            p.start()
            self.__display_frame3()
            Thread(target=self.wait, args=(p,)).start()

    def wait(self, p):
        p.join()
        self.__display_frame4()
