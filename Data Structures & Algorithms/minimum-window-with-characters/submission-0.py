class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        for i in range(len(t), len(s)+1):
            for j in range(len(s)-i+1):
                ss = s[j:j+i]
                if set(t).intersection(set(ss)) == set(t):
                    valid = True
                    for ch in t:
                        if ss.count(ch) < t.count(ch):   # ✅ fix here
                            valid = False
                            break
                    if valid:
                        return ss
                    # valid = True
                    # for i in t:
                    #     if t.count(i)> ss.count(i):
                    #         valid = False
                    #         break
                    # if valid:
                    #     return ss
        return ""