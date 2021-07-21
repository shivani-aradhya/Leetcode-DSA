class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_price = float('inf')

        for price in prices:
            min_price= min(min_price,price)

            profit = price - min_price
            max_profit= max(max_profit, profit)

        return max_profit
© 2021 GitHub, Inc.