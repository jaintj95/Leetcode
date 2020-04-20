# Problem statement - https://leetcode.com/problems/palindrome-number/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


def isPalindrome(x):
    strVal = str(x)
    
    reverse = ''
    for item in strVal[::-1]:
        reverse += item
        
    return reverse == strVal
        