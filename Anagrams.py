# Check for Anagrams:
# ○ Question: Write a program to check if two strings are anagrams of
# each other.
# ○ Logic: Check if the character counts in both strings are the same.
# ○ Sample Input: "listen" and "silent"
# ○ Expected Output: Anagrams


in1 = "listen"
in2 = "silent";

flag = 1;

if(len(in1) != len(in2)):
    flag = 0;
else:
    for char in in1:
        if char not in in2:
            flag = 0;
            break;
            
if(flag):
    print("Anagrams");
else:
    print("Not Anagrams");