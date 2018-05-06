filename = input("enter filename: ")
with open (filename) as f:
    text = f.read()
print(text)
