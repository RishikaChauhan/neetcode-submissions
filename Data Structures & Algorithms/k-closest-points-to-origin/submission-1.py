class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_loc = []
        for x, y in points:
            dist = (x**2)+(y**2)
            points_loc.append([dist, x, y])
        heapq.heapify(points_loc)
        res = []
        while k>0:
            d, x,y = heapq.heappop(points_loc)
            res.append([x,y])
            k-=1
        return res