# Problem statement - https://leetcode.com/problems/maximum-sum-circular-subarray/


"""
Complexity analysis:

1) Time complexity:

2) Space complexity: 
"""


"""
Analysis and Tricks:

"""


class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for item in A:
            curMax = max(curMax + item, item)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + item, item)
            minSum = min(minSum, curMin)
            total += item

        if maxSum > 0:
            # handles the case where maxSum is between circular elements
            # in that case maxsum is difference between total and min sum
            return max(maxSum, total - minSum)
        else:
            # if numbers in array are negative we want to only return the largest number i.e. smallest negative
            return maxSum



if __name__ == '__main__':

    findSum = Solution()

    # Test Case 1
    assert findSum.maxSubarraySumCircular([1,-2,3,-2]) == 3

    # Test Case 2
    assert findSum.maxSubarraySumCircular([5,-3,5]) == 10

    # Test Case 3
    assert findSum.maxSubarraySumCircular([3,-1,2,-1]) == 4

    # Test Case 4
    assert findSum.maxSubarraySumCircular([3,-2,2,-3]) == 3

    # Test Case 5
    assert findSum.maxSubarraySumCircular([-2,-3,-1]) == -1