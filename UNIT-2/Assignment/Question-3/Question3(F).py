# Search for a specified element using index(), displaying an appropriate message if it
# is not found.


a=(1,2,3,4,5,6,7,8,9,10)
index=int(input("Enter a number to search:"))
try:
    print("element is at index ",a.index(index),"index")
except ValueError:
    print("The number", index, "is not found in the tuple.")
