# e) Check element membership using in and not in.

from array import *;

a=[1,2,3,4,5,6,7,8,9,10]
b=10
c=4
 
print("IN") 
if b in a:
    print(f"{b} in a ")
else:
    print(f"{b} is not in")
    
    
print("NOT IN")
if c not in a:
    print(f"{c} not in a")
else:
    print(f"{c} in a")