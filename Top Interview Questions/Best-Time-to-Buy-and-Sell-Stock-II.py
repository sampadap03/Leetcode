# Easy Collection
# Array
# Language : Python3
# Question : https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564
# Best Time to Buy and Sell Stock II
# Statement: Say you have an array prices for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
