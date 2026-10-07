# ask user to enter age and weight and check eligibility for blood donation age 20 to 60 weight 40 in  python
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age >= 20 and age <= 60 and weight >= 40:
    print("You are eligible for blood donation.")
else:
    print("You are not eligible for blood donation.")