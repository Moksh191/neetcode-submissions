class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        seen = []
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(seen, num)
                continue
            
            minimum = seen[0]
            if num > minimum:
                heapq.heapreplace(seen, num)
        return seen[0]
