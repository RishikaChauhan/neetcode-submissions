class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = nums[-k:]
        # print(l)
        # for i in range(len(nums)-k):
        #     nums[i+k] = nums[i]
        # nums[:k] = l
        # return nums
        k = k % len(nums)

        if k == 0:
            return

        l = nums[-k:]

        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]

        nums[:k] = l
        