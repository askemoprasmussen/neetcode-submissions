class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            numbers =[]
            for j in range(9):
                if board[i][j] != ".":
                    numbers.append(board[i][j])
            if len(set(numbers)) != len(numbers):
                return False

        for j in range(9):
            numbers =[]
            for i in range(9):
                if board[i][j] != ".":
                    numbers.append(board[i][j])
            if len(set(numbers)) != len(numbers):
                return False
        
        for row in range(3):
            for column in range(3):
                numbers = []
                for i in range(row * 3, row *3 +3):
                    for j in range(column * 3, column * 3+3):
                        if board[i][j] != ".":
                            numbers.append(board[i][j])
                if len(set(numbers)) != len(numbers):
                    return False
        
        return True
