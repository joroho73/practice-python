# String Lists
# Ask the user for a string and print out whether this string is a palindrome or not. 

st = input("enter a string: ")

# using reversed
rev = "".join(reversed(st))
if st == rev:
    print(f"{st} and {rev} are palindromes!")
else:
    print(f"{st} is not a palinrome.")

# using slicing
rev1 = st[::-1]
if st == rev1:
    print(f"{st} and {rev1} are palindromes!")
else:
    print(f"{st} is not a palinrome.")