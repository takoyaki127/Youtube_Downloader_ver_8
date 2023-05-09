from module.youtube.youtube_package.media.media import Media
# from media import Media

class Audio(Media):
    file_name = "audio.m4a"

    def __init__(self, info: dict):
        super().__init__(info)

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

if __name__ == "__main__":
    dict_ = {"itag": 10, "averageBitrate": 10}
    audio = Audio(dict_)
    print(audio.get_bitrate())
    pass