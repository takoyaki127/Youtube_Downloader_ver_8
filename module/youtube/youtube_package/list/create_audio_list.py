
class CreateAudioList():
    format_str: str = "{:>4}{:>8}kbps{:>8}khz{:^20}{:<40}"

    @staticmethod
    def create(dict_:list[dict]):
        return [
            CreateAudioList.__display_format(audio_info)for audio_info in dict_
        ]

    @staticmethod
    def __display_format(audio_info:dict):
        # bitrateは"averageBitrate"がない場合があるので判別している
        itag = audio_info["itag"]
        bitrate = CreateAudioList.__bitrate_discrimination(audio_info)
        audio_samplerate = audio_info["audioSampleRate"][:-3]
        mimetype = audio_info["mimeType"]

        return CreateAudioList.format_str.format(
            itag,
            bitrate,
            audio_samplerate,
            CreateAudioList.__mimetype_arrange(mimetype,0),
            CreateAudioList.__mimetype_arrange(mimetype,1)
        )

    @staticmethod
    def __bitrate_discrimination(audio_info:dict):
        avg_bitrate_key: str = "averageBitrate"
        bitrate_key: str = "bitrate"

        if avg_bitrate_key in audio_info.keys():
            key: str = avg_bitrate_key
        else:
            key: str = bitrate_key

        return int(audio_info[key]/1000)

    @staticmethod
    def __mimetype_arrange(mimetype:str, n):
        return mimetype.split(';')[n]