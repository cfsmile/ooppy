# 1.
# x = input('Input two integers:')
x = (3, 10)
# x = (10, 3)
a, b = x  # unpacking
if a > b:
    a, b = b, a
print(a, b)

# 2.
name = input('What is your name?')
if name.endswith('Michael'):
    print("Hello, Mr. Michael")
