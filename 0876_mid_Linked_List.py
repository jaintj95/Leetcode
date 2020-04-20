# Problem statement - https://leetcode.com/problems/middle-of-the-linked-list/


"""
Complexity analysis:

1) Time complexity: O(n) => Since all the nodes in the list are traversed until the end, 
                            the time complexity is O(n), where n is the size of the list

2) Space complexity: O(1) => We are not using any additional space except for the space used by slow_link and fast_link
                            Hence, space complexity is O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        The function creates two links, one takes two steps at a time, while the other takes a single step
        If the fast stepper has reached None, then the location of slow stepper is the middle of the list
        """
        slow_link = head
        fast_link = slow_link
        
        if head.next is None:
            return head
        
        while fast_link:
            
            # I chose to use the EAFP principle here. 
            try:
                fast_link = fast_link.next.next
                slow_link = slow_link.next
            except:
                fast_link = fast_link.next
                break
                
        return slow_link


if __name__ == '__main__':


    middleFinder = Solution()

    # test1
    list1 = ListNode(1)
    result1 = None
    node = list1
    for item in [2,3,4,5]:
        node.next = ListNode(item)
        # save middle node reference to verify results
        if item == 3:
            result1 = node.next

        node = node.next

    assert (middleFinder.middleNode(list1) == result1) # Assert succeeds if function returns pointer to node with value 3


    # test2
    list2 = ListNode(1)
    result2 = None
    node = list2
    for item in [2,3,4,5,6]:
        node.next = ListNode(item)
        # save middle node reference to verify results
        if item == 4:
            result2 = node.next

        node = node.next

    assert (middleFinder.middleNode(list2) == result2) # Assert succeeds if function returns pointer to node with value 4
    

