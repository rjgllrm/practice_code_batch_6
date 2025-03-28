words = input("Enter a word: ")
result = ""
for char in word:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print("Lower:", result)
