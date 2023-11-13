"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.
"""

if __name__ == '__main__':
    n = int(input())
    # input of arr can be multiple integers and needs to be split
    arr = map(int, input().split())
    # trying to understand what arr is
    # print(list(arr))
    # print(type(arr))
    
# I am unsure of how to proceed

# take input of n <-- don't know what happens to this

# map cannot be Cast as a set so it must be cast to list 
    arr_list = list(arr)
# cast the list as a set to remove duplicates
    arr_set = set(arr_list)
# cast the set as a list to sort the list
    arr_sorted = sorted(list(arr_set))
    
# print the second to last element of the list for the runner up score
    print(arr_sorted[-2])
