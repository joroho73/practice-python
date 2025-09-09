## List Comprehensions 

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# standard way
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# create empty list
b = []

# iterate through a and add item to b if it is even
# use % to determine if they are even

for item in a:
    if item % 2 == 0:
        b.append(item)
print(b)