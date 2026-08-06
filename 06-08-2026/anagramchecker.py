s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = ''.join(sorted(s1.replace(" ","").lower()))
s2 = ''.join(sorted(s2.replace(" ","").lower()))

if s1 == s2:
    print("Anagram")
else:
    print("Not Anagram")