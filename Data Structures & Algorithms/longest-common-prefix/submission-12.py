class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs: return ""
        word = strs[0]
        for i,ch in enumerate(word):

            for wd in strs:
                if  i >= len(wd) or wd[i]!= ch:
                    return wd[:i]
        return word