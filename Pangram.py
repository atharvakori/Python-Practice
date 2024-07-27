# Check for Pangram:
# ○ Question: Write a program to check if a given string is a pangram
# (contains all letters of the alphabet).
# ○ Logic: Use loops to check if all letters are present.
# ○ Sample Input: "The quick brown fox jumps over the lazy dog."
# ○ Expected Output: Pangram

alpha = set("abcdefghijklmnopqrstuvwxyz");
char = set("The quick brown fox jumps over the lazy dog.");

flag = alpha.issubset(char);

if(flag):
    print("Pangram");
else:
    print("Not Pangram");