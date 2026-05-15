class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs: return ""
        word = strs[0]
        l = 0
        r = len(word)
        while l<=r:
            m = (l+r)//2
            t = False
            for w in strs:
                if len(w)<m or word[:m] != w[:m]:
                    r = m-1
                    t = True
                    break
                
            if t == False:
                l = m+1
        return word[:l - 1] if l > 0 else ""
