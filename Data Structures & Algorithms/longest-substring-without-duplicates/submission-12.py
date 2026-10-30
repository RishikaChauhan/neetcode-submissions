class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        mc = 0
        mv = 0
        se = set()
        while j<len(s):
            if s[j] in se:
                while s[i]!= s[j]:
                    
                    se.remove(s[i])
                    i+=1
                    # mc-=1
                se.remove(s[i])
                i+=1
            se.add(s[j])
            j+=1
            mc = j-i
            # print(i,j,mc,se)
            mv = max(mc, mv)
        return mv