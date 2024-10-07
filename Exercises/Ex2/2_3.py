# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
import numpy as np

# Input array
a = np.array([1, 6, 4, 8, 9, -4, -2, 11])

max_index = min_index = 0
for i in range(0, len(a)):
    if a[i] > a[max_index]: max_index = i
    if a[i] < a[min_index]: min_index = i

print(f'max_index: {max_index}, a[max_index] = {a[max_index]}')
print(f'min_index: {min_index}, a[min_index] = {a[min_index]}')

