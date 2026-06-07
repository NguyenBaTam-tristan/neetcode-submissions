class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy = 0
        sell = 1
        
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
                sell += 1
            else:
                sell += 1
                best_profit = max(best_profit, profit)
        return best_profit

        