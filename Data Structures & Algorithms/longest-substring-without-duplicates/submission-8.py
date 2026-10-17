class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1:
            return len(s)
        ss = s[0]
        i = 0
        ml = 1
        se = set(s[0])
        for j in range(1, len(s)):
            
            # print(se)
            if s[j] not in se:
                ss = ss+s[j]
                se.add(s[j])
                l = len(ss)
                ml = max(l,ml)
            else:
                while s[j] in se:
                    
                    se.remove(s[i])
                    ss = ss[1:]
                    i+=1
                  
                ss = ss+s[j]
                l = len(ss)  
                se.add(s[j])
                # se.remove(s[j])
                ml = max(l,ml)
        return ml