class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for i in range(len(s), 0,-1):
        #     for j in range(0, len(s)-i+1):
        #         ss = s[j:j+i]
        #         if ss==ss[::-1]:
        #             return ss
        # return ""
        
        
        
        res, resLen = "", 0

        for i in range(len(s)-1, -1,-1):
            for j in range(len(s)-1,i-1,-1):
                if j - i + 1 <= resLen:
                    break
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res
        