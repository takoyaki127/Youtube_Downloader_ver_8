from youtube_package.audio_list import AudioList


class Audio():
    file_name = "audio.m4a"

    def __init__(self, audio: AudioList, index):
        self.index = index
        self.itag = audio.list[self.index]["itag"]
        self.bitrate = self.set_bitrate(audio.list)

    def set_bitrate(self, audio_list):
        element = audio_list[self.index]
        key1: str = "averageBitrate"
        key2: str = "bitrate"

        if key1 in element.keys():
            key = key1
        else:
            key = key2

        bitrate = element[key]
        return f"{bitrate/1000}k"

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
