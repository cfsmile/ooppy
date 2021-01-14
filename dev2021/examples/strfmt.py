# The code is taken from
# https://docs.python.org/3.6/library/string.html#template-strings

# 1. positional formatting
'{0}, {1}, {2}'.format('a', 'b', 'c')

'{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only

'{2}, {1}, {0}'.format('a', 'b', 'c')

'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence

'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated


# 2. formatting according to the argument's names
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N',
                                              longitude='-115.81W')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)


# 3. formatting the attributes of arguments
c = 3-5j
('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c)


class Point:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


str(Point(4, 2))

# 4. formatting elements of the arguments
coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)

# 5. output as string
"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')

# 6. alignment and width
'{:<30}'.format('left aligned')

'{:>30}'.format('right aligned')

'{:^30}'.format('centered')

'{:*^30}'.format('centered')  # use '*' as a fill char

# 7. floating numbers and sign
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always

'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers

# show only the minus -- # same as '{:f}; {:f}'
'{:-f}; {:-f}'.format(3.14, -3.14)

# 8. delimination of thousand
'{:,}'.format(1234567890)

# 9. formatting date
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d)
