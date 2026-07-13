class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_list = sorted(nums)
        return sorted_list[-k]