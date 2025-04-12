import praw
import redis
import json
import os
import time
from dotenv import load_dotenv
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

r = redis.Redis(host='localhost', port=6379, db=0)

def stream_comments(subreddit_name="technology"):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"Streaming comments from r/{subreddit_name}...")
    
    for comment in subreddit.stream.comments(skip_existing=True):
        comment_data = {
            "id": comment.id,
            "text": comment.body,
            "timestamp": comment.created_utc
        }
        
        r.lpush("comments_queue", json.dumps(comment_data))
        print(f"Added comment {comment.id} to Redis queue")
        time.sleep(1)  

if __name__ == "__main__":
    stream_comments()