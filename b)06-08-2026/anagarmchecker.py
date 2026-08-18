def normalize(text):
    result = ""

    for ch in text.lower():
        if ch.isalnum():
            result += ch

    return result

def is_anagram(str1, str2):
    return sorted(normalize(str1)) == sorted(normalize(str2))

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_anagram(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")