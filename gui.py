import tkinter as tk

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
        self.frame1.btm.set_command(self.create_frame2)

    def create_frame2(self):
        self.frame2 = Frame2(self)
        self.frame2.btm.set_command(self.create_frame3, self.frame1.tkraise)

    def create_frame3(self):
        self.frame3 = Frame3(self)
        self.create_frame4()

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
