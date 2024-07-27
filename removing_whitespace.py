# Remove White Spaces:
# ○ Question: Write a program to remove white spaces from a string.
# ○ Logic: Use loops to remove spaces or use a regular expression.
# ○ Sample Input: "hello world"
# ○ Expected Output: "helloworld"

str = "hello world";
result = "";

for char in str:
    if char != " ":
        result += char;

print(result)