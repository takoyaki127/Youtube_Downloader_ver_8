import tkinter as tk
from threading import Thread

from module.frame.frame1 import Frame1
from module.frame.frame2 import Frame2
from module.frame.frame3 import Frame3
from module.frame.frame4 import Frame4


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YT_downloader")
        self.geometry("600x520")
        self.create_frame1()

    def create_frame1(self):
        self.frame1 = Frame1(self)
        self.frame1.btm.set_command(self.display_frame2)

    def display_frame2(self):
        try:
            self.youtube = self.frame1.create_object()
        except Exception as e:
            print("Youtubeオブジェクトの生成に失敗しました。")
        else:
            self.create_frame2()

    def create_frame2(self):
        self.frame2 = Frame2(self)
        self.frame2.btm.set_command(self.display_frame3, self.frame1.tkraise)

    def display_frame3(self):
        if self.frame2.canDownload():
            Thread(target=self.display_frame4).start()
            self.create_frame3()

    def display_frame4(self):
        p = self.frame2.prepare_multiprocessing()
        p.start()
        p.join()
        self.create_frame4()

    def create_frame3(self):
        self.frame3 = Frame3(self)

    def create_frame4(self):
        self.frame4 = Frame4(self)
        self.frame4.btm.set_command(
            self.destroy,
            self.restart
        )

    def restart(self):
        self.frame1.tkraise()
        self.frame1.url_entry.delete(0, tk.END)
        self.frame2.video_index = -1
        self.frame2.audio_index = -1


def main():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
