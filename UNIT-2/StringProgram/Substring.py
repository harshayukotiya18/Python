# Substring

text = "Programming";
sub = text[3:8]
print(sub)

text = "Learning Python";
if "Python" in text:
    print("Substring found!")

text = "Hello world";
substring = "world";
index = text.find(substring)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found.")


text = "Hello world";
substring = "world";
index = text.index(substring)
print(f"Found at index {index}")
