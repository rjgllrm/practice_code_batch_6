word = input("Enter a word: ")
prefix = input("Enter prefix to remove: ")
if word.startswith(prefix):
    print("Removeprefix:", word[len(prefix):])
else:
    print("Removeprefix:", word)
