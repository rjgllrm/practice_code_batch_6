words = input("Enter a word: ")
string = input("Enter substring to find index: ")
sub_len = len(string)
found = False
for me in range(len(words) - sub_len + 1):
    if words[me:me + sub_len] == string:
        print(me)
        found = True
        break
if not found:
    print("string not found")
