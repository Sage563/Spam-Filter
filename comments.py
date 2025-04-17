import json
from pytube import YouTube
from googleapiclient.discovery import build
import os
class Comment:
    def __init__(self ,video , comments):
        self.comments = comments
        self.video = video
        self.id_and_video =f"https://www.youtube.com/watch?v={self.video}"

    def get_video_info(self , selfurl):
        """Get video details using Pytube"""
        yt = YouTube(selfurl)
        print (selfurl)
        return yt

    def get_comments(self , api_key, max_comments):
        """Get comments using YouTube API"""
        service = build('youtube', 'v3', developerKey=api_key)
        comments = []
        next_page_token = None
        
        while int(len(comments)) < int(max_comments):
            results = service.commentThreads().list(
                part='snippet',
                videoId=self.video,
                maxResults=min(100, max_comments - len(comments)),
                pageToken=next_page_token
            ).execute()
            
            for item in results['items']:
                comments.append({
                    'text': item['snippet']['topLevelComment']['snippet']['textDisplay']
                })
                
            next_page_token = results.get('nextPageToken')
            if not next_page_token: break
        
        return comments
    
    # Configuration
    def run(self):
        API_KEY = f"{open('key.txt').read().strip()}"
        VIDEO_URL = f"https://www.youtube.com/watch?v={self.video}"

        
        video_data = self.get_comments(API_KEY ,self.comments)
        
        # Save to JSON
        with open('video_data.json','w') as f:
            f.write(json.dumps(video_data, indent=4))
            f.close()

