# Problem statement - https://leetcode.com/problems/binary-tree-maximum-path-sum/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.max = float('-inf')
        
        def util(node):
            if not node:
                return 0
            
            left = util(node.left)
            
            right = util(node.right)
            
            self.max = max(self.max, node.val,\
                          node.val + left, node.val + right, \
                          node.val + left + right)
            
            return max(node.val, node.val + max(left, right))
        
        
        util(root)
        
        return self.max