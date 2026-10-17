class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = 0
        nums = set(nums)
        # nums.sort()
        for i in nums:
            if i-1 not in nums:
                count =1
                j = i
                while j+1 in nums:
                    count+=1
                    j+=1
                c = max(c, count)
        return c