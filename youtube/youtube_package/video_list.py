class VideoList():

    def __init__(self, list):
        self.list = self.list_arrange(list)
        self.display_list = self.set_display_list()

    def list_arrange(self, list):
        video_list = [
            element for element in list if "video" in element["mimeType"]
        ]
        video_list.sort(key=lambda x: x["bitrate"], reverse=True)
        return video_list

    def set_display_list(self):
        result = [
            "{:>4}{:>12}     {:}".format(
                element['itag'],
                element["qualityLabel"],
                element['mimeType']
            )for element in self.list
        ]
        return result

    def get_display_list(self):
        return self.display_list
