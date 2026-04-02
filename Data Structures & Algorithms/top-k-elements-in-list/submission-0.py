import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            try:
                nums_map[num] += 1
            except KeyError:
                nums_map[num] = 1

        heap = []
        for key, val in nums_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [n[1] for n in heap]
