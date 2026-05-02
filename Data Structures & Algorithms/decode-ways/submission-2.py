class Solution:
    def numDecodings(self, s: str) -> int:
        d = {}
        
        def dfs(s):
            if s in d:
                return d[s]

            if not s:
                return 1
            if s[0]=='0':
                return 0
            res = dfs(s[1:])

            if len(s)>=2 and 10<=int(s[:2])<=26:
                res+=dfs(s[2:])

            d[s]=res
            return res
        return dfs(s)
        #     if len(s)<2:
        #         if s=='0':
        #             return 0
        #         else:
        #             return 1
        #     elif len(s)==2:
        #         if s!='10' and s!='20' and s<27:
        #             return 1
        #         else:
        #             return 2
        #     else:
        #         return (dfs(s[:1]) + dfs(s[1:]))+(dfs(s[:2])+dfs(s[2:]))

        #     # res = dfs(i+1)
        #     # if i<len(s)-1:
        #     #     if (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
        #     #         res +=dfs(i+2)
        #     # return res
        # return dfs(s)