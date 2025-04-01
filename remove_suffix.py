name = input("Enter a name: ")
suffix = input("Enter suffix to remove: ")
if name.endswith(suffix):
    print(name[:-len(suffix)])
else:
    print(name)
