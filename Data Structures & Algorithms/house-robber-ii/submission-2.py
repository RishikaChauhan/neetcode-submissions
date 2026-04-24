class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:   # ✅ fix edge case
            return nums[0]

        def fun(num):
            curr, prev = 0,0
            for n in range(len(num)):
                temp = max(curr, prev+num[n])
                prev = curr
                curr = temp
            return curr
        
        return max(fun(nums[1:]), fun(nums[:-1]))