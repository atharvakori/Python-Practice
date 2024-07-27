# Check for Palindrome:
# ○ Question: Write a program to check if a given string is a palindrome.
# ○ Logic: Use loops to compare characters from the start and end of the
# string.
# ○ Sample Input: "racecar"
# ○ Expected Output: Palindrome

input = "racecar";
left = 0;
right = len(input)-1;
flag = 1;

while(left<right):
    if(input[left] != input[right]):
        flag = 0;
    left += 1;
    right -= 1;
        
if(flag):
    print("Palindrom");
else:
    print("Not Palindrom")