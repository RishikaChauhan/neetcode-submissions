class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])-1
        n = len(matrix[0])
        while l<=r:
            m = (l+r)//2
            if matrix[m//n][m%n]==target:
                return True
            elif matrix[m//n][m%n]>target:
                r = m-1
            else:
                l=m+1
        return False