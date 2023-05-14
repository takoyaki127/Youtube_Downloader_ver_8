from module.youtube.youtube_object import YoutubeObject


class Index():
    def __init__(self, video_index, audio_index) -> None:
        self.__video_index = video_index
        self.__audio_index = audio_index

    def create_process(self, youtube: YoutubeObject):
        return youtube.prepare_execute_process(
            self.__video_index,
            self.__audio_index
        )
