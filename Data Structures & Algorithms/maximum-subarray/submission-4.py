class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        sm = 0
        if len(nums)==1: return nums[0]

        for i in range(len(nums)):
            if sm<0:
                sm = nums[i]
            else:
                sm = sm+nums[i]
            maxsum = max(maxsum, sm)

        return maxsum