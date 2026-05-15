class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if "" in strs: return ""
        # word = strs[0]
        # for i,ch in enumerate(word):
        #     print(i,ch)
        #     for wd in strs:
        #         print(len(wd))
        #         if  i >= len(wd) or wd[i]!= ch:
        #             return wd[:i]
        # return word


        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]