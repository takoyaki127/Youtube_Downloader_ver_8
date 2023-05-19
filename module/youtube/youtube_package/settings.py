import os

class Settings():

    @staticmethod
    def read_dir() -> str:
        filePath = r'.\settings.txt'
        if os.path.isfile(filePath) == True:
            with open(filePath, 'r', encoding='utf-8') as f:
                str_ = f.read()
                str_list = str_.split('=')
                dl_dir = str_list[1]
                return dl_dir
        return ""

    @staticmethod
    def write_dir(set_dir) -> None:
        filePath = r'.\settings.txt'
        if set_dir != Settings.read_dir():
            try:
                with open(filePath, 'w', encoding='utf-8') as f:
                    f.write(f'Download_dir={set_dir}')
            except Exception:
                print("settings.txtの作成に失敗しました。")
