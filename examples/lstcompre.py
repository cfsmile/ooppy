
# 1.
alist = [x*x for x in range(10)]

al = []
for x in range(10):
    al.append(x*x)

# 2. list comprehension with condition
b_list = [x*x for x in range(10) if x % 3 == 0]

# 3. list comprehension creating tuple
c_list = [(x, y) for x in range(3) for y in range(3)]

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

# 4. create a list by list comprehension with two smaller lists
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
[b + '+' + g for b in boys for g in girls if b[0] == g[0]]

# 5. flat a nested list
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

# 6. calsulate prime numbers less than 100, like a function
import math
[p for p in range(2, 100) if 0 not in
 [p % d for d in range(2, int(math.sqrt(p) + 1))]]
