# Write a function that will find power of a number.

def find_power(base, power):
    return base ** power

base = int(input('Enter base: '))
power = int(input('Enter power: '))
result = find_power(base, power)
print('Result =', result)