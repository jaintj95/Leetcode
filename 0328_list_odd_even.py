# Problem statement - https://leetcode.com/problems/odd-even-linked-list/


"""
Complexity analysis:

1) Time complexity: O(n) where n is the number of nodes in the list

2) Space complexity: O(1) besides creating two dummy nodes we do not use any additional space
"""


"""
Analysis and Tricks:
Basically we create two dummy nodes for odd and even list
Then we start attaching nodes to these dummy head nodes
Finally we connect the last node of the odd list to the first node of the even list


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)
        
        node = head
        
        while node:
            odd.next = node
            odd = odd.next

            even.next = node.next
            even = even.next
            
            node = node.next.next if even else None
            
        #connect last node of odd to first node of even 
        odd.next = dummy_even.next 
        
        return dummy_odd.next
        

