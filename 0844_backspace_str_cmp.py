# Problem statement - https://leetcode.com/problems/backspace-string-compare/


"""
Complexity analysis:

1) Time complexity: O(M + N) => Since we traverse through the chars in each string, 
                            the time complexity is O(M + N), where M and N are lengths of input strings respectively.

2) Space complexity: O(M + N) => We are using  additional space by storing individual characters in a list
                            Hence, space complexity is O(M + N) where M and N are the lenghts of input strings respectively.
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        print('String S is: {}'.format(S))
        print('String T is: {}'.format(T))

        # list_S = ['' for _ in range(len(S))]
        # list_T = ['' for _ in range(len(T))]

        list_S = []
        list_T = []

        # idx_S = 0
        for char in S:
            if char!='#':
                list_S.append(char)
            elif list_S:
                    list_S.pop()

        # idx_T = 0
        for char in T:
            if char!='#':
                list_T.append(char)
            elif list_T:
                    list_T.pop()

        print('After parsing string S characters are: {}'.format(list_S))
        print('After parsing string T characters are: {}'.format(list_T))

        if len(list_S) != len(list_T):
            print("Strings don't match")
            return False

        for char_S, char_T in zip(list_S, list_T):
            if char_S != char_T:
                print("Strings don't match")
                return False

        print("Strings match")
        return True


if __name__ == '__main__':

    str_matcher = Solution()
    print('\n')
    assert(str_matcher.backspaceCompare(S = "ab#c", T = "ad#c") == True)
    print('\n')
    assert(str_matcher.backspaceCompare(S = "ab##", T = "c#d#") == True)
    print('\n')
    assert(str_matcher.backspaceCompare(S = "a##c", T = "#a#c") == True)
    print('\n')
    assert(str_matcher.backspaceCompare(S = "a#c", T = "b") == False)
    print('\n')
    assert(str_matcher.backspaceCompare(S = "isfcow#", T = "isfco#w#") == False)