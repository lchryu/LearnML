"""
- Ex1: Write a NumPy program to reverse an array (first element becomes last).
- Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
"""
import numpy as np

# Input array as a string
user_inp = "[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]"
print(f"Original array: {user_inp}")

user_inp = user_inp.strip("[]")

# Step 2: Split elements (assuming they are separated by spaces)
elements = user_inp.split(" ")

# Step 3: Convert each element from string to an integer
array = np.array([int(e) for e in elements])

# Use two-pointer technique to reverse the array
left = 0
right = len(array) - 1
while (left < right):
    # Swap elements at positions left and right
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

print(f"Reversed array: {array}")