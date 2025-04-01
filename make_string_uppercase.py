word = input("Enter a word: ")
result = ""
for char in word:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char
print(result)
