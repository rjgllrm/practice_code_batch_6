words = input("Enter the main string: ")
string = input("Enter the string to count: ")
count = 0 
text_length = len(words)
sub_length = len(string)

for i in range(text_length - sub_length + 1):
    if words[i:i + sub_length] == string:  
        count += 1 

print(f'The substring "{string}" appears {count} times in the given string.')
