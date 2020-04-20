# Problem statement - https://leetcode.com/problems/contiguous-array/
# Elegant solution - https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation

"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

class Solution:
    def findMaxLength(self, nums) -> int:
        count = 0
        max_length=0
        
        table = {0: 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in table:
                max_length = max(max_length, index - table[count])
            else:
                table[count] = index
        
        return max_length






if __name__ == '__main__':

    contArr = Solution()

    assert(contArr.findMaxLength([0,1]) == 2)

    assert(contArr.findMaxLength([0, 1, 0]) == 2)

    assert(contArr.findMaxLength([1, 1, 1, 0, 0]) == 4)

    assert(contArr.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]) == 4)

    assert(contArr.findMaxLength([0, 1, 1, 1, 0, 1, 1, 0]) == 4)

    assert(contArr.findMaxLength([1, 1, 1, 0, 0, 1, 1, 0]) == 6)


    ## Edge cases
    assert(contArr.findMaxLength([]) == 0)

    assert(contArr.findMaxLength([1]) == 0)

    assert(contArr.findMaxLength([0]) == 0)