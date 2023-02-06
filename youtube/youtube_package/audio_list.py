class AudioList():

    def __init__(self, list):
        self.list = self.list_arrange(list)
        self.display_list = self.set_display_list()

    def list_arrange(self, list):
        audio_list = [
            element for element in list if "audio" in element["mimeType"]
        ]
        audio_list.sort(key=lambda x: x["bitrate"], reverse=True)
        return audio_list

    def set_display_list(self):
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

    def get_display_list(self):
        return self.display_list
