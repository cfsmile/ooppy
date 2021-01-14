# import usage
# 1.
import math
print(math.floor(32.9))

# 2.
from math import sqrt

# 3. from math import *
print(sqrt(9))

# 4.
# print(sqrt(-1))
import cmath as cm
print(cm.sqrt(-1))

# 5. wierd usage, like binding
from math import sqrt as st1
from xmath import sqrt as st2
