class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        d = {0:0,1:nums[0], 2:max(nums[0], nums[1])}
        
        def dfs(n):
            if n in d:
                return d[n]
            d[n] =  max(nums[n-1] + dfs(n-2), dfs(n-1))
            return d[n]
        return dfs(len(nums))