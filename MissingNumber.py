# Find Missing Number in Array:
# ○ Question: Given an array containing n distinct numbers taken from 0,
# 1, 2, ..., n, find the one that is missing from the array.
# ○ Logic: Calculate the expected sum of the series and subtract the sum
# of the array from it.
# ○ Sample Input: [0, 1, 3]
# ○ Expected Output: Missing Number: 2

arr = [0, 1, 3];
missing_sum = 0;
sum = 0;

for i in range(0,len(arr)):
    if(arr[i] != i):
        missing_sum += i;
    else:
        sum += i 

print(sum - missing_sum)