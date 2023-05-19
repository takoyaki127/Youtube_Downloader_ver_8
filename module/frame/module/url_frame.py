import tkinter as tk

class URLFrame():
    def __init__(self, root:tk.Frame, label_font, entry_font) -> None:
        self.__root = root
        self.__url_frame = tk.Frame(root)
        self.__url_frame.pack(expand=1, fill='x')
        self.add_label(label_font)
        self.add_button()
        self.add_entry(entry_font)

    def add_label(self, font):
        url_label = tk.Label(self.__url_frame, text='URLを入力', font=font)
        url_label.pack(anchor='nw')

    def add_button(self):
        self.__img = tk.PhotoImage(file="./img/paste_icon.png")
        url_btn = tk.Button(
            self.__url_frame,
            text='ペースト',
            image=self.__img,
            command=self.paste
        )
        url_btn.pack(side='right', ipadx=10)

    def add_entry(self, font):
        self.__string_var = tk.StringVar()
        entry = tk.Entry(
            self.__url_frame,
            textvariable=self.__string_var,
            font=font
        )
        entry.pack(side='right', expand=1, fill='x')

    def paste(self):
        try:
            self.__string_var.set(self.__root.clipboard_get())
        except Exception:
            print("ペーストできません")

    def get(self):
        return self.__string_var.get()
