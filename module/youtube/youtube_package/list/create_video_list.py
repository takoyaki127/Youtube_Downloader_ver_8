
class CreateVideoList():
    format_str: str = "{:>4}{:>12}{:^30}{:<20}"

    @staticmethod
    def create(dict_:dict):
        return [
            CreateVideoList.format_str.format(
                video_info['itag'],
                video_info["qualityLabel"],
                CreateVideoList.__mimetype_arrange(video_info['mimeType'], 0),
                CreateVideoList.__mimetype_arrange(video_info['mimeType'], 1)
            )for video_info in dict_
        ]

    @staticmethod
    def __mimetype_arrange(mimetype: str, n):
        return mimetype.split(';')[n]