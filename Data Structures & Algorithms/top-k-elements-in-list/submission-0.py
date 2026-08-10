import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap,(count,num))

            if len(heap) > k:
                heapq.heappop(heap)
        result = [ num for count, num in heap]
        return result