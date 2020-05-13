# Problem statement - https://leetcode.com/problems/remove-k-digits/


"""
Complexity analysis:

1) Time complexity: O(log n) since we are using a form of binary search.

2) Space complexity: O(1) since no additional memory is used
"""


"""
Analysis and Tricks:

"""



class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []
        print("We need to remove {} digits from {}".format(k, num))
        for digit in num:
            print("Digit is: ", digit)
            while k and out and out[-1] > digit:
                print("Last item in out is: ",out[-1])
                out.pop()
                k -= 1
            out.append(digit)
        print("Final out is: ", out)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


if __name__ == '__main__':

    smallest = Solution()

    # test case 1
    assert smallest.removeKdigits(num = "1432219", k = 3) == "1219"

    # test case 2
    assert smallest.removeKdigits(num = "10200", k = 1) == "200"

    # test case 3
    assert smallest.removeKdigits(num = "10", k = 2) == "0"

    # test case 4
    assert smallest.removeKdigits(num = "12345678", k = 3) == "12345"