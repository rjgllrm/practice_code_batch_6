word = input("Enter a word: ")
prefix = input("Enter a prefix: ")
starts_with = True
if len(prefix) > len(word):
    starts_with = False
else:
    for me in range(len(prefix)):
        if word[me] != prefix[me]:
            starts_with = False
            break
print(starts_with)
