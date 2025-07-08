class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]
        if max_profit > 0:
            return max_profit
        else:
            return 0
