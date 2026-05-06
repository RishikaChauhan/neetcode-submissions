class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        d = {}
        dir = [(-1,0), (0,-1), (1,0),(0,1)]
        inf = 2147483647

        def bfs(r,c):
            if (r,c) in d:
                return d[(r,c)]
            q = deque([(r,c)])
            visit = set()
            visit.add((r,c))
            step = 0
            while q:
                for i in range(len(q)):
                    ro,co = q.popleft()
                    if grid[ro][co]==0:
                        d[(r, c)] = step
                        return step
                    for dr,dc in dir:
                        nr, nc = ro+dr, co+dc
                        if (0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit and grid[nr][nc]!=-1):
                            visit.add((nr,nc))
                            q.append((nr,nc))
                step+=1
            d[(nr,nc)]=inf

            return inf

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==inf:
                    grid[r][c] = bfs(r,c)