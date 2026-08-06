text = input("Enter Text: ")
stopwords = ["is", "the", "and", "a", "an", "of", "to", "in"]
words = text.split()
result = []
for word in words:
    if word.lower() not in stopwords:
        result.append(word)

print("Clean Text:")
print(" ".join(result))