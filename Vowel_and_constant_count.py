# Count Vowels and Consonants:
# ○ Question: Write a program to count the number of vowels and
# consonants in a given string.
# ○ Logic: Use loops and conditional statements to categorize characters.
# ○ Sample Input: "hello"
# ○ Expected Output: Vowels: 2, Consonants: 3

vowels = "AEIOUaeiou";
input = "hello";
num = 0;
const = 0;

for char in input:
    if char in vowels:
        num += 1;
    else:
        const += 1;
        
print("Vowels count : ",num);
print("Constant count : ",const);