class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        word = strs[0]
        l = 0
        r = len(word)  # Fix: use len(word) not len(word)-1
        
        while l <= r:
            m = (l + r) // 2
            valid = True
            
            for w in strs:
                # Fix: check len(w) < m (not m+1)
                if len(w) < m or word[:m] != w[:m]:
                    r = m - 1
                    valid = False
                    break  # Early exit for efficiency
            
            if valid:
                l = m + 1
        
        return word[:l - 1]  # Fix: return word[:l-1] instead of word[:m]
