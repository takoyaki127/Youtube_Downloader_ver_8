from module.youtube.youtube_package.list.media_list import MediaList
from module.youtube.youtube_package.media.audio import Audio

class AudioList(MediaList):

    def __init__(self, list, download):
        super().__init__(list, "audio", download)

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
            format_str: str = "{:>4}{:>8}kbps{:>8}khz{:^20}{:<40}"

            # bitrateは"averageBitrate"がない場合があるので判別している
            itag = audio_info["itag"]
            bitrate = bitrate_discrimination(audio_info)
            audio_samplerate = audio_info["audioSampleRate"][:-3]
            mimetype = audio_info["mimeType"]

            return format_str.format(
                itag,
                bitrate,
                audio_samplerate,
                AudioList.__mimetype_arrange(mimetype,0),
                AudioList.__mimetype_arrange(mimetype,1)
            )
        
    

        display_list = [
            audio_display_list_format(audio_info)for audio_info in self.list
        ]
        return display_list
    
    @staticmethod
    def __mimetype_arrange(mimetype:str, n):
        return mimetype.split(';')[n]

    def get_audio(self, index):
        return Audio(self.list[index], self.download)
    
    def set_list(self,frame):
        frame.set_audio_list(self.display_list)
