import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg=bg)
        self.place(relheight=1, relwidth=1)


class MainFrame(tk.Frame):
    def __init__(self, root=None, bg=None, padx=None):
        super().__init__(root, bg=bg, padx=padx)
        self.pack(expand=1, fill='both')


class BottomFrame(tk.Frame):
    def __init__(self, frame, text1=None, text2=None, bg='#aaa'):
        super().__init__(frame, bg=bg)
        self.pack(side="bottom", fill="x")
        self.create_btn(text1, text2)

    def create_btn(self, text1, text2):
        if text1 != None:
            self.btn = tk.Button(self, text=text1, font=('meiryo', 8))
            self.btn.pack(side="right", ipadx=18, padx=(0, 15), pady=8)

        if text2 != None:
            self.btn2 = tk.Button(self, text=text2, font=('meiryo', 8))
            self.btn2.pack(side="right", ipadx=18, padx=(0, 24))

    def set_command(self, func1=None, func2=None):
        if func1 != None:
            self.btn['command'] = func1
        if func2 != None:
            self.btn2['command'] = func2
