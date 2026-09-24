try:
    age=int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid age......")
else:
    print("Your age is", age)
finally:
    print("Program completed")