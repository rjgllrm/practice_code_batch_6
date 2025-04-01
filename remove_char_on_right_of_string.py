word = input("Enter a word: ")

me = len(word) - 1
while me >= 0 and word[me] == ' ':
    me -= 1
print(word[:me+1])
