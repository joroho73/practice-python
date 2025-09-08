# Divsors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("give me a number: "))
a = range(1, num + 1)
b = []

for divisor in a:
    if num % divisor == 0:
        b.append(divisor)

print(b)