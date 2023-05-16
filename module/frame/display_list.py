from tkinter import Listbox
import tkinter as tk

class DisplayList():
    def __init__(self, video:Listbox, audio:Listbox) -> None:
        self.__video = video
        self.__audio = audio

    def set_video(self, list_):
        self.__video.delete(0, tk.END)        
        for e in list_:
            self.__video.insert(tk.END, e)

    def set_audio(self, list_):
        self.__audio.delete(0, tk.END)
        for e in list_:
            self.__audio.insert(tk.END, e)
