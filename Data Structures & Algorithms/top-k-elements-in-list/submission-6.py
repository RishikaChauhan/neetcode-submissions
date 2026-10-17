class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        d = {}

        for i in nums:
            d[i] = d.get(i, 0) + 1
        # print(list(d.keys()).sort(key = lambda x: d[x], reverse = True))
        return sorted(d.keys(), key = lambda x: d[x], reverse = True)[:k]