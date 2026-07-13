class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        seen = []
        for i, num in enumerate(nums):
            if i < k:
                seen.append(num)
                continue
            minimum = min(seen)
            if num > minimum:
                seen.remove(minimum)
                seen.append(num)
        return min(seen)
