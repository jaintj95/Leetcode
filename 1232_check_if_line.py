# Problem statement - https://leetcode.com/problems/check-if-it-is-a-straight-line/


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


class Solution:
    def checkStraightLine(self, coordinates) -> bool:

        if len(coordinates) == 2:
            return True
        A, B = coordinates[0][1] - coordinates[1][1], coordinates[1][0] - coordinates[0][0]
        C = -A*coordinates[0][0] - B*coordinates[0][1]
        for point in coordinates:
            if A*point[0] + B*point[1] + C != 0:
                return False
        return True


class SolutionOld:
    def checkStraightLine(self, coordinates) -> bool:

        if len(coordinates) == 2:
            return True
            
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]
        
        if run == 0:
            slope = float("inf")    
        else:
            slope = rise/run

        for idx in range(1, len(coordinates)-2):
            rise = coordinates[idx+1][1] - coordinates[idx][1]
            run = coordinates[idx+1][0] - coordinates[idx][0]

            if run == 0:
                curr_slope = float("inf")
            else:
                curr_slope = rise/run
                
            if curr_slope != slope:
                return False

        return True


if __name__ == "__main__":

    verifyLine = Solution()

    # # Test Case 1
    # assert verifyLine.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True

    # # Test Case 2
    # assert verifyLine.checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False

    # Test Case 3
    assert verifyLine.checkStraightLine(coordinates = [[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]) == False