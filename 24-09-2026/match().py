import re
text = "Sakshi Sherkhane is a student of CSE"
result = re.match("Sakshi", text)
print(result.group())