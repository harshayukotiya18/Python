# write a python program to print all from 1 to 1000 that are not divide by 2,3,5,7,11,13,17 and 9
for i in range(1, 1001):
    if (i % 2 != 0 and
        i % 3 != 0 and
        i % 5 != 0 and
        i % 7 != 0 and
        i % 9 != 0 and
        i % 11 != 0 and
        i % 13 != 0 and
        i % 17 != 0):
        
        print(i)