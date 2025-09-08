# Divsors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("give me a number: "))
b = []

for divisor in range(1, num + 1):
    if num % divisor == 0:
        b.append(divisor)

print(b)