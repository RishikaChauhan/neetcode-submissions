class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res =float("inf")
        sm =0
        for r in range(len(nums)):
            sm +=nums[r]
            while sm>=target:
                sm = sm-nums[l]
                
                res = min(res, r-l+1)
                l+=1
        return 0 if res==float("inf") else res