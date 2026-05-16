class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        mnword = word1 if len(word1)<len(word2) else word2
        for i in range(len(mnword)):
            res+=word1[i]
            res+=word2[i]
        res+=word1[len(mnword):]+word2[len(mnword):]
        return res