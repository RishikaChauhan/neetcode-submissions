class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            k = bin(i)
            res.append(k.count('1'))
        return res