word = input("Enter a word: ")
prefix = input("Enter prefix to remove: ")
if text.startswith(prefix):
    print("Removeprefix:", text[len(prefix):])
else:
    print("Removeprefix:", text)
