import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame


class Frame4(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.create_widget()

    def create_widget(self):
        self.btm = BottomFrame(self, '終了', 'もう一度')
        self.main = MainFrame(self)
        label = tk.Label(self.main, text='完了しました', font=('meiryo', 15))
        label.pack(expand=1)
