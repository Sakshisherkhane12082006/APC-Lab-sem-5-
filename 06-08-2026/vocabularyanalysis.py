book1 = set(input("Book1 Text: ").lower().split())
book2 = set(input("Book2 Text: ").lower().split())

print("Unique Book1:", book1)
print("Unique Book2:", book2)
print("Common:", book1 & book2)
print("Only Book1:", book1 - book2)
print("Only Book2:", book2 - book1)
print("Total Unique:", len(book1 | book2))