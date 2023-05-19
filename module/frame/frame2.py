from module.frame.base.BaseFrame import Frame, BottomFrame, MainFrame
from module.frame.module.video_frame import VideoFrame
from module.frame.module.audio_frame import AudioFrame

class Frame2(Frame):
    def __init__(self, root=None, bg=None):
        super().__init__(root, bg)
        self.__create_widget()

    def __create_widget(self):
        self.btm = BottomFrame(self, '実行', '戻る')
        main = MainFrame(self, padx=20)

        label_font = ('meiryo', 10)
        list_font = ('meiryo', 8)

        self.__video_frame = VideoFrame(main, label_font, list_font)
        self.__audio_frame = AudioFrame(main, label_font, list_font)

        self.__index = self.__video_frame.index(self.__audio_frame)

    def execute_process(self):
        return self.__index.execute_process()
    
    def display_list(self):
        return self.__video_frame.display_list(self.__audio_frame)
