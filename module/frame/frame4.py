import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.frame.explorer_btn import ExplorerButton


class Frame4(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.create_widget()

    def create_widget(self):
        self.btm = BottomFrame(self, '終了', 'もう一度')
        self.main = MainFrame(self)
        label = tk.Label(self.main, text='完了しました', font=('meiryo', 15))
        label.pack(expand=1)

        self.exp_btn = tk.Button(self.main, text="フォルダーを開く", font=("meiryo",10))
        self.exp_btn.pack(padx=30,pady=30,ipadx=5)

    def explorer_btn(self):
        return ExplorerButton(self.exp_btn)

