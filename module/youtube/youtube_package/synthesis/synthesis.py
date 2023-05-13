from moviepy.video.io.VideoFileClip import VideoFileClip

from module.youtube.youtube_package.synthesis.device import Device
from module.youtube.youtube_package.media.video import Video
from module.youtube.youtube_package.media.audio import Audio


class Synthesis():
    def __init__(self, tmp, output):
        self.__tmp = tmp
        self.__output = output

    def execute(self, video_info: Video, audio_info: Audio, device=Device.GPU):
        ffmpeg_params = self.__set_device(device)

        video = video_info.file_clip(self.__tmp)
        audio = audio_info.file_clip(self.__tmp)
        video:VideoFileClip = video.set_audio(audio)

        video.write_videofile(
            self.__output,
            bitrate=video_info.get_bitrate(),
            audio_bitrate=audio_info.get_bitrate(),
            ffmpeg_params=ffmpeg_params
        )

    def __set_device(self, device):
        # Todo: GPUがないとき、Noneを返す
        if device == Device.GPU:
            return ['-vcodec', 'h264_nvenc']

        return None
