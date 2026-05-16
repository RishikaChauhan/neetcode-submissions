class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cursum = 0
        prefixsum = {0:1}
        for num in nums:
            cursum+=num
            dif = cursum-k
            res+=prefixsum.get(dif,0)
            prefixsum[cursum] = 1+prefixsum.get(cursum,0)
        return res