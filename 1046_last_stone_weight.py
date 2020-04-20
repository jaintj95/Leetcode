# Problem statement - https://leetcode.com/problems/last-stone-weight/


"""
Complexity analysis:

1) Time complexity: O(n log n) - A heap takes O(log n) time for the implicit heapify operation that runs when an element is inserted. 
                                Since we have n elements the total time taken is O(n log n)
2) Space complexity: O(n) - We are creating an additional array for heap storage. Number of elements is n.
"""

class Solution:
    def lastStoneWeight(self, stones) -> int:
        
        import heapq 
        neg_sorted = []
        for item in stones:
            heapq.heappush(neg_sorted, -item)
            
        while len(neg_sorted) >= 2:
            larger = -(heapq.heappop(neg_sorted))
            large = -(heapq.heappop(neg_sorted))
            if large == larger:
                continue
            heapq.heappush(neg_sorted,-(larger-large))
        
        return -(heapq.heappop(neg_sorted))

    ## Shorter alternative
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     q = [-stone for stone in stones]
    #     heapq.heapify(q)
    #     while (len(q)) > 1:
    #         heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))
    #     return -q[0]

if __name__ == '__main__':
    
    stoneSmasher = Solution()

    assert(stoneSmasher.lastStoneWeight( [2,7,4,1,8,1]) == 1)