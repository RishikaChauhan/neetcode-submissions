class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1+d.get(i,0)
            if d[i]>len(nums)//2:
                ans = i
                break
        return i
        print(d)