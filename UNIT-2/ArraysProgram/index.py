# index():

from array import array

arr = array('i', [10, 20, 30, 40, 50])
search_item = 30

if search_item in arr:
    index = arr.index(search_item)
    print(f"Element {search_item} found at index {index}")
else:
    print("Element not found")

arr[0] = 15
print(arr)