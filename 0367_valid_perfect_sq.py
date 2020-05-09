# Problem statement - https://leetcode.com/problems/valid-perfect-square/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

# Input number is a positive integer

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # newton root technique
        r = num
        while r*r > num:
            r = (r + num/r)//2
        
        return r*r == num
    

if __name__ == "__main__":

    checkSQ = Solution()

    # Test case 1
    assert checkSQ.isPerfectSquare(15) == False

    # Test case 2
    assert checkSQ.isPerfectSquare(16) == True