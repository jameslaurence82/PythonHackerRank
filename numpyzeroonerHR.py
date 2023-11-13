"""
https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
You are given the shape of the array in the form of space-separated integers, 
each integer representing the size of different dimensions, your task is to 
print an array of the given shape and integer type using the tools numpy.zeros 
and numpy.ones.
Input Format
A single line containing the space-separated integers.
Constraints
1 <= each integer <= 3
"""

# pseudo code
# user input of array shape as integer
# shape input function to create zero 
# shape input function to create one

import numpy as np

def zeros(arr): # function to take np.array value to create np.zeros array
    arr1 = np.zeros(arr, dtype = np.int32)
    return arr1

def ones(arr): # function to take np.array value to create np.ones array
    arr2 = np.ones(arr, dtype = np.int32)
    return arr2

arr = input().strip().split(' ') # takes user input as list
new_arr = np.array(arr, dtype = np.int32) # converts string input to become np.array intergers 
# print(new_arr) # <- printing values of new array
# print(type(new_arr)) <-- check array datatype

print(zeros(new_arr)) # print function zeros to return np.zeros array
print(ones(new_arr)) # print function zeros to return np.ones array

