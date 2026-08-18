text = input("Enter a paragraph: ")

words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Total number of words:", len(words))
print("Word Frequency:", frequency)

top3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 frequent words:", top3)

vowels = "aeiou"
count = 0

for ch in text.lower():
    if ch in vowels:
        count += 1

print("Number of vowels:", count)