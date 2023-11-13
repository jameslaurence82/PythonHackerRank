"""
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of 
all the plants with distinct heights in her greenhouse.

Formula used:
Average = Sum of Distinct Heights / Total Number of Distinct Heights

average has the following parameters:
int arr: an array of integers
Returns:
float: the resulting float value rounded to 3 places after the decimal
Input Format
The first line contains the integer N, the size of arr.
The second line contains the N space-separated integers arr[i]
"""

# Pseudocode
# define average function
# # N is the input for number of inputs taken 
# arr is the list for the input of plant heights
# arr needs to be set as set to have unique values only per question requirements
# Average function will take the array input values and divide it by the sum of the array elements
# displays the average with 3 decimal places


def average(array):
    array = set(array) # turns list into set for unique values only
    # print(array) # to see what values were passed into the function
    # print(type(array)) # to see if data type of array is a set
    arr_sum = 0 # forget to declare the variable sum being caluctated
    for i in array: # loops through set elements to calculate the total element sum 
        arr_sum += i # adds each element to the arr_sum
    return (arr_sum/len(array)) # returns the average of the array elements to the main function

if __name__ == '__main__':
    n = int(input()) # the number of inputs should be used as a loop for the arr??? but it isn't in hackerrank requirements
    arr = list(map(int, input().split()))
    # print(n) # to see what the input is for n
    # print(arr) # to see what the input is for arr
    # print(type(arr)) # to see the data type of arr
    # result = average(arr) # this is from the question. I liked the f string version i used
    # print(result)
    print(f"{average(arr):.3f}") # display average result with 3 decimal places 