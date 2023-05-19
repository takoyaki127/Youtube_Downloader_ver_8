import tkinter as tk
from module.youtube.youtube_package.settings import Settings
from tkinter import filedialog

class DirectoryEntry():
    def __init__(self, frame, font) -> None:
        self.__string_var = self.__create_string_var()
        self.__entry = self.__create_entry(frame, self.__string_var, font)
        self.__entry.pack(side='right', expand=1, fill='x')

    def __create_entry(self, frame, str_, font):
        return tk.Entry(
            frame,
            textvariable=str_,
            font=font
        )
    
    def __create_string_var(self):
        return tk.StringVar(value=Settings.read_dir())
    
    def set(self):
        if path:=self.__filedialog():
            path = path.replace("/", "\\")
            self.__string_var.set(path)

    def get(self):
        return self.__string_var.get()
    
    def __filedialog(self):
        iDirPath = filedialog.askdirectory()
        if iDirPath:
            return iDirPath
        return None