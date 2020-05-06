# Problem statement - https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        n = len(arr)
        
        def visit(node, index):
            if index == n-1:
                if node is not None and node.val == arr[index]:
                    return node.left is None and node.right is None
                return False
            
            if node is None:
                return False
            
            if node.val == arr[index]:
                return visit(node.left, index+1) or visit(node.right, index+1)
            
            return False
        
        return visit(root, 0)


# if __name__ == "__main__":

#     checkTree = Solution()
#     #Test Case 1
#     assert checkTree.isValidSequence()