# g) Create an alias and a clone of the list, modify one element, and demonstrate the
# difference between aliasing and cloning.


a=[1,2,3,4,5,6,7,8,9,10]
alias=a


clone1=a.copy()

alias[0]=11



print("Alias:",alias)
print("Copy",clone1)
