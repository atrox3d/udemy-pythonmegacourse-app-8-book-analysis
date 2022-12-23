import re

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
try:
    analyzer = SentimentIntensityAnalyzer()
except LookupError as lue:
    """
    **********************************************************************
    Resource vader_lexicon not found.
    Please use the NLTK Downloader to obtain the resource: 

    >>> import nltk
    >>> nltk.download('vader_lexicon')
    """
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

# TODO https://stackoverflow.com/questions/62284611/sentiment-analysis-of-italian-sentences
score = analyzer.polarity_scores("I hate trees")
print(score)
score = analyzer.polarity_scores("I like trees")
print(score)

# load book
with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

score = analyzer.polarity_scores(book)
print(score)
