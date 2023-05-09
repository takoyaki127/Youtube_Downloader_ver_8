
class Title():

    @staticmethod
    def escape(title:str):
        escaped_title = title.translate(str.maketrans({
            "\\": "￥", "/": "／", ":": "：",
            "*": "＊", "?": "？", "\"": "”",
            "<": "＜", ">": "＞", "|": "｜"
        }))
        return escaped_title