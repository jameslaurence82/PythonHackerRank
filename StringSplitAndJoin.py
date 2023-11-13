"""
String Split and Join
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

"""

# Pseudo code
# line input will take a string provided by the user
# split the string on a " " (space) delimiter
# join the strings with a dash
# print the result


def split_and_join(line):
    line = line.split() # uses the split function to separate str into list based on whitespace
    # print(line) # checking the function input
    # print(type(line)) # checking the type of function input
    # line = line.join("-") # error with syntax
    return "-".join(line) # uses the join function to join the list with a dash when being returned from the function

if __name__ == '__main__':
    line = input()
    # print(line) # checking the input
    # print(type(line)) # checking the type of input
    result = split_and_join(line)
    print(result)