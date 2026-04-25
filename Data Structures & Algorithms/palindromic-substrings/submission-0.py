class Solution:
    def countSubstrings(self, s: str) -> int:
        
        c = 0

        def dfs(i, j):
            nonlocal c
            if i < 0 or j >= len(s) or s[i] != s[j]:
                return
            
            # count current palindrome
            c += 1

            # expand outward
            dfs(i - 1, j + 1)

        # odd length palindromes
        for i in range(len(s)):
            dfs(i, i)

        # even length palindromes
        for i in range(len(s) - 1):
            dfs(i, i + 1)

        return c