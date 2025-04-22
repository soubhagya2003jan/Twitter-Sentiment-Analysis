# Twitter Sentiment Analysis for IPL2025

## Project Overview
This project analyzes public sentiment on Twitter regarding IPL2025 by collecting tweets with relevant hashtags and applying advanced natural language processing techniques to determine whether the sentiment is positive, negative, or neutral. The analysis includes visualizations to help understand trends and patterns in public opinion.

## Methodology
1. **Data Collection**: Tweets are collected using the Twitter API v2 with specific search queries related to IPL2025.
2. **Data Preprocessing**: Raw tweets are cleaned by removing URLs, mentions, special characters, and extra whitespace to prepare them for analysis.
3. **Sentiment Analysis**: A pre-trained BERT model is used to classify the sentiment of each tweet as positive, negative, or neutral.
4. **Visualization**: The results are visualized through various charts to identify patterns and trends.
5. **Data Storage**: Analyzed data is saved to CSV for further analysis or reference.

## Project Structure
- `main.py`: Entry point that orchestrates the entire analysis pipeline
- `config.py`: Configuration settings and environment variables
- `twitter_client.py`: Handles Twitter API authentication and data retrieval
- `data_processor.py`: Cleans and preprocesses tweet data
- `sentiment_analyzer.py`: Performs sentiment analysis using BERT
- `visualizer.py`: Creates visualizations of the analysis results

## Tools & Libraries
- **Python**: Primary programming language
- **Tweepy**: For Twitter API integration
- **Transformers**: For BERT-based sentiment analysis
- **NLTK**: For natural language processing tasks
- **Pandas**: For data manipulation and analysis
- **Matplotlib & Seaborn**: For data visualization
- **python-dotenv**: For secure management of API credentials

## Setup & Installation
1. **Prerequisites**:
   - Python 3.7+
   - Twitter Developer Account with API credentials

2. **Environment Setup**:
   ```bash
   # Clone the repository 
   # Create a virtual environment (recommended)
   python -m venv venv
   venv\Scripts\activate

   # Install dependencies
   pip install tweepy python-dotenv pandas numpy matplotlib seaborn transformers torch
