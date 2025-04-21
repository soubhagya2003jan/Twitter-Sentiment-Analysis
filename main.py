from twitter_client import TwitterClient
from data_processor import DataProcessor
from sentiment_analyzer import SentimentAnalyzer
from visualizer import Visualizer
from config import DEFAULT_OUTPUT_FILE

def run_analysis(query="#IPL2025", max_results=100, output_file=DEFAULT_OUTPUT_FILE):
    
    print(f"Starting sentiment analysis for query: {query}")
    
    
    twitter_client = TwitterClient()
    sentiment_analyzer = SentimentAnalyzer()
    
    
    tweets_df = twitter_client.get_tweets(query, max_results)
    
    if tweets_df.empty:
        print("No tweets to analyze. Exiting.")
        return
    
    
    processed_df = DataProcessor.preprocess_data(tweets_df)
    
    
    results_df = sentiment_analyzer.analyze_sentiment(processed_df)
    
    
    Visualizer.visualize_results(results_df)
    
    
    Visualizer.print_summary(results_df)
    
    
    DataProcessor.save_results(results_df, output_file)
    
    print("\nAnalysis complete!")
    return results_df

if __name__ == "__main__":
    
    results = run_analysis(
        query="#IPL2025 OR #IPL OR #IndianPremierLeague", 
        max_results=100
    )