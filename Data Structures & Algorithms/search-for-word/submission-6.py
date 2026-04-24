class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(x,y, word):
            if word=='':
                return True
            a,b,c,d = False, False, False, False

            if board[x][y]==word[0] and (x,y) not in visited:
                if len(word) == 1:   # ✅ fix here
                    return True
                visited.add((x,y))

                if x+1<len(board): a = dfs(x+1, y, word[1:])
                if y+1<len(board[0]): b = dfs(x, y+1, word[1:])
                if y-1>=0: c = dfs(x, y-1, word[1:])
                if x-1>=0: d = dfs(x-1, y, word[1:])
                visited.remove((x, y))
                if a or b or c or d:

                    return True
            return False



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visited = set()
                    found = dfs(i,j, word)
                    if found: return True
        return False