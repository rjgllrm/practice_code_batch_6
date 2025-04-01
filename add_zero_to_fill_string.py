word = input("Enter a word: ")
width = int(input("Enter width for fill: "))
if len(word) >= width:
    print(word)
else:
    zeros = width - len(word)
    print('0' * zeros + word)
