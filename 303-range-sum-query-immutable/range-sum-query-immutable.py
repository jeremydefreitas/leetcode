class NumArray(object):

    def __init__(self, nums):
       self.prefixSum = []
       cur = 0
       for n in nums:
        cur += n
        self.prefixSum.append(cur)
        

    def sumRange(self, left, right):
        res = self.prefixSum[right] - (self.prefixSum[left - 1] if left > 0 else 0)
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)