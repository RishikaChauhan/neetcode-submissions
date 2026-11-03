class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def rec(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if total+nums[j]>target:
                    return
                cur.append(nums[j])
                rec(j, cur, total+nums[j])
                cur.pop()
        rec(0,[],0)
        return res