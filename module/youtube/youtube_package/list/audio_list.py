from module.youtube.youtube_package.list.media_list import MediaList
from module.youtube.youtube_package.media.audio import Audio
from module.frame.module.display_list import DisplayList
from module.youtube.youtube_package.list.create_audio_list import CreateAudioList

class AudioList(MediaList):

    def __init__(self, list, download):
        super().__init__(list, "audio", download)

    def create_display_list(self):
        return CreateAudioList.create(self.list)

    def get_element(self, index):
        return Audio(self.list[index], self.download)

    def set(self, display:DisplayList):
        display.set_audio(self.display_list)
