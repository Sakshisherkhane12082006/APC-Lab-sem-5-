import re
text = "My phone numbers are 9699551596 and 986025420"
result = re.findall(r"\d+", text)
print(result)