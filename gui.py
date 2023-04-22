import tkinter as tk
from threading import Thread

from frame.frame1 import Frame1
from frame.frame2 import Frame2
from frame.frame3 import Frame3
from frame.frame4 import Frame4


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
            self.create_video_object()
            self.create_frame2()
        except Exception as e:
            print("Youtubeオブジェクトの生成に失敗しました。")

    def create_video_object(self):
        self.youtube = self.frame1.create_object()

    def create_frame2(self):
        self.frame2 = Frame2(self)
        self.frame2.btm.set_command(self.display_frame3, self.frame1.tkraise)
        self.frame2.setList_with_object(self.youtube)

    def display_frame3(self):
        Thread(target=self.execute, args=(self.youtube,)).start()
        self.create_frame3()

    def execute(self, youtube):
        self.frame2.download(youtube)
        self.frame2.syntheis(youtube)
        self.frame2.remove(youtube)
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
