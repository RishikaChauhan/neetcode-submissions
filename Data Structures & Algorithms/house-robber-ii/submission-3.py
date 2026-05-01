class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]

        def dfs(nums):
            cur , pre = 0,0
            for i in range(len(nums)):

                temp = max(cur, pre+nums[i])
                pre = cur
                cur = temp
            return cur
        return max(dfs(nums[1:]), dfs(nums[:-1]), nums[0])