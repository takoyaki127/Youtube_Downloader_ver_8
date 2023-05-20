import tkinter as tk

from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.frame.module.explorer_btn import ExplorerButton
from module.youtube.youtube_package.open_folder import Explorer


class Frame4(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.__create_widget()

    def __create_widget(self):
        self.btm = BottomFrame(self, '終了', 'もう一度')
        self.main = MainFrame(self)
        label = tk.Label(self.main, text='完了しました', font=('meiryo', 15))
        label.pack(expand=1)
        self.exp_btn = ExplorerButton(self.main)

    def explorer_btn(self, explorer:Explorer):
        self.exp_btn.set_command(explorer.open)

