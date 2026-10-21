# e) Demonstrate string immutability by attempting to modify a character through
# indexing, and explain why the operation is not permitted.


a="Python is a programming language"
a[0]="p" #TypeError because string immutability 

print(a)