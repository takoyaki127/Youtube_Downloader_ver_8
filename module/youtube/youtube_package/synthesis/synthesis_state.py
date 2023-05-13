import os
from moviepy.video.io.VideoFileClip import VideoFileClip


class SynthesisState():
    def __init__(self, video_bitrate, audio_bitrate, audio_sampling_rate):
        self.__video_bitrate = video_bitrate
        self.__audio_bitrate = audio_bitrate
        self.__audio_sampling_rate = audio_sampling_rate

    def execute(self, video: VideoFileClip, output, ffmpeg_params=None):
        try:
            video.write_videofile(
                output,
                bitrate=self.__video_bitrate,
                audio_fps=self.__audio_sampling_rate,
                audio_bitrate=self.__audio_bitrate,
                ffmpeg_params=ffmpeg_params,
                threads=self.__core_count()
            )
        except Exception as e:
            print(e)
            self.execute(video, output)

    def __core_count(self):
        return os.cpu_count()
