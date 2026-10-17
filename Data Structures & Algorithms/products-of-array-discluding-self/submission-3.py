class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        l = 1
        m = 1
        for i in nums:
            if i!= 0:
                m = m*i
        if nums.count(0)>=2:
            return [0]* len(nums)
        if nums.count(0) == 1:
            i = nums.index(0)
            l = [0]*len(nums)
            l[i] = m
            return l
        else:
            for i in range(len(nums)):
                nums[i] = m//nums[i]
            return nums
