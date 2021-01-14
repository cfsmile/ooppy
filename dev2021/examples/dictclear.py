# 1.
d = {}
d['name'] = 'Adam'
d['age'] = 39
print(d)
rv = d.clear()
print(rv)

# 2.
# first scenario
x = {}
y = x
x['key'] = 'value'
y
x = {}
y

# second scenario
x = {}
y = x
x['key'] = 'value'
y
x.clear()
y
