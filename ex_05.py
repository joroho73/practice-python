# List Overlap

# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("first version")
out1 = []
for i in a:
    for j in b:
        if i == j:
            out1.append(i)
out1 = list(set(out1))
print(out1)

print("version using 'in'")

out2 = []
for i in a:
    if i in b:
        out2.append(i)
print(list(set(out2)))

