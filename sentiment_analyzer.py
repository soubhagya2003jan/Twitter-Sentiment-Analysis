from transformers import pipeline
from config import BERT_MODEL_NAME

class SentimentAnalyzer:
    def __init__(self):
        self.model = self._initialize_model()
        
    def _initialize_model(self):
        
        sentiment_analyzer = pipeline("sentiment-analysis", model=BERT_MODEL_NAME)
        print("BERT sentiment model initialized successfully")
        return sentiment_analyzer
    
    def analyze_sentiment(self, df):
        
        if df.empty:
            return df
        
        
        sentiments = []
        scores = []
        
        for tweet in df['cleaned_text']:
            try:
                result = self.model(tweet)[0]
                label = result['label']
                score = result['score']
                
                
                if '1' in label or '2' in label:
                    sentiment = 'Negative'
                elif '3' in label:
                    sentiment = 'Neutral'
                else:  
                    sentiment = 'Positive'
                
                sentiments.append(sentiment)
                scores.append(score)
            except Exception as e:
                print(f"Error analyzing sentiment: {e}")
                sentiments.append('Unknown')
                scores.append(0.0)
        
        df['sentiment'] = sentiments
        df['sentiment_score'] = scores
        
        return df