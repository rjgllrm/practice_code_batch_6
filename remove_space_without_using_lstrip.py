word = input("Enter a word: ")
index = 0
while index < len(word) and word[index] == ' ':
    index += 1
print("Lstrip:", word[index:])

