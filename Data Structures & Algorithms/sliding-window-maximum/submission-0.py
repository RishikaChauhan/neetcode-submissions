class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = []
        for i in range(len(nums)-k+1):
            mx.append(max(nums[i:i+k]))
        return mx