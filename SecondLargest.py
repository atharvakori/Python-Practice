# Find the Second Largest Element:
# ○ Question: Find the second largest element in an array.
# ○ Logic: Initialize two variables to store the largest and second-largest
# elements and iterate through the array.
# ○ Sample Input: [7, 3, 9, 2, 8]
# ○ Expected Output: Second Largest: 8

arr = [7, 3, 9, 2, 8];
largest = sec_largest = -2**31
for i in arr:
    if(i > largest):
        sec_largest = largest;
        largest = i;
    elif(i > sec_largest and i != largest):
        sec_largest = i;
        
print(sec_largest)