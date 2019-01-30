d = {}
print(d['name'])  # KeyError
print(d.get('name'))  # No exception
print(d.get('name', 'N/A'))  # provide self-defined error message

d['name'] = 'Eric'
d.get('name')  # all good
