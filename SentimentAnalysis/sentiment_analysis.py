import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analyzer(text_to_analyze):
    # Initialize the SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Get the polarity scores
    sentiment_scores = sia.polarity_scores(text_to_analyze)

    # Determine the sentiment label based on the compound score
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        label = 'Positive'
    elif compound_score <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'

    # Return the result
    return {'label': label, 'score': compound_score}

# Example usage:
# text_to_analyze = "I love using NLTK for sentiment analysis. It's amazing!"
# result = sentiment_analyzer(text_to_analyze)
# sentiment_analyzer("Result of Sentiment Analysis")
# print(result)
