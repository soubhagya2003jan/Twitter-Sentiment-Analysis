import tweepy
import pandas as pd
from config import (
    TWITTER_API_KEY, 
    TWITTER_API_SECRET, 
    TWITTER_ACCESS_TOKEN, 
    TWITTER_ACCESS_TOKEN_SECRET,
    TWITTER_BEARER_TOKEN
)

class TwitterClient:
    def __init__(self):
        self.client = self._initialize_client()
        
    def _initialize_client(self):
        
        client = tweepy.Client(
            bearer_token=TWITTER_BEARER_TOKEN,
            consumer_key=TWITTER_API_KEY, 
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN, 
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )
        print("Twitter API client initialized successfully")
        return client
    
    def get_tweets(self, query, max_results=100):
        
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=['created_at', 'lang', 'public_metrics']
            )
            
            if not tweets.data:
                print(f"No tweets found for query: {query}")
                return pd.DataFrame()
            
            
            tweet_data = []
            for tweet in tweets.data:
                tweet_data.append({
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'lang': tweet.lang,
                    'retweet_count': tweet.public_metrics['retweet_count'],
                    'reply_count': tweet.public_metrics['reply_count'],
                    'like_count': tweet.public_metrics['like_count']
                })
            
            df = pd.DataFrame(tweet_data)
            print(f"Successfully fetched {len(df)} tweets")
            return df
        
        except Exception as e:
            print(f"Error fetching tweets: {e}")
            return pd.DataFrame()