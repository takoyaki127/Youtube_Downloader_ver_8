from moviepy.video.io.VideoFileClip import VideoFileClip

from module.youtube.youtube_package.synthesis.device import Device
from module.youtube.youtube_package.media.video import Video
from module.youtube.youtube_package.media.audio import Audio


class Synthesis():
    def __init__(self, tmp, output, video_info: Video, audio_info: Audio):
        self.__tmp = tmp
        self.__output = output
        self.__video = self.__create_video_file_clip(video_info, audio_info)
        self.__state = self.__create_state(video_info, audio_info)

    def __create_video_file_clip(self, video_info: Video, audio_info: Audio) -> VideoFileClip:
        video = video_info.file_clip(self.__tmp)
        audio = audio_info.file_clip(self.__tmp)
        return video.set_audio(audio)

    def __create_state(self, video_info: Video, audio_info: Audio):
        return video_info.synthesis_state(audio_info)

    def execute(self, device=Device.GPU):
        ffmpeg_params = self.__set_device(device)
        self.__state.execute(self.__video, self.__output, ffmpeg_params)

    def __set_device(self, device):
        if device == Device.GPU:
            return ['-vcodec', 'h264_nvenc']
        return None
