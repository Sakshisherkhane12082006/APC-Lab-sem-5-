class AgeError(Exception):
    pass
try:
    age=int(input("Enter your age: "))
    if age<18:
        raise AgeError
    print("You are eligible")
except AgeError:
    print("Age must be 18 or above")