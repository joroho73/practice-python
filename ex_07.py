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
print("for item in a:\n    if item % 2 == 0:\n        b.append(item)")
print(b)

print("[x for x in a if x % 2 == 0]")
print([x for x in a if x % 2 == 0])

# explanaion https://medium.com/py-blog/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404
print("explanation: https://medium.com/py-blog/python-list-comprehensions-use-list-comprehension-to-replace-your-stupid-for-loop-and-if-else-9405acfa4404")


numbers = [1,2,3,4]
output = []
for i in numbers:
   if i%2 == 1:
      output.append(i)
print(numbers
      )
print(output)

output2 = [i for i in numbers if i%2 ==1 ] 
print(output2)
