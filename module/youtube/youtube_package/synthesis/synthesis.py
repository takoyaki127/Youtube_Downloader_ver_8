import os
from moviepy.video.io.VideoFileClip import VideoFileClip

from module.youtube.youtube_package.synthesis.device import Device
from module.youtube.youtube_package.media.video import Video
from module.youtube.youtube_package.media.audio import Audio


class Synthesis():
    def __init__(self, tmp, output, video_info: Video, audio_info: Audio):
        self.__tmp = tmp
        self.__output = output
        self.__video_info = video_info
        self.__audio_info = audio_info
        self.__video = self.__create_video_file_clip()

    def __create_video_file_clip(self) -> VideoFileClip:
        video = self.__video_info.file_clip(self.__tmp)
        audio = self.__audio_info.file_clip(self.__tmp)
        return video.set_audio(audio)

    def execute(self, device=Device.GPU):
        ffmpeg_params = self.__set_device(device)
        self.__video_info.synthesis_start(
            self, self.__audio_info, ffmpeg_params)

    def write(self, video_bitrate, audio_bitrate, audio_sampling_rate, ffmpeg_params=None):
        try:
            self.__video.write_videofile(
                self.__output,
                bitrate=video_bitrate,
                audio_fps=audio_sampling_rate,
                audio_bitrate=audio_bitrate,
                ffmpeg_params=ffmpeg_params,
                threads=self.__core_count()
            )
        except Exception as e:
            print(e)
            self.write(video_bitrate, audio_bitrate, audio_sampling_rate)

    def __set_device(self, device):
        if device == Device.GPU:
            return ['-vcodec', 'h264_nvenc']
        return None

    def __core_count(self):
        return os.cpu_count()
