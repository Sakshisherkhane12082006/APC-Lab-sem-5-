# Single line string using single quotes

str1 = 'Hello, Python!'
print(str1)

# Single line string using double quotes

str2 = "Welcome to Python Programming"
print(str2)

# Multi-line string using triple single quotes

str3 = '''This is the first line.
This is the second line.
This is the third line.'''

print(str3)

# Multi-line string using triple double quotes

str4 = """Python is easy to learn.
It is powerful.
It is widely used."""

print(str4)


#1
string = input("Enter a string: ")

count = 0
for i in string:
    count += 1

print("Length of the string:", count)

#2 
string = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in string:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        consonants += 1
    elif '0' <= ch <= '9':
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)

#3
string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

print("Reversed String:", reverse)

#4
string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
    #5
    string = input("Enter a string: ")

upper = lower = 0

for ch in string:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)

#6
string = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in string:
    if ch == old:
        result += new
    else:
        result += ch

print("Modified String:", result)

#7
string = input("Enter a string: ")

result = ""

for ch in string:
    if ch != ' ':
        result += ch

print("String without spaces:", result)

#8
string = input("Enter a string: ")
char = input("Enter the character to search: ")

count = 0

for ch in string:
    if ch == char:
        count += 1

print("Frequency of", char, "is:", count)

#9
string = input("Enter a string: ")

print("First Character:", string[0])
print("Last Character:", string[-1])

#10
string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))
    