# Problem statement - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Logic:
Save the first item as the root of the tree
Push this root to the stack
For all other values in the input list do the following:
* if current value is less than value of item on top of stack:
    wrap it into a node and make the left child of top stack item
    push this new node to top of stack

* else
    while stack is not empty and current value is greater than top of stack:
        keep popping top of stack and saving it
    eventually we will encounter an item from stack top whose value is greater than curr item
    we need to wrap our curr item into a node and attach it to the right of the last item
    push this new node to top of stack
"""
# tl;dr: We need to regenerate the binary tree based on the preorder traversal data given to us
class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and value > stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root


"""
Alternate solution:
The function is given a bound i.e. the maximum value it will handle
Basically `bound` is value of the subtree root for each recursive call
Left recursion handles elements less than node.val
Right recursion will handle all other elements (Basically we don't need to worry about bound for right recursion)

Time complexity is O(n) because the recursive call is made same number of times as length of the input array
"""
# class Solution:
#     i = 0
#     def bstFromPreorder(self, A, bound=float('inf')):
#         if self.i == len(A) or A[self.i] > bound:
#             return None
#         root = TreeNode(A[self.i])
#         self.i += 1
#         root.left = self.bstFromPreorder(A, root.val)
#         root.right = self.bstFromPreorder(A, bound)
#         return root


if __name__ == '__main__':

    bstGenesis = Solution()

    # Test Case 1
    result = bstGenesis.bstFromPreorder([8, 5, 1, 7, 10, 12])
    print(result)
    print([8, 5, 10, 1, 7, None, 12])
     