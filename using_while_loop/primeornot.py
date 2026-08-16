n = int(input("Enter number: "))

i = 2
prime = True

while i < n:
    if n % i == 0:
        prime = False
        break
    i = i + 1

if prime and n > 1:
    print("Number is prime")
else:
    print("Number is not prime")