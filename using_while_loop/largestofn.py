n = int(input("Enter n: "))

i = 1
largest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))

    if num > largest:
        largest = num

    i = i + 1

print("Largest =", largest)