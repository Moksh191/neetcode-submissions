class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_counter = {}

        for num in nums:
            if num not in freq_counter:
                freq_counter[num] = 1
            else:
                freq_counter[num] += 1
        
        output = []
        for i in range(k):
            output.append(max(freq_counter, key=freq_counter.get))
            freq_counter.pop(output[-1])
        
        return output
