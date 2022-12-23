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
text = "I hate trees"
score = analyzer.polarity_scores(text)
print(text, score)
text = "I like trees"
score = analyzer.polarity_scores(text)
print(text, score)

# load book
with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

score = analyzer.polarity_scores(book)
print("book", score)

# extract chapters
chapters = re.split("Chapter [0-9]+", book)[1:]
# extract titles
titles = re.findall('(Chapter [0-9]+)[\n]+(.+)', book)
# format chapters
titles = [f"{chapter}: {title}" for chapter, title in titles]
print(chapters)
print(titles)

# print chapters scores
for nr, (title, chapter) in enumerate(zip(titles, chapters), start=1):
    score = analyzer.polarity_scores(chapter)
    print(f'{nr:2d} - {title}: {score}')
