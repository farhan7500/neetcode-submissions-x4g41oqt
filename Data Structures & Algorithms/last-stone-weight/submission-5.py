class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            second_heaviest = heapq.heappop(stones)
            heapq.heappush(stones, heaviest - second_heaviest)
        return 0 - stones[0]
