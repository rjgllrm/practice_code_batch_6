word = input("Enter a word: ")
upper = True
for char in word:
    if 'a' <= char <= 'z':
        upper = False
        break
print("is_upper:", upper)
