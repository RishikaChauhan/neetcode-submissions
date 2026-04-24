class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        count = 0
        pre = intervals[0]
        for i in intervals[1:]:
            if i[0]>=pre[1]:
                pre = i
            else:
                count+=1
                pre[1] = min(pre[1],i[1])
        return count