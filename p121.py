# My Solution: [TLE / Too slow]
lass Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            if i < len(prices) -1:
                p1 = price
                p2 = max(prices[i+1:])
                profit = p2 - p1
                if profit >= max_profit: max_profit = profit                

        return max_profit
        
        
# Solution no. 2 (From solutions sections)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
# Ques: Can this answer make sure buy first and sell next? I dont think so.
# Answers:
# the key idea is that "price" is the selling price, and min_price is the lowest possible buying price in the array BEFORE price

# Neater Version of Solution no. 2 
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0   

        max_profit = sell_price = 0
        for price in prices[::-1]:
            sell_price = max(sell_price, price)
            max_profit = max(max_profit, sell_price - price)
        return max_profit