class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(arr)):
            d[i] = abs(arr[i]-x)
        indices = sorted(d.keys(), key=lambda i: (d[i], arr[i]))
        for i in range(k):
            res.append(arr[indices[i]])
        res = sorted(res)
        return res