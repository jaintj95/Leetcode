# Problem statement - https://leetcode.com/problems/longest-common-subsequence/

# Reference 1 - https://leetcode.com/problems/longest-common-subsequence/discuss/348884/C%2B%2B-with-picture-O(nm)
# Reference 2 - https://leetcode.com/problems/longest-common-subsequence/discuss/398711/ALL-4-ways-Recursion-greater-Top-down-greaterBottom-Up-greater-Efficient-Solution-O(N)-including-VIDEO-TUTORIAL
# Reference 3 - https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis



"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:




if __name__ == '__main__':

    subseq = Solution()

    # Test Case 1
    # Input: text1 = "abcde", text2 = "ace" 
    # Output: 3  
    # Explanation: The longest common subsequence is "ace" and its length is 3.
    assert subseq.longestCommonSubsequence("abcde", "ace") == 3


    # Test case 2
    # Input: text1 = "abc", text2 = "abc"
    # Output: 3
    # Explanation: The longest common subsequence is "abc" and its length is 3.
    assert subseq.longestCommonSubsequence("abc", "abc") == 3


    # Test case 3
    # Input: text1 = "abc", text2 = "def"
    # Output: 0
    # Explanation: There is no such common subsequence, so the result is 0.
    assert subseq.longestCommonSubsequence("abc", "def") == 0