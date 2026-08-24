class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit if max_profit > 0 else 0