class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        def dfs(i,j):
            if grid[i][j]=="0": return
            if (i,j) in visited: return
            else:
                visited.add((i,j))
                if i+1<len(grid): dfs(i+1, j)
                if j+1<len(grid[0]): dfs(i,j+1)
                if i-1>=0: dfs(i-1,j)
                if j-1>=0: dfs(i,j-1)
                
            


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]=="1" and (x,y) not in visited:
                    count+=1
                    dfs(x,y)

        return count
        
        
        # visited = set()
        # island = 0
        
        # def dfs(x,y):
            
        #     if grid[x][y] == "0":
        #         return
        #     if (x,y) in visited:
        #         return
        #     else:
        #         visited.add((x,y))
        #         if x+1<len(grid): dfs(x+1, y)
        #         if x>0: dfs(x-1,y)
        #         if y+1< len(grid[0]): dfs(x, y+1)
        #         if y>0: dfs(x, y-1)


        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] =="1" and (i,j) not in visited:
        #             island +=1
        #             dfs(i,j)
        # return island