class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums = set(nums)
        mcount = 0
        for i in nums:
            if i-1 not in nums:
                count = 1
                while i in nums:
                    count+=1
                    i+=1
                mcount = max(count, mcount)
        return mcount-1