i = 1
while i < 10:
    i += 1
    if (i % 2) > 0:  # if not an even number, it won't print
        continue
    print(i)  # print even number

i = 1
while True:
    print(i)  # print 1~10
    i += 1
    if i > 10:
        break

# for reading
for n in range(100, 1, -1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)
        break

while i < 10:
    if i % 2 == 0:
        continue
    print(i + ' ')
    i += 1
