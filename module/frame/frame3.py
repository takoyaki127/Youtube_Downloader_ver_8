import tkinter as tk
from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame


class Frame3(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.create_widget()

    def create_widget(self):
        self.main = MainFrame(self)
        label = tk.Label(
            self.main, text='ダウンロード中・・・', font=('meiryo', 15))
        label.pack(expand=1)
