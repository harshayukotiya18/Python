fruits = ["Apple","Banana","Mango","Orange"]
search = input("Enter Fruit Name: ")
for i in range(len(fruits)):
    if search == fruits[i]:
        print("Fruit Found at Index:", i)
        break
else:
    print("Fruit Not Found")