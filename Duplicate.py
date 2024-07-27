# Remove Duplicates from Unsorted Array:
# ○ Question: Write a function to remove duplicates from an unsorted
# array.
# ○ Logic: Use a hash set to keep track of unique elements as you iterate
# through the array.
# ○ Sample Input: [3, 2, 3, 1, 2, 4]
# ○ Expected Output: [3, 2, 1, 4]

arr = [3, 2, 3, 1, 2, 4];

check = set();
result = [];

for i in arr:
    if i not in check:
        check.add(i);
        result.append(i);
        
print(result)