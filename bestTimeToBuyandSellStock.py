# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        max_profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price > buy:
                max_profit = max(max_profit, buy - price)
            else:
                buy = price
        return max_profit

prices = [7,1,5,3,6,4]
ob1 = Solution()
print(ob1.maxProfit(prices))