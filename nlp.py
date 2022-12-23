import re
import nltk
# use in case of missing module error
# nltk.download('stopwords')
from nltk.corpus import stopwords

# load book
with open('miracle_in_the_andes.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# get list of all words in the book
pattern = re.compile('[a-zA-Z]+')
findings = re.findall(pattern, book.lower())

# create dict with words count in book
book_words = {}
for word in findings:
    book_words[word] = book_words.get(word, 0) + 1

# create list of word count in reverse order
book_stats = [(value, key) for key, value in book_words.items()]
book_stats = sorted(book_stats, reverse=True)

# filter out english stop words
swe = stopwords.words('english')
filtered_words = [(word, count) for count, word in book_stats if word not in swe]
print(filtered_words[:30])
