import re
pattern = re.compile(r"\d+")
text = "My age is 20 and gouri's age is 21"
result = pattern.findall(text)
print(result)