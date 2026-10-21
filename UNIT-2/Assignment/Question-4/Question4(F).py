# f) Compare two strings using ==, !=, <, and >.

a= "hello"
b= "world"


if a==b:
    print("strings are equal")
else:
    print("strings are not equal")

if a!=b:
    print("strings are not equal")
else:
    print("strings are equal")

if a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is not less than {b}")

if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")