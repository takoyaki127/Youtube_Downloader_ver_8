from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

from module.youtube.youtube_package.directory import Directory
from module.youtube.youtube_package.video import Video
from module.youtube.youtube_package.audio import Audio


class Synthesis():
    def __init__(self, video: Video, audio: Audio, dir: Directory):
        self.video_bitrate = video.get_bitrate()
        self.audio_bitrate = audio.get_bitrate()
        self.output = dir.getOutput()
        tmp = dir.get_tmp()
        self.video_path = tmp + "\\" + video.file_name
        self.audio_path = tmp + "\\" + audio.file_name

    def synthesis(self, ffmpeg_params=['-vcodec', 'h264_nvenc']):

        video = VideoFileClip(self.video_path)
        audio = AudioFileClip(self.audio_path)
        video: VideoFileClip = video.set_audio(audio)

        video.write_videofile(
            self.output,
            bitrate=self.video_bitrate,
            audio_bitrate=self.audio_bitrate,
            ffmpeg_params=ffmpeg_params
        )
