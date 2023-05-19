import tkinter as tk
from module.frame.module.directory_entry import DirectoryEntry

class DirectlyFrame():
    def __init__(self, root, label_font, entry_font) -> None:
        self.__frame = tk.Frame(root)
        self.__frame.pack(expand=1, fill='x')
        self.__add_label(label_font)
        self.__add_button()
        self.__add_entry(entry_font)

    def __add_label(self, font):
        dir_label = tk.Label(self.__frame, text='ディレクトリを指定', font=font)
        dir_label.pack(anchor='nw')


    def __add_button(self):
        self.__img = tk.PhotoImage(file="./img/folder_icon.png")
        dir_btn = tk.Button(
            self.__frame,
            image=self.__img,
            command=self.__filedialog_click
        )
        dir_btn.pack(side='right', ipadx=10)

    def __add_entry(self, font):
        self.__dir_entry = DirectoryEntry(self.__frame, font)

    def __filedialog_click(self):
        self.__dir_entry.set()

    def get(self):
        return self.__dir_entry.get()