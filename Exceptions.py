"""
https://www.hackerrank.com/challenges/exceptions/problem
You are given two values a and b.
Perform integer division and print a/b.
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.
Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code
"""
# Try Except Layout
#Try
    #problem logic body
#Except *exception name* as Alias
    #exception body


# try: <- this is in the wrong location of code
    # user input to set number of test cases for a and b
T = int(input())
# for loop to iterate through the number of test cases
for i in range(T):
    try:
    # a,b = int(input().split()) <- can't split int() has to be string
        a,b = input().split() # taking split inputs as string
        print(int(int(a)/int(b))) # print the integer division of a and b
    # print (f"a,b value is {a,b}") # display values <- for testing
    # print (f"T value is {T}") # display values <- for testing
    
    except ZeroDivisionError as ZDE: # except clause for ZeroDivisionError
        # prints error message if b is equal to 0
        print("Error Code: integer division or modulo by zero") # custom error message based on Hackerrank code to pass submission
        # print(f"Error Code: {ZDE}") <- this python error message was unaccepted by hackerrank
        # break <- break can be used to stop the loop when the except error happens (if required)

    except ValueError as VE: # except clause for ValueError
        # prints error message if b is not an integer
        #print(f"Error Code: Value Error - Integer required for input, '{b}' is not valid") <- custom error message
        print(f"Error Code: {VE}") # <- standard python error message for value error 