class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0

        for sell in range(len(prices)):
            res = max(res, prices[sell] - prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell

        return res