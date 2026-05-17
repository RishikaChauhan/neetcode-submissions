class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        p = 0
        for i in range(len(nums)):
            if nums[i]!=nums[i-1]:
                nums[p]=nums[i]
                p+=1
        return p