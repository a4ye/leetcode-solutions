class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_is_zero = False
        first_col_is_zero = False
        
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_is_zero = True
                break
        
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_is_zero = True
                break
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        if first_row_is_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        if first_col_is_zero:
            for i in range(rows):
                matrix[i][0] = 0
