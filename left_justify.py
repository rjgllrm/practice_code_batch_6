word = input("Enter a word: ")
width = int(input("Enter width for ljust: "))
space = input("Enter space for ljust: ")
print("Justified:", word + space * (width - len(word)) if len(word) < width else word)
