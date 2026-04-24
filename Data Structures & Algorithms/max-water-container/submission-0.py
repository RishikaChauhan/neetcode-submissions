class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height)-1
        mv = 0
        while l<=h:
            v = min(height[h], height[l])*(h-l)
            mv = max(mv, v)
            if height[h]<height[l]:
                h-=1
            elif height[h]>height[l]:
                l+=1
            else:
                h-=1
                l+=1
        return mv