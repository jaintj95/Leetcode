# Problem statement - https://leetcode.com/problems/jump-game/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

# Start to end
class Solution:
    def canJump(self, nums) -> bool:
        max_idx_so_far = 0
        print(nums)
        for idx, num in enumerate(nums):
            print("idx: {}".format(idx))
            print("num: {}".format(num))
            print("max old: {}".format(max_idx_so_far))
            if idx > max_idx_so_far:
                return False
            max_idx_so_far = max(max_idx_so_far, idx+num)
            print("max new: {}".format(max_idx_so_far))
        return True


# Alternate backtracking strategy
class SolutionBack:
    def canJump(self, nums) -> bool:
        lastGoodIdx = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if (i + nums[i] >= lastGoodIdx):
                lastGoodIdx = i
            
        return lastGoodIdx == 0


if __name__ == '__main__':

    jumper = Solution()

    # Test Case 1
    # Input: [2,3,1,1,4]
    # Output: true
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    assert jumper.canJump([2,3,1,1,4]) == True


    # Test Case 2
    # Input: [3,2,1,0,4]
    # Output: false
    # Explanation: You will always arrive at index 3 no matter what. Its maximum
    #              jump length is 0, which makes it impossible to reach the last index.

    assert jumper.canJump([3,2,1,0,4]) == False


    ################################################################

    jumper2 = SolutionBack()

    # Test Case 1
    # Input: [2,3,1,1,4]
    # Output: true
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
    assert jumper2.canJump([2,3,1,1,4]) == True


    # Test Case 2
    # Input: [3,2,1,0,4]
    # Output: false
    # Explanation: You will always arrive at index 3 no matter what. Its maximum
    #              jump length is 0, which makes it impossible to reach the last index.

    assert jumper2.canJump([3,2,1,0,4]) == False