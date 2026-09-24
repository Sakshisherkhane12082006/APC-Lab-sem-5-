import re
password = input("Enter password: ")
pattern = r"^[A-Za-z0-9@#$]{8,}$"
if re.search(pattern, password):
    print("Valid password")
else:
    print("Invalid password")