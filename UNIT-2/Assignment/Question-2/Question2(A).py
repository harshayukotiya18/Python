list1=['sachin','virat','rohit','dhoni','rahul']
list2=[[100,'sachin'],[87,'virat'],[45,'rohit'],[45,'dhoni'],[99,'rahul']]

i = input("enter name:")

if i in list1:
    index = list1.index(i)
    print("found",{index})
else:
    print("not found")
          