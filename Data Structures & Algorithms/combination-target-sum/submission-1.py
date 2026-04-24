class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        level = []
        def dfs(nums,st, target):
            nonlocal level
            if target ==0:
                
                res.append(level.copy())
                # level=[]
                return
            if target<0: return
            else:
                for i in range(st, len(nums)):
                    level.append(nums[i])
                    dfs(nums,i, target-nums[i])
                    level.pop()
        dfs(nums,0, target)
        return res