class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" ")).lower()
        for i in s:
            if not i.isalnum():
                s = s.replace(i,"")
        # print(s)
        return s==s[::-1]