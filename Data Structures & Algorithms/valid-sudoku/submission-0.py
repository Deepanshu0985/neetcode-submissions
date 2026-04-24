class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                number = board[i][j]

                if number=='.':
                    continue
                
                if number in row[i] or number in col[j] or number in square[(i//3,j//3)]:
                    return False
                
                col[j].add(number)
                row[i].add(number)
                square[(i//3,j//3)].add(number)

        return True

        