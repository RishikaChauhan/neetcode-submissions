class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n =len(nums)
        res = []
        d = {}
        for i in s:
            d[i]=nums.count(i)
        for i in d:
            if d[i]>n//3:
                res.append(i)
        return res