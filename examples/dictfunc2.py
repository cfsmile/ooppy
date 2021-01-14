# A simple database
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
# name = input('Name:')
name = 'Cecil'
request = input('Phone number(p) or address(a)?')
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
# Use get to provide default values:
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

if name in people:
    print("%s's %s is %s." % (name, label, result))
