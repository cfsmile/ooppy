# 1. indexing
tag = '<a href="http://www.python.org">Python web site</a>'
tag[9:30]
tag[32:-4]

# 2. indexing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[3:6]
numbers[0:1]
numbers[7:10]
numbers[-3:-1]
numbers[-3:0]
numbers[-3:]
numbers[:3]
numbers[:]
# if the leftmost index comes later in the sequence than the second
# one, the results is always an empty sequence.

# 3. slicing step
numbers[0:10:1]
numbers[0:10:2]
numbers[3:6:3]
numbers[::4]
numbers[8:3:-1]
numbers[10:0:-2]
numbers[0:10:-2]
numbers[::-2]
numbers[5::-2]
numbers[:5:-2]

# 4. print out a date, given year, month, and day as numbers
months = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
 ]

# A list with one ending for each number form 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

#  year = input('Year:')
#  month = input('Month(1-12):')
#  day = inpu('Day(1-31):')

year = 2019
month = 5
day = 16

month_number = int(month)
day_number = int(day)

# Remember to substract 1 from month and day to get a correct index
month_name = months[month_number - 1]
ordinal = str(day) + endings[day_number - 1]

print(month_name + ' ' + ordinal + ',' + str(year))
