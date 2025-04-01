word = input("Enter a word: ")
is_lower = True
for char in word:
    if 'A' <= char <= 'Z':
        is_lower = False
        break
print(is_lower)
