class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []

        # intervals.sort()

        # for st, en in intervals:
        #     # completely before
        #     if en < newInterval[0]:
        #         res.append([st, en])

        #     # completely after
        #     elif st > newInterval[1]:
        #         res.append(newInterval)
        #         newInterval = [st, en]

        #     # overlap → merge
        #     else:
        #         newInterval[0] = min(newInterval[0], st)
        #         newInterval[1] = max(newInterval[1], en)

        # res.append(newInterval)
        # return res
        
        res = []

        intervals.sort()
        print(intervals)
        for st,en in intervals:
            if en<newInterval[0]:
                res.append([st, en])
            elif st>newInterval[1]:
                res.append(newInterval)
                newInterval = [st, en]
            else:
                newInterval[0] = min(newInterval[0], st)
                newInterval[1] = max(newInterval[1], en)

        res.append(newInterval)
        return res