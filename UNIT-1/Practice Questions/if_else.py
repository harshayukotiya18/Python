# Write a python program to print number is positive/negative using if-else
# statement.

from operator import gt


num = int(input('Enter a number: '))
if num >= 0:
    print('Number is Positive')
else:
    print('Number is Negative')