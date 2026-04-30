class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit,price-lowest)
            lowest = min(lowest,price)
        return profit