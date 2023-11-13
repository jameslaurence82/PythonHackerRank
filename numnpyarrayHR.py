"""
https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
Input Format
A single line of input containing space separated numbers.
Output Format
Print the reverse NumPy array with type float.
Sample Input
1 2 3 4 -8 -10
"""
# Pseudocode
# user input list with split/strip function 
# use function to cast list in np.array and dtype as float
# print array in reverse order


import numpy

def arrays(arr):
    # takes user list, cast into float and numpy array
    arr1 = numpy.array(arr, dtype=numpy.float64)
    # reverse the order of the array
    
    return arr1[::-1]
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
print(arr) # display array created
print(type(arr)) # display array type
result = arrays(arr)
print(result)
print(type(result))