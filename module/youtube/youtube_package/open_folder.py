import subprocess as sp

class Explorer():
    def __init__(self, path) -> None:
        self.__path = self.__path_fix(path)

    def open(self):
        sp.Popen(['explorer', self.__path], shell=True)

    @staticmethod
    def __path_fix(path:str):
        return path.replace('/','\\')
