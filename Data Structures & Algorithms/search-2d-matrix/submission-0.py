class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        column = len(matrix[0])
        row = 0 
        cols = column-1

        while row<rows and cols>-1:
            curr = matrix[row][cols]
            if curr==target:
                return True
            if target>curr:
                row+=1
            else:
                cols-=1
        return False

            



        