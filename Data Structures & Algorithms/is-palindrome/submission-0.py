class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum(): s = s.replace(i, '')
        print(s)
        return ''.join(s).lower()==''.join(s).lower()[::-1]