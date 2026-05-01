class Solution:
    def climbStairs(self, n: int) -> int:
        # d = {1:1, 2:2}
        
        # def dfs(n):
        #     if n in d:
        #         return d[n]
        #     # else:
        #     d[n] = dfs(n-1)+dfs(n-2)
        #     return d[n]
        # return dfs(n)


        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b if n > 1 else 1