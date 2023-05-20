import tkinter as tk


class ExplorerButton():
    def __init__(self, root) -> None:
        self.__btn = tk.Button(root, text="フォルダーを開く", font=("meiryo",10))
        self.__btn.pack(padx=30,pady=30,ipadx=5)

    def set_command(self, command):
        self.__btn["command"] = command