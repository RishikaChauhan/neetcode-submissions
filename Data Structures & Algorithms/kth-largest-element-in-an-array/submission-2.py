class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        i = 0
        for i in range(k):
            h = heapq.heappop(nums)
            # i+=1÷
        return -h