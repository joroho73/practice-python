# String Lists
# Ask the user for a string and print out whether this string is a palindrome or not. 

str = input("enter a string: ")

print(str[len(str):0:-1])
print(str[0:len(str)])
print(list(reversed(str)))