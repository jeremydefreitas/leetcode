class NumMatrix(object):

    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

        

    def sumRegion(self, row1, col1, row2, col2):
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        
        bottomLeftSum = self.sumMatrix[r2][c2]
        above = self.sumMatrix[r1 - 1][c2]
        left = self.sumMatrix[r2][c1 - 1]
        topLeft = self.sumMatrix[r1 - 1][c1 - 1]

        return (bottomLeftSum - above - left) + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)