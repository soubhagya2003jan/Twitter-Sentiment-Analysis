import re
import pandas as pd

class DataProcessor:
    @staticmethod
    def clean_tweet(tweet):
        
        tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
       
        tweet = re.sub(r'@\w+', '', tweet)
        
        tweet = re.sub(r'#', '', tweet)
        
        tweet = re.sub(r'[^\w\s]', '', tweet)
        
        tweet = re.sub(r'\s+', ' ', tweet).strip()
        return tweet
    
    @staticmethod
    def preprocess_data(df):
        
        if df.empty:
            return df
        
        
        df['cleaned_text'] = df['text'].apply(DataProcessor.clean_tweet)
        
        
        df = df[df['cleaned_text'].str.strip() != '']
        
        return df
    
    @staticmethod
    def save_results(df, filename):
        
        if not df.empty:
            df.to_csv(filename, index=False)
            print(f"Results saved to {filename}")