word = input("Enter a word: ")
words = word.split()
title = [word[0].upper() + word[1:].lower() if word else "" for word in words]
print("Title:", ' '.join(title))
