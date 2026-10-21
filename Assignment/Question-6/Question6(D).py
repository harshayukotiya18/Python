# d) Search for an element and display its index if found; otherwise, display an
# appropriate message.

from array import *;

a=[1,2,3,4,5,6,7,8,9,10]
i=int(input("Enter Search Element:"))

if i in a:
   print(a.index(i))
else:
    print("Search element not found in a")
    
    