# 1. while else

count = 0
while count < 5:
    print("%d is less than 5." % count)
    count += 1
else:
    print("%d is no less than 5." % 5)

# 2. for else
for i in xrange(2, n):
    # found = True
    for j in xrange(2, i):
      if i % j == 0:
         # found = False 
        break
    else:
      print "{} it's a prime number".format(i)
    # if found:
         # print "{} it's a prime number".format(i)    
