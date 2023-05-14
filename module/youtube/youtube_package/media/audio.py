from module.youtube.youtube_package.media.media import Media
from module.youtube.youtube_package.download.download import Download
from moviepy.audio.io.AudioFileClip import AudioFileClip

from module.youtube.youtube_package.synthesis.synthesis_state import SynthesisState


class Audio(Media):
    file_name = "audio.m4a"

    def __init__(self, info: dict, download:Download):
        super().__init__(info, download, Audio.file_name)
        self.__sampling_rate=self.__get_sampling_rate(info)

    def set_bitrate(self, info):
        key1: str = "averageBitrate"
        key2: str = "bitrate"

        if key1 in info.keys():
            key = key1
        else:
            key = key2
        try:
            bitrate = info[key]
        except Exception as e:
            print("bitrateを取得できませんでした。")
            return "6k"

        return f"{bitrate/1000}k"
    
    def __get_sampling_rate(self,info):
        try:
            return int(info['audioSampleRate'])
        except:
            return 44100
    
    def file_clip(self, tmp):
        return AudioFileClip(tmp + "\\" + self.filename)
    
    def synthesis_state(self, video_bitrate):
        return SynthesisState(video_bitrate, self.bitrate, self.__sampling_rate)
