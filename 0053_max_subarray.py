# Problem statement - https://leetcode.com/problems/maximum-subarray


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


def maxSubArray(nums): 
    for i in range(1,len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    return max(nums)


if __name__ == "__main__":

    out = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(out)