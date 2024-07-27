# Remove Duplicates from a String:
# ○ Question: Write a program to remove duplicate characters from a
# string.
# ○ Logic: Use a hash set or loops to track unique characters.
# ○ Sample Input: "programming"
# ○ Expected Output: "progamin"

str = "programming";

check = set();
str_arry = [];

for char in str:
    if char not in check:
        check.add(char);
        str_arry.append(char);
        
result = "".join(str_arry);

print(result);