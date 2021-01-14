# 1. create a list
# consists of strings and nummerrics
a_list = ['a', 'b', 'mpilgrim', 'z', 'example', 2018]
b_list = []  # create a empty list, whose value is False

# 2. take a list as conditional expression
if b_list:
    print('True')
else:
    print('False')

# 3. create a list by list()
c_list = list((3, 5, 7, 9, 11))  # cast a tuple to a list
d_list = list(range(1, 10, 2))  # cast a range object to a list
e_list = list('hello, world!')  # cast a string to a list
f_list = list()  # create empty list

# 4. unbinding the variables, and delete the object as well
del a_list  # unbinding the variable
# NameError: name 'a_list' is not defined. a_list is not binding to any value
a_list

# 5. unbinding the variable, but the object it pointed to still exists.
g_list = d_list
del d_list
d_list
g_list
