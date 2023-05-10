import os

class Settings():

    @staticmethod
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

    @staticmethod
    def write_dir(set_dir):
        filePath = './settings.txt'
        if set_dir != Settings.read_dir():
            try:
                with open(filePath, 'w', encoding='utf-8') as f:
                    f.write(f'Download_dir={set_dir}')
            except Exception:
                print("settings.txtの作成に失敗しました。")
