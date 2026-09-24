import re 
mobile=input("enter mobile number:")
pattern=r"^[6-9][0-9]{9}$"
if re.search(pattern,mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")