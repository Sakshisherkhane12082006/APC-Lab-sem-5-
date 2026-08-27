import nltk
from nltk.tokenize import sent_tokenize
text = "I like reading boooks. My all time favorite book is We were never meant to be. It is by Palle vasu."
sentences = sent_tokenize(text)
print(sentences)