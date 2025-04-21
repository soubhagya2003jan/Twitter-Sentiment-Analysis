import os
from dotenv import load_dotenv


load_dotenv()


TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")


BERT_MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"


DEFAULT_OUTPUT_FILE = 'ipl2025_sentiment_results.csv'
VISUALIZATION_DIR = 'visualizations'


os.makedirs(VISUALIZATION_DIR, exist_ok=True)