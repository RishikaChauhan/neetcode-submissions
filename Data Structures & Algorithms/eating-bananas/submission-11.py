class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        
        l, r = 1, max(piles)
        while l<r:
            t = 0
            m = (l+r)//2
            for j in piles:
                # t+=(j//m + 1) if j%m!= 0 else j//m
                t+=(j + m - 1) // m
            
            if t<=h:
                r = m
            else:
                l = m+1
        return l