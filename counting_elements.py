# Problem statement - https://leetcode.com/problems/

## Temporary URL - https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


def countElements(arr) -> int:
    """
    
    """
    result = 0
    stat_dict = {} # (key -> item: value -> [item_count, Bool: True if x+1 is present])

    for item in arr:
        if item not in stat_dict:
            stat_dict[item] = [1, False]
        elif item in stat_dict:
            stat_dict[item][0] = stat_dict[item][0] + 1

        if (item-1) in stat_dict:
            stat_dict[item-1][1] = True

        if (item+1) in stat_dict:
            stat_dict[item][1] = True 

    print(stat_dict)
    for key, value in stat_dict.items():
        if value[1]:
            result += value[0]

    return result

if __name__ == "__main__":

    assert (countElements([1,2,3]) == 2)
    assert (countElements([1,1,3,3,5,5,7,7]) == 0)
    assert (countElements([1,3,2,3,5,0]) == 3)
    assert (countElements([1,1,2,2]) == 2)