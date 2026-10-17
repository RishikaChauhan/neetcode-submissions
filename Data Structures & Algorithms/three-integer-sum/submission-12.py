class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        target = 0
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            # print(nums, j, k)
            while j<k:
                if nums[i]+nums[j]+nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                
                elif nums[i]+nums[j]+nums[k]>target:
                    k-=1
                else:
                    j+=1
        return res