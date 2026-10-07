# Traversing an array

from operator import lt

arr = [10, 20, 30, 40, 50]
print("Array elements are:")
for i in range(len(arr)):
    print(f"Element at index {i}: {arr[i]}")
arr = [10, 20, 30, 40]
i = 0
while i < len(arr):
    print(arr[i])
    i += 1