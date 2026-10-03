class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float("inf")
        max_profit = 0

        for price in prices:
            profit = price - curr_min
            max_profit = max(max_profit, profit)
            curr_min = min(curr_min, price)

        return max_profit
