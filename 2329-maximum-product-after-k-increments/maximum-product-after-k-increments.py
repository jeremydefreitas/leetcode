import math
class Solution(object):
    def maximumProduct(self, nums, k):
        mod = 10 ** 9 + 7
        heapq.heapify(nums)
        for i in range(k):
            n = heapq.heappop(nums)
            heapq.heappush(nums, n + 1)
        res = 1
        for n in nums:
            res = (res * n) % mod
        return res
