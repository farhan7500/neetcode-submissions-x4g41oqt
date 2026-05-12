class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return 0
        left = 1
        right = max(piles)

        result = max(piles) + 1

        while left <= right:
            mid = (left + right) // 2
            passes = self.compute_passes(piles, mid)
            if passes <= h:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1

        return result;


    def compute_passes(self, piles, num):
        passes = 0
        for pile in piles:
            passes += math.ceil(pile/num)
        return passes


