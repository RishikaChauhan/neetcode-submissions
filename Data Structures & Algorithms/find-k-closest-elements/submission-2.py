class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr)-k
        while l<r:
            m=(l+r)//2
            if x-arr[m]>arr[m+k]-x:
                l=m+1
            else:
                r=m
        return arr[l:l+k]
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]