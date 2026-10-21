list2=[{"marks":100,"name":'sachin'},
    {"marks":87,"name":'virat'},
    {"marks":56,"name":'rohit'},
    {"marks":45,"name":'dhoni'},
    {"marks":99,"name":'rahul'}
    ]

highest_student = max(list2,key=lambda x:x["marks"])
print(f"highest name:{highest_student['name']}(highest marks:{highest_student['marks']})")

total_marks=sum(student["marks"] for student in list2)
avg_marks= total_marks / len(list2)

print(f"average marks:{avg_marks}")