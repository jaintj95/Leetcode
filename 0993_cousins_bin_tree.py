# Problem statement - https://leetcode.com/problems/cousins-in-binary-tree/


"""
Complexity analysis:

1) Time complexity: O(n) where n is the number of nodes in the binary tree 
            (since we are using deque time-complexity of queue operations is O(1))

2) Space complexity: 
"""


from collections import defaultdict
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = defaultdict(list)
        queue = deque([(root,0,0)])
        
        while queue:
            node,level,parent = queue.popleft()
            nodes[node.val] = [level,parent]
            if node.left:
                queue.append((node.left,level+1,node.val))
            if node.right:
                queue.append((node.right,level+1,node.val))
                
        if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
            return True
        
        return False
        