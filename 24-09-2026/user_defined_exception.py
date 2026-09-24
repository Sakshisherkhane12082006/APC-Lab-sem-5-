class AgeError(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 18:
        print("AgeError: Age must be 18 or above")
    else:
        print("You are eligible")
except ValueError:
    print("Please enter a valid age")