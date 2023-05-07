import os


def read_dir():
    filePath = './settings.txt'
    if os.path.isfile(filePath) == True:
        with open(filePath, 'r', encoding='utf-8') as f:
            str = f.read()
            str_list = str.split('=')
            dl_dir = str_list[1]
    else:
        dl_dir = ""
    return dl_dir


def write_dir(set_dir):
    filePath = './settings.txt'
    if set_dir != read_dir():
        try:
            with open(filePath, 'w', encoding='utf-8') as f:
                f.write(f'Download_dir={set_dir}')
        except Exception:
            print("settings.txtの作成に失敗しました。")


class Directory():
    def __init__(self, download, title):
        self.download = download
        self.tmp = self.download + r"\tmp"
        self.output = self.download + "\\" + title + ".mp4"

    def get_tmp(self) -> str:
        return self.tmp

    def getOutput(self):
        return self.output

    def create_tmp_dir(self):
        if not os.path.isdir(self.tmp):
            os.makedirs(self.tmp)

    def write_to_text_file(self):
        write_dir(self.download)
