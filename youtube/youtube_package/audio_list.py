from youtube.youtube_package.root_list import RootList
from youtube.youtube_package.audio import Audio


class AudioList(RootList):

    def __init__(self, list):
        super().__init__(list, "audio")

    def create_display_list(self):
        def bitrate_discrimination(audio_info):
            avg_bitrate_key: str = "averageBitrate"
            bitrate_key: str = "bitrate"

            if avg_bitrate_key in audio_info.keys():
                key: str = avg_bitrate_key
            else:
                key: str = bitrate_key

            return int(audio_info[key]/1000)

        def audio_display_list_format(audio_info):
            format_str: str = "{:>4}{:>8}kbps{:>8}khz     {}"

            # bitrateは"averageBitrate"がない場合があるので判別している
            itag = audio_info["itag"]
            bitrate = bitrate_discrimination(audio_info)
            audio_samplerate = audio_info["audioSampleRate"][:-3]
            mimetype = audio_info["mimeType"]

            return format_str.format(
                itag,
                bitrate,
                audio_samplerate,
                mimetype
            )

        display_list = [
            audio_display_list_format(audio_info)for audio_info in self.list
        ]
        return display_list

    def get_audio_with_index(self, index):
        return Audio(self.list[index])
