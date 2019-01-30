# 1.
'Price of eggs: $%d' % 42
'Hexadecimal price of eggs: %x' % 42

# 2.
from math import pi
'Pi: %f...' % pi
'Very inexact estimate of pi: %i' % pi  # signed integer %i, %d
'Using str: %s' % 42

# 3.
'%10f' % pi  # width 10
'%10.2f' % pi  # width 10, precision 2 demicals after point
'%.2f' % pi  # default width, 2 decimals after point
'%.5s' % 'Guido van Rossum'

# 4. * can be used as wdith, precision or both,
'%.*s' % (5, 'Guido van Rossum')

# 5.
'010.2f' % pi  # flag: 0, -, +, or space, 0 is a placeholder
'%-10.2f' % pi  # - align left
print(('% 5d' % 10) + '\n' + ('% 5d' % - 10))  # space for alignment
print(('%+5d' % 10) + '\n' + ('%+5d' % - 10))  # show + symbol

# 6. print a formatted price list with a given width

width = int(input('Please enter width: '))

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print('=' * width)
print(header_format % (item_width, 'Item', price_width, 'Price'))

print('-' * width)
print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8))
print(format % (item_width, 'Prunes (4 libs.)', price_width, 12))

print('=' * width)
