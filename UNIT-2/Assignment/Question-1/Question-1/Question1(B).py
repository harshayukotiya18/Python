# b) Update an element at a specified index entered by the user.
from array import *


arr = [1,2,3,4,5,6,7,8,9,10]
i = int(input("enter a number: "))
new=int(input("enter a number"))



if 0 <= i < len(arr):
    arr[i]=new
    print("updated list",arr)
   
    
else:
    print("not ")











