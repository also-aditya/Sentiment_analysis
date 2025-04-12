import redis
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
import nltk
nltk.download('vader_lexicon')

r = redis.Redis(host='localhost', port=6379, db=0)

sid = SentimentIntensityAnalyzer()

def process_comments():
    print("Starting sentiment analysis...")
    while True:
        comment_json = r.brpop("comments_queue", timeout=5)
        if comment_json:
            _, comment_data = comment_json  # brpop returns (key, value)
            comment = json.loads(comment_data.decode('utf-8'))
            text = comment["text"]

            scores = sid.polarity_scores(text)
            sentiment = "Positive" if scores["compound"] >= 0.05 else "Negative" if scores["compound"] <= -0.05 else "Neutral"
            
            processed_data = {
                "id": comment["id"],
                "text": text,
                "sentiment": sentiment,
                "compound_score": scores["compound"],
                "timestamp": comment["timestamp"]
            }
            r.set(f"sentiment:{comment['id']}", json.dumps(processed_data))
            print(f"Processed comment {comment['id']}: {sentiment}")
        time.sleep(0.1) 

if __name__ == "__main__":
    process_comments()