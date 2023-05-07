class Audio():
    file_name = "audio.m4a"

    def __init__(self, audio_info):
        self.itag = audio_info["itag"]
        self.bitrate = self.set_bitrate(audio_info)

    def set_bitrate(self, audio_info):
        key1: str = "averageBitrate"
        key2: str = "bitrate"

        if key1 in audio_info.keys():
            key = key1
        else:
            key = key2

        bitrate = audio_info[key]
        return f"{bitrate/1000}k"

    def get_itag(self):
        return self.itag

    def get_bitrate(self):
        return self.bitrate
