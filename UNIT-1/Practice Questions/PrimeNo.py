# write a python program for printing prime number upto n. n>100 take the input from user
n = int(input("Enter a number greater than 100: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)