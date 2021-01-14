name = input('What is your name?')
# name = 'c'
if name.endswith('Adam'):
    if name.startswith('Mr.'):
        print("Hello, Mr. Adam")
    elif name.startswith('Mrs.'):
        print("Hello, Mrs. Adam")
    else:
        print("Hello, Adam")
else:
    print("Hello, stranger")
