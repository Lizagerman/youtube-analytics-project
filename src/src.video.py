from helper.youtube_api_manual import youtube


class Video:
    def __init__(self,video_id):

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.video_id = video_id
        self.url = 'https://youtu.be/' + video_id


        self.set_attributes_video()

    def __str__(self):
        return f'{self.title}'

    def set_attributes_video(self):
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()

        self.title = video_response['items'][0]['snippet']['title']
        self.viewCount = video_response['items'][0]['statistics']['viewCount']
        self.likeCount = video_response['items'][0]['statistics']['likeCount']
        self.duration = video_response['items'][0]['statistics']['likeCount']
        print(video_response)

    def __str__(self):
        return f'{self.title}'

class PLVideo(Video):
    def __init__(self, video_id, channel_id):
        super().__init__(video_id)
        self.channel_id = channel_id

