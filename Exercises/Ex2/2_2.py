# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]


import numpy as np 

# Input arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

# Use np.in1d to check if elements of array1 are in array2
result = np.isin(array1, array2)
print(f"Array1: {array1}")
print(f"Array2: {array2}")
print(f"Result (elements of array1 in array2): {result}")