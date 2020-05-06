# Problem statement - 

## Temporary URL - https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = []

    def showFirstUnique(self) -> int:
        return -1

    def add(self, value: int) -> None:
        pass


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


if __name__ == "__main__":

    # Test Case 1
    fUniq = FirstUnique([2, 3, 5])
    assert fUniq.showFirstUnique() == 2
    fUniq.add(5)
    assert fUniq.showFirstUnique() == 2
    fUniq.add(2)
    assert fUniq.showFirstUnique() == 3
    fUniq.add(3)
    assert fUniq.showFirstUnique() == -1


    # Test Case 2
    fUniq = FirstUnique([7,7,7,7,7,7])
    assert fUniq.showFirstUnique() == -1
    fUniq.add(7)
    fUniq.add(3)
    fUniq.add(3)
    fUniq.add(7)
    fUniq.add(17)
    assert fUniq.showFirstUnique() == 17


    # Test case 3
    fUniq = FirstUnique([809])
    assert fUniq.showFirstUnique() == 809
    fUniq.add(809)
    assert fUniq.showFirstUnique() == -1