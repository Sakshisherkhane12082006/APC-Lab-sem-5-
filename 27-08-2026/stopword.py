import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
text = "I am Sakshi and i am the best student with the good marks in the class"
words = text.split()
for word in words:
    if word not in stopwords.words('english'):
        print(word)