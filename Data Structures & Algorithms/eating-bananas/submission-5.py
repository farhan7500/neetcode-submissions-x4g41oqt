class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.binary_search_style(piles, h)

    def binary_search_style(self, piles, h):
        maximum_num = max(piles)
        minimum_attempts = None
        l = 1
        r = maximum_num
        while l <= r:
            mid = (l + r) // 2
            hours = self.get_hours(piles, mid)
            if hours <= h:
                if minimum_attempts is None:
                    minimum_attempts = mid

                else:
                    minimum_attempts = min(mid, minimum_attempts)
                r = mid - 1
            else:
                l = mid + 1

        return minimum_attempts

    def get_hours(self, piles, num):
        total = 0
        for pile in piles:
            if pile % num == 0:
                total += int(pile / num)
            else:
                total += int(pile // num) + 1
        return total