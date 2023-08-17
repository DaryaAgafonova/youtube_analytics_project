from googleapiclient.discovery import build
import os


class Video():

    """ Класс видео """

    def __init__(self, video_id):

        """ Инициализация реальными данными атрибутов """

        self.dict_of_video = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()

        self.video_id = video_id
        self.video_title = str(self.dict_of_video['items'][0]['snippet']['title'])
        self.video_url = f"https://youtu.be/gaoc9MPZ4bw/{self.video_id}"
        self.count_views = int(self.dict_of_video['items'][0]['statistics']['viewCount'])
        self.count_likes = int(self.dict_of_video['items'][0]['statistics']['likeCount'])


    @classmethod
    def get_service(cls):

        """ Возвращает объект для работы с YouTube API """

        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))


    def __str__(self):

        """ Метод, который выводит название видео """

        return self.video_title


class PLVideo(Video):

    """ класс для видео, который инициализируется 'id видео' и 'id плейлиста """

    def __init__(self, video_id, playlist_id):

        """ Инициализация реальными данными атрибутов  """

        self.dict_of_video = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()

        self.video_id = video_id
        self.video_title = str(self.dict_of_video['items'][0]['snippet']['title'])
        self.video_url = f"https://youtu.be/gaoc9MPZ4bw/{self.video_id}"
        self.count_views = int(self.dict_of_video['items'][0]['statistics']['viewCount'])
        self.count_likes = int(self.dict_of_video['items'][0]['statistics']['likeCount'])
        self.playlist_id = playlist_id