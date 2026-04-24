class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0,0
        mp = 0
        for i in range(len(prices)):
            b = prices[i]
            for j in range(i+1, len(prices)):
                s = prices[j]
                p = s-b
                mp = max(mp, p)
        return mp
        
        
        
        # b, s = 0,0
        # mp = 0
        # for i in range(len(prices)):
        #     b = i
        #     for j in range(i+1, len(prices)):
        #         s = j
        #         mp = max(mp, prices[s]- prices[b])
        # return mp