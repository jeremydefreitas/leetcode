class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefix = set()
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        for n in arr1:
            while n and n not in prefix:
                prefix.add(n)
                n = n // 10
            
        res = 0
        for n in arr2:
            while n and n not in prefix:
                n = n // 10

            if n != 0:
                res = max(res, len(str(n)))

        return res

        