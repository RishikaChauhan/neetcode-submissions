class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        visited = set()
        def dfs(i, j):
            if i<0 or j<0 or i>=row or j>=col or (i,j) in visited or grid[i][j]==0:
                return 0

            visited.add((i,j))
            if grid[i][j]==1:
                a=1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+ dfs(i,j-1)
            return a


        mar = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited:
                    a = 0
                    a = dfs(i,j)
                    mar = max(a, mar)

        return mar
