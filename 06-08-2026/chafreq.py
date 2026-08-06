text = input("Enter String: ")

choice = input("Ignore case? (y/n): ")

if choice == "y":
    text = text.lower()

freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0)+1

result = sorted(freq.items(), key=lambda x:x[1], reverse=True)

for ch,count in result:
    print(ch,":",count)