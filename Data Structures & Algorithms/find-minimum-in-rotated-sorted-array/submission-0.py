class Solution:
    def findMin(self, arr: List[int]) -> int:
        l = 0
        r= len(arr)-1
        

        while l<r:
            m = (l+r)//2

            if arr[m]>arr[r]:
                l=m+1
            else:
                r = m
            
                # l = m+1
        return arr[l]