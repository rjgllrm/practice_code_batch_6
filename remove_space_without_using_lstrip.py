word = input("Enter a word: ")
index = 0
while index < len(text) and text[index] == ' ':
    index += 1
print("Lstrip:", text[index:])

