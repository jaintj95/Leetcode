# Problem statement - 

## Temporary URL - https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def stringShift(self, s: str, shift) -> str:

        print("Input string: {}".format(s))

        total_shift = 0
        # shift matrix is a list of lists e.g. [[0,1],[1,2]] -> [[left_shift, 1 unit], [right_shift, 2 units]]
        for indi_shift in shift:
            if indi_shift[0] == 0:
                total_shift -= indi_shift[1]
            
            else:
                total_shift += indi_shift[1]

        print("Total shift: {}".format(total_shift))

        total_shift %= len(s)

        print("Total shift if len > s: {}".format(total_shift))

        final_str = s[-total_shift:] + s[:-total_shift]

        print("Out string: {}".format(final_str))

        return final_str


# class SolutionOld:
#     def stringShift(self, s: str, shift) -> str:

#         total_shift = 0
#         # shift matrix is a list of lists e.g. [[0,1],[1,2]] -> [[left_shift, 1 unit], [right_shift, 2 units]]
#         for indi_shift in shift:
#             if indi_shift[0] == 0:
#                 total_shift -= indi_shift[1]
            
#             else:
#                 total_shift += indi_shift[1]

#         print("Total shift: {}".format(total_shift))

#         if total_shift == 0:
#             return s

#         elif total_shift < 0:
#             total_shift = 0 - total_shift
#             if total_shift >= len(s):
#                 total_shift %= len(s)
#             final_str = s[total_shift:] + s[:total_shift]
#             print(final_str)

#         elif total_shift > 0:
#             if total_shift >= len(s):
#                 total_shift %= len(s)
#             final_str = s[-total_shift:] + s[:-total_shift]
#             print(final_str)

#         return final_str

"""
Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
"""


if __name__ == "__main__":

    shifter = Solution()

    # Test Case 1
    # Input -> "abc"
    # Shift -> [[0,1],[1,2]]
    # Output -> "cab"
    # Explanation ->
                    ## [0,1] means shift to left by 1. "abc" -> "bca"
                    ## [1,2] means shift to right by 2. "bca" -> "cab"
    assert(shifter.stringShift(s = "abc", shift = [[0,1],[1,2]]) == "cab")

    # Test Case 2
    # Input -> "abcdefg"
    # Shift -> [[1,1],[1,1],[0,2],[1,3]]
    # Output -> "efgabcd"
    # Explanation ->
                    ## [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
                    ## [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
                    ## [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
                    ## [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
    assert(shifter.stringShift(s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]) == "efgabcd")

    # Test Case 3
    # Input -> "wpdhhcj"
    # Shift -> [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
    # Output -> "hcjwpdh"

    assert(shifter.stringShift(s = "wpdhhcj", shift = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]) == "hcjwpdh")


    # Test Case 4
    # Input -> "xqgwkiqpif"
    # Shift -> [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
    # Output -> "qpifxqgwki"

    assert(shifter.stringShift(s = "xqgwkiqpif", shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]) == "qpifxqgwki")


