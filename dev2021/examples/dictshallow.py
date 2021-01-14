# use pytutor to show the difference
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machine'].remove('bar')
y
x
