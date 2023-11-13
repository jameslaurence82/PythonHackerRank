"""
https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
You are given a space separated list of nine integers. 
Your task is to convert this list into a 3X3 NumPy array using shape/reshape.
"""

# psuedocode
# user inputs list of integers
# user specifies the array shape the list needs to become
# prints the new array

import numpy as np

# input for np.array as 1 dimension
list_array = np.array([input().strip().split(" ")], int)
# input for new dimensions for np.array <------ this works when not on hacker rank
# shape_size = tuple(map(int, input().strip().split(" ")))
# hardcoded the new array dimension as HackerRank wanted it. 
shape_size = (3,3)

# Test Prints
print() # line gap
print(f"User Inputted array dtype is: {type(list_array)}")
print(f"User Inputted array shape is: {list_array.shape}")
print(f"The hardcoded array reshape value dtype: {type(shape_size)}")
print(f"The hardcoded array reshape is: {shape_size}")
print() # line gap

# reshape the list_array to new dimension
new_array = list_array.reshape(shape_size)

# print the new dimensioned array
print("Type and Shape of new array")
print(type(new_array))
print(new_array.shape)
print(f"\nReshaped array:\n {new_array}")