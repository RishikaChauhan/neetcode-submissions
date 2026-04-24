class Solution:
    def climbStairs(self, n: int) -> int:
        mem = dict()
        tab = [1]*(n+1)
        for i in range(2, n+1):
            tab[i] = tab[i-1]+tab[i-2]
        return tab[-1]