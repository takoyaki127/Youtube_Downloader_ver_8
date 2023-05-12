from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

from module.youtube.youtube_package.synthesis.device import Device
from module.youtube.youtube_package.media.video import Video
from module.youtube.youtube_package.media.audio import Audio


class Synthesis():
    def __init__(self, tmp, output):
        self.tmp = tmp
        self.output = output

    def execute(self, video_info: Video, audio_info: Audio, device=Device.GPU):
        ffmpeg_params = self.__set_device(device)

        video = VideoFileClip(self.tmp + "\\" + video_info.file_name)
        audio = AudioFileClip(self.tmp + "\\" + audio_info.file_name)
        video: VideoFileClip = video.set_audio(audio)

        video.write_videofile(
            self.output,
            bitrate=video_info.get_bitrate(),
            audio_bitrate=audio_info.get_bitrate(),
            ffmpeg_params=ffmpeg_params
        )

    def __set_device(self, device):
        if device == Device.GPU:
            return ['-vcodec', 'h264_nvenc']

        return None
