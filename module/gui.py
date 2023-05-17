import tkinter as tk

from module.frame.frames import Frames


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YT_downloader")
        self.geometry("600x520")

        self.__frames = Frames(self)
