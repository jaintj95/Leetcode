# Problem statement - https://leetcode.com/problems/search-in-rotated-sorted-array/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

# Note - algorithm's runtime complexity must be in the order of O(log n)

class Solution:
    def search(self, nums, target: int) -> int:
        
        if nums is None or target is None:
            return
        
        return self.mod_binary_search(nums, target, 0, len(nums)-1)

    def mod_binary_search(self, nums, target, start_idx, end_idx):

        # if start_idx has crossed the end_idx while recursing, return -1
        if start_idx > end_idx:
            return -1

        mid_idx = (end_idx+start_idx) // 2

        if nums[mid_idx] == target:
            return mid_idx

        # check if right-half array is sorted
        if nums[mid_idx] <= nums[end_idx]:
            
            # if target lies in this range, use binary search to find it
            if nums[mid_idx] <= target <= nums[end_idx]:
                return self.mod_binary_search(nums, target, mid_idx+1, end_idx)

            else:
                return self.mod_binary_search(nums, target, start_idx, mid_idx-1)
        

        # if right-half is not sorted, left-half is definitely sorted
        else:
            # if target lies in range of values in left-half, use binary search
            if nums[start_idx] <= target <= nums[mid_idx]:
                return self.mod_binary_search(nums, target, start_idx, mid_idx-1)

            else:
                return self.mod_binary_search(nums, target, mid_idx+1, end_idx)
        
    # def mod_binary_search(self, nums, target, start_idx, end_idx):
    #     mid_idx = (end_idx + start_idx) // 2
    #     print(mid_idx)
    #     if nums[mid_idx] == target:
    #         return mid_idx

    #     elif nums[mid_idx] > target:
    #         if (nums[mid_idx] < nums[end_idx]):
    #             return self.mod_binary_search(nums, target, start_idx, mid_idx-1)
    #         else:
    #             return self.mod_binary_search(nums, target, mid_idx+1, end_idx)
        
    #     else:
    #         # nums[mid_idx] < target
    #         if (nums[mid_idx] < nums[start_idx]):
    #             return self.mod_binary_search(nums, target, start_idx, mid_idx-1)
    #         else:
    #             return self.mod_binary_search(nums, target, mid_idx+1, end_idx)


if __name__ == '__main__':
    
    rot_arr = Solution()

    # Test Case 1
    assert rot_arr.search(nums = [4,5,6,7,0,1,2], target = 0) == 4

    # Test Case 2
    assert rot_arr.search(nums = [4,5,6,7,0,1,2], target = 3) == -1

    # Test Case 3
    assert rot_arr.search(nums = [2,4,5,6,7,8,0,1], target = 0) == 6

    # Test Case 4
    assert rot_arr.search(nums = [5,6,7,8,0,1,2,4], target = 4) == 7