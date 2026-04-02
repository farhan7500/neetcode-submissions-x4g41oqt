class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maximum = 0
        while j < len(prices):
            if prices[j] > prices[i]:
                maximum = max(prices[j] - prices[i], maximum)
                j += 1
            else:
                i = j
                j = i + 1
        return maximum
        