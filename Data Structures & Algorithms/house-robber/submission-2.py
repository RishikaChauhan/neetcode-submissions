class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0,0
        for n in nums:
            temp = max(curr, prev+n)
            prev = curr
            curr = temp
            
        return curr