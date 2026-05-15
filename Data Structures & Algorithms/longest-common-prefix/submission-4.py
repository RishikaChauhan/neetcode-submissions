class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        word = strs[0]
        l, r = 0, len(word)
        
        while l <= r:
            m = (l + r) // 2
            valid = all(len(w) >= m and w[:m] == word[:m] for w in strs)
            
            if valid:
                l = m + 1
            else:
                r = m - 1
        
        return word[:l - 1] if l > 0 else ""