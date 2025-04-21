import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import VISUALIZATION_DIR

class Visualizer:
    @staticmethod
    def visualize_results(df):
        
        if df.empty:
            print("No data to visualize")
            return
        
        
        sns.set(style="whitegrid")
        
        
        plt.figure(figsize=(10, 6))
        sentiment_counts = df['sentiment'].value_counts()
        plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', 
                colors=['green', 'gray', 'red'])
        plt.title('Sentiment Distribution for IPL2025 Tweets')
        plt.savefig(os.path.join(VISUALIZATION_DIR, 'sentiment_distribution_pie.png'))
        plt.close()
        
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x='sentiment', data=df, palette={'Positive': 'green', 'Neutral': 'gray', 'Negative': 'red'})
        plt.title('Sentiment Distribution for IPL2025 Tweets')
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Tweets')
        plt.savefig(os.path.join(VISUALIZATION_DIR, 'sentiment_distribution_bar.png'))
        plt.close()
        
        
        if len(df) > 10:
            plt.figure(figsize=(12, 6))
            df['date'] = df['created_at'].dt.date
            sentiment_by_date = df.groupby(['date', 'sentiment']).size().unstack().fillna(0)
            sentiment_by_date.plot(kind='line', marker='o')
            plt.title('Sentiment Trends Over Time for IPL2025')
            plt.xlabel('Date')
            plt.ylabel('Number of Tweets')
            plt.legend(title='Sentiment')
            plt.savefig(os.path.join(VISUALIZATION_DIR, 'sentiment_over_time.png'))
            plt.close()
        
        
        plt.figure(figsize=(12, 6))
        engagement_metrics = ['retweet_count', 'reply_count', 'like_count']
        engagement_by_sentiment = df.groupby('sentiment')[engagement_metrics].mean()
        engagement_by_sentiment.plot(kind='bar')
        plt.title('Average Engagement by Sentiment for IPL2025 Tweets')
        plt.xlabel('Sentiment')
        plt.ylabel('Average Count')
        plt.savefig(os.path.join(VISUALIZATION_DIR, 'engagement_by_sentiment.png'))
        plt.close()
        
        print("Visualizations created and saved successfully")
    
    @staticmethod
    def print_summary(df):
        
        if df.empty:
            return
            
        sentiment_summary = df['sentiment'].value_counts(normalize=True) * 100
        print("\nSentiment Analysis Summary:")
        for sentiment, percentage in sentiment_summary.items():
            print(f"{sentiment}: {percentage:.1f}%")