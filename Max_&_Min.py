# Find the Maximum and Minimum Elements:
# ○ Question: Write a function to find the maximum and minimum
# elements in an array.
# ○ Logic: Iterate through the array, updating the maximum and minimum
# as you go.
# ○ Sample Input: [5, 3, 9, 2, 8]
# ○ Expected Output: Maximum: 9, Minimum: 2

arr = [5, 3, 9, 2, 8];
max = -2**31
min = 2**31 - 1

for i in arr:
    if (i >= max):
        max = i;
    elif (i < min):
        min = i;
        
print(max)
print(min)