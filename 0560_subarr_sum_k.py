# Problem statement - https://leetcode.com/problems/subarray-sum-equals-k/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

class Solution:
    def subarraySum(self, nums, k: int) -> int:

        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        print(d)
        print(count)
        return(count)



if __name__ == '__main__':

    arrSum = Solution()

    # Test Case 1
    assert arrSum.subarraySum(nums = [1,1,1], k = 2) == 2

    # Test Case 2
    # [1,2,1,3] => [1,3,4,7]
    assert arrSum.subarraySum(nums = [1,2,1,3], k = 3) == 3

    # Test Case 3
    assert arrSum.subarraySum(nums = [1,4,0,1,2,2,5], k = 5) == 6