# c) Remove a specified element using remove() and remove the last element using
# pop().

from array import *;

a=[1,2,3,4,5,6,7,8,9]

print("Original array:",a)


# using remove()
a.remove(9)
print("After remove :",a)


# using pop()
a.pop()
print("After pop:",a)