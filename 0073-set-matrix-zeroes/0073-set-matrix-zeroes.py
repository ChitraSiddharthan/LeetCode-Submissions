class Solution(object):
    def setZeroes(self, matrix):
        Row, Column = len(matrix), len(matrix[0])
        r, c = [False]*Row, [False]*Column

        for m in range(Row):
            for n in range(Column):
                if matrix[m][n] == 0:
                    r[m] = True
                    c[n] = True

        for m in range(Row):
            for n in range(Column):
                if r[m] or c[n]:
                    matrix[m][n] = 0
                    