# Problem statement - https://leetcode.com/problems/single-element-in-a-sorted-array


"""
Complexity analysis:

1) Time complexity: O(log n) since we are using a form of binary search.

2) Space complexity: O(1) since no additional memory is used
"""

"""
Analysis and Tricks:

1) Input arrays will always will be odd in size because there's always one num that's missing a pair while others have a pair.
So, size is always odd

2) XORing a number with 1 decrements it by 1 and returns the previous even num if the org num is odd i.e. 5^1 = 4
While if the org num is even it increments it by 1 and returns the next odd num (obviously) i.e. 6^1 = 7
We can use this trick to find pairs.
"""

class Solution:
    def singleNonDuplicate(self, nums) -> int:
        
