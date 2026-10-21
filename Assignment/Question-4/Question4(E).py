# e) Check whether a character or substring exists using in and not in.

a=["hello world","python","programming","language","javascript"]
b=["java","c++","ruby","php"]


for string in a:
    if "a" in string:
        print(f"The character 'a' exists in the string: {string}")
    else:
        print("The character 'a' not found")


for string in b:
        if "ruby" in string:
            print(f"The substring 'ruby' exists in the string: {string}")
        else:
            print("The substring 'ruby' not found")
            