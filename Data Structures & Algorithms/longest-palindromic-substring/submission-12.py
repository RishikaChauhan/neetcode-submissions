class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1: return s
        for i in range(len(s), -1, -1):
            for j in range(len(s)-i, -1, -1):
                
                ss = s[j:j+i]
                print(ss)
                if ss==ss[::-1]:
                    return ss
        return ""