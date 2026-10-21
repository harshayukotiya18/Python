# f) Display the list in ascending and descending order using sort() and sorted().

arr = [1,2,3,4,5,6,7,8,9,10]

print("ascending order",sorted(arr))


print("descending order:",sorted(arr,reverse=True))

print("SORT")
arr.sort()
print("ascending order:",arr)

arr.sort(reverse=True)
print("descending order:",arr)