# Problem statement - https://leetcode.com/problems/majority-element/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        comp = len(nums)//2

        countMap = defaultdict(int)
        
        for num in nums:
            countMap[num] += 1
            
            if countMap[num] > comp:
                return num
        