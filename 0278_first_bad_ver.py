# Problem statement - 


"""
Complexity analysis:

1) Time complexity: 

2) Space complexity: 
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
bad_dict = {}

def isBadVersion(version):
    return bad_dict[version]

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        end = n
        bad = end
        def binarySearch(start, end, bad):
            
            if start > end:
                return bad
            
            mid = start+(end-start)//2
            
            if isBadVersion(mid):
                bad = mid
                return binarySearch(start, mid-1, bad)
                
            else: 
                return binarySearch(mid+1, end, bad)
                
        return binarySearch(start, end, bad) 
                
        
if __name__ == "__main__":

    findBad = Solution()

    # Test Case 1
    n = 5
    bad = 4
    bad_dict = {}
    for i in range(1, n+1):
        if i == bad:
            bad_dict[bad] = True
        else:
            bad_dict[bad] = False

    assert findBad.firstBadVersion(5) == 4