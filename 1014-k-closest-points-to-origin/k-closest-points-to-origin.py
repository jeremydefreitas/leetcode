class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        x2 = 0
        y2 = 0
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dist = (x1**2 + y1**2)
            points[i] = [dist, x1, y1]
        print(points)

        heapq.heapify(points)
        res = []
        
        for i in range(k):
            dist, x, y = heapq.heappop(points)
            res.append([x,y])

        return res
        