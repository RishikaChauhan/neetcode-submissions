class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p = set(nums)
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0) + 1
            
        res = sorted(d.keys(), key=lambda x: d[x], reverse=True)        
        return res[:k]