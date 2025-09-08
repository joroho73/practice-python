# List Less Than Ten
# Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.
print(a)
for i in a:
    if i < 5: print(i)
   
# Extras
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 
# from this list in it and print out this new list.

b = [] 
for i in a:
    if i < 5:
        b.append(i)
print(b)

# 2. Write this in one line of Python.
# p = [q.index(v) if v in q else 99999 for v in vm]
# b2 = [a.index(j) if j < 5 else b2.append(j)]
# 3. Ask the us er for a number and return a list that contains only elements from the original list
# that are smaller than that number given by the user.

num = int(input("Give me a number: "))
c = []
for i in a:
    if i < num:
        c.append(i)
print(c)