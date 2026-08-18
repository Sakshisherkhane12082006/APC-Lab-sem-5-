book1 = set(input("Enter words of Book 1: ").lower().split())
book2 = set(input("Enter words of Book 2: ").lower().split())

print("Unique words in Book 1:", book1)
print("Unique words in Book 2:", book2)

print("Common words:", book1.intersection(book2))

print("Words only in Book 1:", book1.difference(book2))
print("Words only in Book 2:", book2.difference(book1))

print("Total unique words:", len(book1.union(book2)))