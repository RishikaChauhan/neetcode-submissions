class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        se = set()
        ml = 0
        for j in range(len(s)):  
             
            if s[j] not in se:
                se.add(s[j])
            else:
                while s[j] in se:
                    se.remove(s[i])
                    i+=1
                se.add(s[j])
            ml = max(ml, j-i+1)
        return ml
        
        # se = set()
        # i = 0
        # ml = 0

        # for j in range(len(s)):
        #     while s[j] in se:
        #         se.remove(s[i])
        #         i += 1

        #     se.add(s[j])
        #     ml = max(ml, j - i + 1)

        # return ml
        
        
        
        
        
        
        
        
        
        
        
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res