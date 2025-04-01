word = input("Enter a word: ")
width = int(input("Enter width for rjust: "))
if len(word) >= width:
    print(word)
else:
    spaces = width - len(word)
    print(' ' * spaces + word)
