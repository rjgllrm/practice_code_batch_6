word = input("Enter a word: ")
width = int(input("Enter width for center: "))
space = input("Enter space for center: ")
total = width - len(wordt)
left_space = total // 2
right_space = total - left_space
print("Center:", space * left_space + word + space * right_space)
