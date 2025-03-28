word = input("Enter a word: ")
suffix = input("Enter suffix to check: ")
print("Endswith:", word[-len(suffix):] == suffix if len(suffix) <= len(word) else False)
