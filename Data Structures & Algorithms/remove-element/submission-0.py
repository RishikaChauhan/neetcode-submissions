class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        print(nums, nums[:])
        for i in range( len(nums)):
            if nums[i]!=val:
                nums[p] = nums[i]
                p+=1

                # nums[i] = nums[p]
        return p