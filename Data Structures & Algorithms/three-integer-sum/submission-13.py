class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        res = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                sm = nums[i]+nums[j]+nums[k]
                if sm ==target:
                    res.append(sorted([nums[i], nums[j], nums[k]])) if sorted([nums[i], nums[j], nums[k]]) not in res else None
                    j+=1
                    k-=1
                elif sm>target:
                    k-=1
                elif sm<target:
                    j+=1
        return res