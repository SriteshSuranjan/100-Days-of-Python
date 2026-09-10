# MAP

# Function returning the cube values
# def cube(x):
#     return x * x * x

# print(cube(2))

# List of numbers
l =[1, 2, 3, 4, 5, 6, 7]

# newl = []
# for item in l:
#     newl.append(cube(item))

# Cube each number using map function
# newl = list(map(cube, l))
newl = list(map(lambda x: x * x * x, l))

# Print the cube numbers
print(newl)

# FILTER

# def filter_function(a):
    # return a > 2
# newnewl = list(filter(filter_function, l))
newnewl = list(filter(lambda x: x > 2, l))
print(newnewl)

# REDUCE

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# def mysum(x,y):
#     return x + y
# sum = reduce(mysum, numbers)

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)
