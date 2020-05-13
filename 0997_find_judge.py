# Problem statement - https://leetcode.com/problems/find-the-town-judge


"""
Complexity analysis:

1) Time complexity: O(T+N) where T is the number of items in trust array and N is the number of items in counts array

2) Space complexity: O(N) since we create an array of size N+1 to store the counts for every person
"""


class Solution:
    def findJudge(self, N: int, trust) -> int:
        counts = [0] * (N+1)
        for i, j in trust:
            counts[i] -= 1
            counts[j] += 1
            
        for idx in range(1, N+1):
            if counts[idx] == N-1:
                return idx
            
        return -1


if __name__ == '__main__':

    whoJudge = Solution()

    # Test Case 1
    assert whoJudge.findJudge(N=2, trust = [[1,2]]) == 2

    # Test Case 2
    assert whoJudge.findJudge(N=3, trust = [[1,3],[2,3]]) == 3

    # Test Case 3
    assert whoJudge.findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]) == -1

    # Test Case 4
    assert whoJudge.findJudge(N = 3, trust = [[1,2],[2,3]]) == -1

    # Test Case 5
    assert whoJudge.findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3