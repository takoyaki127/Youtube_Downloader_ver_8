from youtube_package.root_list import RootList


class AudioList(RootList):

    def __init__(self, list):
        super().__init__(list, "audio")

    def create_display_list(self):
        list = [
            "{:>4}{:>8}kbps{:>8}khz     {}".format(
                element['itag'],
                int(element["averageBitrate"]/1000) if "averageBitrate" in element.keys(
                ) else int(element["bitrate"]/1000),
                (element["audioSampleRate"][:-3]),
                element['mimeType']
            )for element in self.list
        ]
        return list
