class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}

        def dfs(i):
            if i == n:
                return 0
            if i in d:
                return d[i]
                

            LIS = 1
            for j in range(i+1, len(nums)):
                if nums[j]>nums[i]:
                    LIS = max(LIS, 1+dfs(j))
            d[i] = LIS
            return LIS

        return max(dfs(i) for i in range(n))