"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
Hacker Rank - List Comprehensions
You are given three integers x,y and z representing the dimensions of a cuboid along with an n
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is
not equal to n. Use list comprehensions rather than multiple loops
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Should i have known not to use [x,y,z] at the start of my list comprehension? and to use [i,j,k]????
    results = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i+j+k) != n]
    print(results)
    #gives the hacker rank answer
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
This is my trial attempts
"""
# Using inputs 1, 1, 1, 2

# September 21st attempts
#My Logic?????????????????????
# results = []
# for i in range(x):
#     for j in range(y):
#         for k in range(z):
#             results.append((i, j, k))
# print(results)
# creates this ??????????????????????
# [(0, 0, 0)]

# ChatGPT logic?????????????????
# x, y, z, n = 2, 2, 2, 2  # Replace these values with your input
# coordinates = [(i, j, k) for i in range(x) for j in range(y) for k in range(z) if (i + j + k) != n]
# print(coordinates)


# docs.python.org 
# this expression 
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# creates this 
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#results = [[i,j,k] for i in [x,y,z] for j in [x,y,z] for k in [x,y,z] if (i+j+k) != n]
#print(results)
# give this ??????????????
# [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], 
# [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], 
# [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

# results = [[i,j,k] for i in [x] for j in [y] for k in [z] if (i+j+k) != n]
# print(results)
# gives this??????????????????????
#[[1, 1, 1]]

# results = [[i,j,k] for i in range[x] for j in range[y] for k in range[z] if (i+j+k) != n]
# print(results)
# GIVES THIS????????????
#Traceback (most recent call last):
#   File "e:\4-Data Analytics Fall 2023\DBAS3018 - Data Movement and Integration\Demo\listcomprehension.py", line 42, in <module>
#     results = [[i,j,k] for i in range[x] for j in range[y] for k in range[z] if (i+j+k) != n]
#                                 ~~~~~^^^
# TypeError: type 'range' is not subscriptable
# PS E:\4-Data Analytics Fall 2023\DBAS3018 - Data Movement and Integration\Demo>

# September 24th attempts
# results.append([[i,j,k] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n])
# print(results)
# gives this?????
# Traceback (most recent call last):
#   File "d:\4-Data Analytics Fall 2023\DBAS3018 - Data Movement and Integration\Assignments\Assignment 2\assignment-2-jameslaurence82\listcomprehension.py", line 58, in <module>
#     results.append([[i,j,k] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n])
# NameError: name 'results' is not defined

# results = (for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n)
# print(results)
#     results = (for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n)
#                ^^^
# SyntaxError: invalid syntax

# results = ([] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n)
# print(results)
# # gives this?????
# <generator object <genexpr> at 0x00000178F2648040>

# results = [[i,j,k] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k) != n]
# print(results)
# gives this????
# [[2, 2, 2]]

# results = [[x,y,z] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k != n)]
# print(results)
# # gives this????
# [[1, 1, 1]]

# From reading List Comprehesion and Genertors in a Intermediate Python book, i saw the use of the colon. Thought that was was the issue.
# Still doesn't work
# results = [[x,y,z] for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k != n)]
# print(results)
# giuves this???
    # results = ([x,y,z]:, for i in [x + 1] for j in [y + 1] for k in [z + 1] if (i+j+k != n))

# Additional Attempts Sept 26th. back to basic loop
#     results = []
#     for i in range(x):
#         for j in range(y):
#             for k in range(z):
#                 if (i+j+k) != n:
#                     results.append((i, j, k))
#     print(results) 
# # give this???????
# # [(0, 0, 0)]

# Additional Attempts Sept 26th. back to basic loop updated
    # results = [] # creates empty list
    # for i in range(x+1): # i didn't understand that i had to add +1 to make the loop iterate to be the value of i
    #     for j in range(y+1): # i didn't understand that i had to add +1 to make the loop iterate to be the value of j
    #         for k in range(z+1): # i didn't understand that i had to add +1 to make the loop iterate to be the value of k
    #             if (i+j+k) != n: # if condition that prevents printing  (i+j+k) to new list if the value is equal to n
    #                 results.append([i, j, k])
    # print(results) # prints the new list
    # gives what is listed in hacker rank 
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
    
    # results = [[x,y,z] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i+j+k) != n]
    # print(results)
    # gives this????????
    # [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    
    # Should i have known not to use [x,y,z] at the start of my list comprehension? and to use [i,j,k]????
    # results = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i+j+k) != n]
    # print(results)
    # #gives the hacker rank answer
    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]