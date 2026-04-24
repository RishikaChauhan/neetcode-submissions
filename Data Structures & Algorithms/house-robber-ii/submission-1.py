class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:   # ✅ fix edge case
            return nums[0]

        curr, prev = 0,0
        for n in range(len(nums)-1):
            temp = max(curr, prev+nums[n])
            prev = curr
            curr = temp
        a = curr
        curr, prev = 0,0
        for n in range(1, len(nums)):
            temp = max(curr, prev+nums[n])
            prev = curr
            curr = temp
        b = curr
        return max(a,b)