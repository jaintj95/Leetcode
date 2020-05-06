# Problem statement - https://leetcode.com/problems/number-complement/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        
        while i <= num:
            i = i << 1
            
        print(i)
        print(i - 1)
        # ^ => Binary XOR
        return (i - 1) ^ num


if __name__ == '__main__':

    comp = Solution()

    # Test Case 1
    assert comp.findComplement(5) == 2

    # Test Case 2
    assert comp.findComplement(1) == 0

    # Test Case 3
    assert comp.findComplement(7) == 0