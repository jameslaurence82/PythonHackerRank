import numpy as np
# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# You are given two integer arrays, a and b of dimensions n x m.
# Add (a + b), Subtract (a - b) , Multiply (a * b) ,Integer Division (a // b) <<-- floor_divide
# Modulus (a % b), # Power (a ** b)

# creation of nxm array dimension variables
print("\nEnter the Array Dimensions")
n,m = map(int, input().strip().split()) # map function to have n,m as integers for range statement
print("\nEnter the Elements for array a and array b")
# creation of array elements based on n array size
a = np.array([input().strip().split(" ") for elements in range(n)], int)
b = np.array([input().strip().split(" ") for elements in range(n)], int)

#Print values and types of n,m
print("\nPrinting User Array dimensions Input with type")
print(type(n), f" and {n}")
print(type(m), f" and {m}")


#printing user created arrays
print("\nPrinting User Array Input with type")
print(type(a), f"array value \n {a}")
print(type(b), f"array value \n {b}")

# processing arrays
addition = a+b # adding arrays
subtraction = (a-b) # subtracting arrays
multiplication = (a*b) # multiplying arrays
floor_division = (a//b)  # floor division of arrays
modulus = (a%b) # modulus division of arrays
power = (a**b) # power to arrays

#printing math results
print("\nOutput Array Mathematic Results")
print(addition)
print(subtraction)
print(multiplication)
print(floor_division)
print(modulus)
print(power)

