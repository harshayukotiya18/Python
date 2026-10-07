# Performing arithmetic operations

from array import array
a = array('i', [10, 20, 30, 40])
total = sum(a)
average = total / len(a)
print("Sum:", total)
print("Average:", average)
numbers = [10, 20, 30, 40, 50]
doubled = []
for num in numbers:
    doubled.append(num * 2)
print("Original:", numbers)
print("Doubled:", doubled)