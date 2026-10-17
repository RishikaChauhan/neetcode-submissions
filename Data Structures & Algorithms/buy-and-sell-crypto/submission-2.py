class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices)):
            
            for j in prices[i:]:
                s = j
                p = max(p, s-prices[i])
        return p