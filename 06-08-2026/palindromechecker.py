text = input("Enter a word or phrase: ")
text = text.replace(" ","").lower()
if text == text[::-1]:
    print("True")
else:
    print("False")