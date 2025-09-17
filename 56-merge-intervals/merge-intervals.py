class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key= lambda i : i[0])
        res = [intervals[0]]


        for start, finish in intervals:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], finish)
            else:
                res.append([start, finish])
        return res

                
        