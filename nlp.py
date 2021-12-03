import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import textstat

# Initialising our parameter here
text = "Life is Great! I won the lottery."

# text = "It will rain today, don't forget to take umberlla."

# Passing parameter to NLP
tokens = nltk.word_tokenize(text)
print(sent_tokenize(text))
print(tokens)

# This loop through each word and print it to the console
for x in tokens:
  print(x)

# Print how many sentence in text
print("number of sentence:", textstat.sentence_count(text))

# Print how many characters in text excluding space.
print("number of characters:", textstat.char_count(text, ignore_spaces=True))

# Print how many words in text
print("number of words:", len(text.split()))
