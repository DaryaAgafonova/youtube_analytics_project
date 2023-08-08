import json
import os
from googleapiclient.discovery import build


# AIzaSyAdBFVvXjxXVv9Hy6iQeE3sra_O55m9NZ8
yt_api_key: str = os.getenv("YT_API_KEY")

youtube = build("youtube", "v3", developerKey=yt_api_key)


class Channel:

    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, title: str, description: str, url: str, count_subscribers: int, video_count: int, all_count_views: int) -> None:

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.title = None
        self.description = None
        self.url = None
        self.count_subscribers= None
        self.video_count = None
        self.all_count_views = None


    def print_info(self) -> None:

        """Выводит в консоль информацию о канале."""

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        print(json.dumps(channel, indent=2, ensure_ascii=False))


    @classmethod
    def get_service(cls):

        """ Возвращает объект для работы с YouTube API """

        return youtube


    def to_json(self):

        """ Метод, сохраняющий в файл значения атрибутов экземпляра Channel """

        data = {
                "id": self.channel_id,
                "title": self.title,
                "description": self.description,
                "url": self.url,
                "count_subscribers": self.count_subscribers,
                "video_count": self.video_count,
                "all_count_views": self.all_count_views
        }

        with open("", "w") as json_file:

            json.dump(data, json_file, indent=2, ensure_ascii=False)