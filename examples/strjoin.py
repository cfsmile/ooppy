seq = [1, 2, 3, 4, 5]
sep = '+'
sep.join(seq)  # type error

seq = ['1', '2', '3', '4', '5']
sep.join(seq)

dirs = '', 'usr', 'bin', 'env'
'/'.join(dirs)
print('C:' + '\\'.join(dirs))
print('\\'.join(dirs))  # how about this?

''.join(seq)
