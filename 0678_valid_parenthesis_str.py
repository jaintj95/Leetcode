# Problem statement - https://leetcode.com/problems/valid-parenthesis-string/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack 1, try to test all the ( and * can balance all the )
        S=[]        
        # go through s from left to right
        for x in s:
            if x=='(' or x=='*':
                S.append(x)
            else:
                if len(S)>0:
                    S.pop()
                else:
                    return False        # this means left ( is not enough

        # stack 2, try to test all the ) and * can balance all the (
        S=[]        
        # go through s from right to left
        for x in s[::-1]:
            if x==')' or x=='*':
                S.append(x)
            else:
                if len(S)>0:
                    S.pop()
                else:
                    return False        # this means right ) is not enough

        return True

# class SolutionOld:
        # print(s)
        # stack = []
        # star = []

        # for char in s:
        #     print('Stack: {}'.format(stack))
        #     print('astra: {}'.format(star))
        #     if char == '(':
        #         stack.append(char)
        #     elif char == '*':
        #         star.append(char)
        #     elif char == ')' and len(stack) > 0:
        #         popped = stack.pop()
        #         # if popped == '(':
        #         continue
        #     elif char == ')' and len(star) > 0:
        #         popped = star.pop()
        #         # if popped == '(':
        #         continue
        #     else:
        #         return False

        # print('Here')
        # print(stack)
        # print(star)

        # if (len(stack) == 0):
        #     return True

        # elif len(stack) <= len(star):
        #     return True

        # return False


if __name__ == '__main__':

    strChecker = Solution()

    # # Test Case 0
    # assert strChecker.checkValidString("") == True

    # # Test Case 1
    # assert strChecker.checkValidString("()") == True

    # # Test Case 2
    # assert strChecker.checkValidString("(*)") == True

    # # Test Case 3
    # assert strChecker.checkValidString("(*))") == True

    # # Test Case 4
    # assert strChecker.checkValidString("((*)") == True

    # # Test Case 5
    # assert strChecker.checkValidString("*") == True

    # # Test Case 6
    # assert strChecker.checkValidString("())") == False

    # # Test Case 7
    # assert strChecker.checkValidString("(*()") == True

    # # Test Case 8
    # assert strChecker.checkValidString("(((******))") == True

    # Test Case 9
    assert strChecker.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*") == False
    