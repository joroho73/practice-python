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
for j in a:
    if j < 5:
        b.append(j)
print(b)

# 2. Write this in one line of Python.
c = []
#print([i for i in range(1, num+1) if num % i == 0])
#print([k for k in a if k < 5 c.append(k)]) < does not work

num = int(input("Give me a number: "))
d = []
for i in a:
    if i < num:
        d.append(i)
print(d)