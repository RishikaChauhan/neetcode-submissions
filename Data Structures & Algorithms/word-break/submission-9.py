class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        d = {}
        def dfs(s):
            if s in d:
                return d[s]
            if s in wordSet:
                d[s] = True
                return True
            for i in range(len(s)):
                s1 = s[:i]
                s2 = s[i:]
                if s1 in wordSet:
                    

                    if dfs(s2):
                        d[s]=True
                        return True
            d[s] = False
            return False
        return dfs(s)