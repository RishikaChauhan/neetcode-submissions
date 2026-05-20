class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        ss = ""
        for r in range(len(s)):
            if s[r] not in ss:
                
                ss = ss+s[r]
            else:
                while s[r] in ss:
                    l+=1
                    ss=ss[1:]
                
                ss+=s[r]
                
            res = max(res, len(ss))
        return res