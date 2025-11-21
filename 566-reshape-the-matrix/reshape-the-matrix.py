class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        ROWS, COLS = len(mat), len(mat[0])
        originalSize = ROWS * COLS
        newSize = r * c

        if originalSize != newSize:
            return mat
        
        
        res = [[0 for _ in range(c)] for i in range(r)]
        
        tmp = []

        for i in range(ROWS):
            for j in range(COLS):
                tmp.append(mat[i][j])

        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[k]
                k += 1

        return res


        