import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id
        self.dict_of_channel = self.get_service().channels().list(id=self.channel_id,
                                                                  part='snippet,statistics').execute()
        self.title = self.dict_of_channel.get("items")[0].get("snippet").get("title")
        self.description = self.dict_of_channel.get("items")[0].get("snippet").get("description")
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.count_subscribers = int(self.dict_of_channel.get("items")[0].get("statistics").get("subscriberCount"))
        self.video_count = int(self.dict_of_channel.get("items")[0].get("statistics").get("videoCount"))
        self.all_count_views = int(self.dict_of_channel.get("items")[0].get("statistics").get("viewCount"))

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API """

        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))

    @staticmethod
    def __printj(dict_of_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами. """

        print(json.dumps(dict_of_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """ Выводит в консоль информацию о канале """

        self.__printj(self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute())

    def to_json(self, filename):
        """ Метод, сохраняющий в файл значения атрибутов экземпляра Channel """

        data = {"title": self.title,
                "channel_id": self.channel_id,
                "description": self.description,
                "url": self.url,
                "count_subscribers": self.count_subscribers,
                "video_count": self.video_count,
                "all_count_views": self.all_count_views}

        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)


    def __str__(self):

        """ Метод, возвращающий название и ссылку на канал """

        return f"{self.title} ({self.url})"


    def __add__(self, other):

        """ Метод для сложения 2х каналов """

        return self.count_subscribers + other.count_subscribers


    def __sub__(self, other):

        """ Метод для вычитания 2х каналов """

        return self.count_subscribers - other.count_subscribers


    def __lt__(self, other):

        """ Метод для сравниения 2х каналов между собой """

        return self.count_subscribers < other.count_subscribers


    def __le__(self, other):

        """ Метод для сравниения 2х каналов между собой """

        return self.count_subscribers <= other.count_subscribers


    def __gt__(self, other):

        """ Метод для сравниения 2х каналов между собой """

        return self.count_subscribers > other.count_subscribers


    def __ge__(self, other):

        """ Метод для сравниения 2х каналов между собой """

        return self.count_subscribers >= other.count_subscribers