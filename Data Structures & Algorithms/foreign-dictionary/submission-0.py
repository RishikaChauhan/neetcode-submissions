class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char:set() for word in words for char in word}

        visited = {}
        for i in range(len(words)-1):
            min_len = min(len(words[i]), len(words[i+1]))
            if words[i][:min_len]==words[i+1][:min_len] and len(words[i])>len(words[i+1]):
                return ""
            for j in range(min_len):
                if words[i][j]!=words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break

        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c]=True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c]=False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])