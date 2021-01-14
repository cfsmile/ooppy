# 1.
p = 'rw'
'w' in p
'x' in p
'x' not in p

# 2. Check a user name and PIN code
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith' '7524'],
    ['jones', '9843'],
]

# username = input('User Name: ')
# pin = input('PIN code: ')
username = 'jones'
pin = '9843'
if [username, pin] in database:
    print('Access granted!')
else:
    print('Access denied!')
