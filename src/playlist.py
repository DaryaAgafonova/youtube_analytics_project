from googleapiclient.discovery import build
import os
from datetime import datetime
import datetime
import isodate


class PlayList():

    """ класс PlayList, который инициализируется id плейлиста """

    def __init__(self, playlist_id):

        """ Инициализация атрибутов """

        self.playlists = self.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails, snippet', maxResults=50,).execute()

        self.playlist_id = playlist_id
        self.title = str(self.playlists['items'][0]['snippet']['title'])
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"


    @classmethod
    def get_service(cls):

        """ Возвращает объект для работы с YouTube API """

        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))


    @property
    def total_duration(self):

        """ возвращает объект класса datetime.timedelta с суммарной длительность плейлиста """

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlists['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',id=','.join(video_ids)).execute()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            #(h, m, s) = duration.split(":")
            #return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            #all_time = datetime.timedelta()
            #for i in duration:
            #    (h, m, s) = i.split(":")
            #    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            #    all_time += d
            #    print(str(all_time))


    def __str__(self):

        """ """

        pass



    def show_best_video(self):

        """ возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков) """

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlists['items']]