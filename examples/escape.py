# -*- encoding: utf-8 -*-
#!/usr/bin/env python

print('Hello, \nworld!')

path = 'c:\nowhere'
print(path)

cpath = 'c:\\program files\\fnord\\foo\\bar\\baz\\frozz\\bozz'
print(cpath)

print(r'c:\nowhere')
rpath = r'c:\program files\fnord\foo\bar\baz\frozz\bozz'
print(rpath)

print(r'Let\'s go!')  # leave \' as it be

# print(r'This is illegal\')
print(r'c:\program files\foo\bar''\\')
