# Problem statement - https://leetcode.com/problems/palindrome-number/

def isPalindrome(x):
    strVal = str(x)
    
    reverse = ''
    for item in strVal[::-1]:
        reverse += item
        
    return reverse == strVal
        