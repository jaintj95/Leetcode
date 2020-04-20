# Problem statement - https://leetcode.com/problems/min-stack/


"""
Complexity analysis:

1) Time complexity: N/A, as this was an Abstract Data Structure implementation and not an algorithm

2) Space complexity: N/A, as this was an Abstract Data Structure implementation and not an algorithm
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_item = None
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min_item = x
        
        else:
            if self.min_item > x:
                self.min_item = x

        self.stack.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_item:
            if len(self.stack) > 0:
                self.min_item = min(self.stack)

            else:
                self.min_item = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_item


if __name__ == '__main__':

    minStack = MinStack() 
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert (minStack.getMin() == -3)
    minStack.pop()
    assert (minStack.top() == 0)
    assert (minStack.getMin() == -2)