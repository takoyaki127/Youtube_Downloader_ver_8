
class ExplorerButton():
    def __init__(self, btn) -> None:
        self.__btn = btn

    def set_command(self, command):
        self.__btn["command"] = command