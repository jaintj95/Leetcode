# Problem statement - https://leetcode.com/problems/bitwise-and-of-numbers-range/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while(m != n):
            m >>= 1
            n >>= 1
            i += 1 
      
        return m << i  


if __name__ == '__main__':

    bitwise = Solution()

    # Test case 1
    assert bitwise.rangeBitwiseAnd(5,7) == 4

    # Test case 2
    assert bitwise.rangeBitwiseAnd(0,1) == 0