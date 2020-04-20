# Problem statement - https://leetcode.com/problems/product-of-array-except-self/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

# Instructions: Solve it without division and in O(n).

class Solution:
    def productExceptSelf(self, nums):
        
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

"""
Logic ->

1st time going through the array, it's beginning to the end. 
p keeps a running total of the product, and each element will equal 
the running total of the products of the elements that came before. 
Then the 2nd time going through the array, you're doing the same process, 
but backwards, finishing off the result by multiplying the elements that came after.

example: [1,2,3,4]. let's say initially, your output is [1, 1, 1, 1] and p = 1.

Loop 1:
i = 0, your output becomes [1*1, 1, 1, 1] and p = p * 1 (1)
i = 1, your output becomes [1, 1*1, 1, 1] and p = p * 2 (2)
i = 2, your output becomes [1, 1, 1*2, 1] and p = p * 3 (6)
i = 3, your output becomes [1, 1, 2, 6]

Loop 2 (p = 1 again)
i = 3, your output becomes [1, 1, 2, 6*1] and p = p * 4 (4)
i = 2, your output becomes [1, 1, 2*4, 6] and p = p * 3 (12)
i = 1, your output becomes [1, 1*12, 8, 6] and p = p * 2 (24)

Final result: [24, 12, 8, 6]

"""


if __name__ == "__main__":

    prod = Solution()

    # Test Case 1
    assert prod.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    # Test Case 2
    assert prod.productExceptSelf([7, 2, 5]) == [10, 35, 14]

    # Test Case 3 - Duplicate values
    assert prod.productExceptSelf([4, 7, 7, 1]) == [49, 28, 28, 196]