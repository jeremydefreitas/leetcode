class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res = len(points)
        prevInt = points[0]

        for i in range(1, len(points)):
            curr = points[i]
            if prevInt[1] >= curr[0]:
                res -= 1
                prevInt = [curr[0], min(curr[1], prevInt[1])]

            else:
                prevInt = curr
        return res

        