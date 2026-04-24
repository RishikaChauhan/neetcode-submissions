"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st =sorted([i.start for i in intervals])
        en =sorted([i.end for i in intervals])

        res = 0
        count = 0
        s,e = 0,0
        while s<len(intervals):
            if st[s]<en[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res