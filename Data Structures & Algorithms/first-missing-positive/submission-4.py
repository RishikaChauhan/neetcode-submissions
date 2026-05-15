class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(2, max(nums)+1):
            print(i)
            if i-1>0 and i-1 not in nums:
                return i-1
        return max(nums)+1 if max(nums)+1>0 else 1