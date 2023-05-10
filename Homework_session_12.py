#Compare 2 books from project gutenberg.
# Which one has more unique words? Which one has the ratio of unique to total words higher?

import requests
from string import punctuation

# Download the books in a txt format
book1_url = "https://www.gutenberg.org/files/1513/1513-0.txt" # Romeo and Juliet by William Shakespeare
book2_url = "http://www.gutenberg.org/files/11/11-0.txt" # Alice's Adventures in Wonderland by Lewis Carroll

book1 = requests.get(book1_url).text
book2 = requests.get(book2_url).text

# Create lists by processing the text (remove punctuation and converting to lowercase)
book1_processed = book1.translate(str.maketrans("", "", punctuation)).lower()
book2_processed = book2.translate(str.maketrans("", "", punctuation)).lower()

book1_words = book1_processed.split()
book2_words = book2_processed.split()

book1_unique_words = []
book2_unique_words = []

#Add the unique words
for word in book1_words:
    if word not in book1_unique_words:
        book1_unique_words.append(word)

for word in book2_words:
    if word not in book2_unique_words:
        book2_unique_words.append(word)

#compare
if len(book1_unique_words) > len(book2_unique_words):
    print("Book 1 has more unique words")
elif len(book1_unique_words) < len(book2_unique_words):
    print("Book 2 has more unique words")
else:
    print("Both books have the same number of unique words")