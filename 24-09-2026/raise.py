class AgeError(Exception):
    pass
age = int(input("Enter your age: "))
if age < 18:
    raise AgeError
print("You are eligible")