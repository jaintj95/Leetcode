# Problem Statement - https://leetcode.com/problems/move-zeroes/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ##start_idx = 0
    counts = nums.count(0)
    print(counts)
    for j in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

def test(*test_lists):
    print(test_lists)
    for nums in test_lists:
        print('Before:')
        print(nums)
        moveZeroes(nums)
        print('After moving zeroes')
        print(nums)


if __name__ == "__main__":
    list1 = [0, 5]
    list2 = [4, 0]
    list3 = [0, 0, 1, 3]
    list4 = [2, 7, 0, 0]

    list5 = [0, 1, 0, 2]
    list6 = [0, 1, 2, 0]
    list7 = [1, 0, 0, 2]
    list8 = [1, 0, 2, 0]

    list9 = [0,1,0,3,12]

    test(list1, list2, list3, list4, list5, list6, list7, list8, list9)