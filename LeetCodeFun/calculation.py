# 计算数学题
from typing import List

class Calculation:
    '''计算股票的最佳买卖点，返回最佳收益值'''
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        min = prices[0]
        val = 0
        for i in range(l):
            if prices[i] <= min:
                min = prices[i]
                continue
            else:
                p = prices[i] - min
                val = p if p > val else val
        return val