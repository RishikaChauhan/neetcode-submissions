class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        mv = 0

        while i<j:
            v = min(heights[i],heights[j])*(j-i)
            mv = max(v,mv)
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
                j-=1
        return mv