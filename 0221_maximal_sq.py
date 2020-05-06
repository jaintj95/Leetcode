# Problem statement - https://leetcode.com/problems/maximal-square/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""

class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        mat2 = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                mat2[i][j] = min(mat2[i - 1][j - 1], mat2[i - 1][j], mat2[i][j - 1]) + 1 if matrix[i][j] == '1' else 0
        return max([max(row) for row in mat2]) ** 2



if __name__ == '__main__':

    maxSQ = Solution()

    # Test Case 1
    matrix1 =  [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]

    assert maxSQ.maximalSquare(matrix1) == 4