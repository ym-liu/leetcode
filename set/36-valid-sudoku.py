class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_sets, cols_sets, squares_sets = (
            [set() for _ in range(9)],
            [set() for _ in range(9)],
            [set() for _ in range(9)],
        )

        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if ord("0") <= ord(digit) <= ord("9"):
                    squares_index = (row // 3) * 3 + (col // 3)
                    if (
                        digit in rows_sets[row]
                        or digit in cols_sets[col]
                        or digit in squares_sets[squares_index]
                    ):
                        return False

                    rows_sets[row].add(digit)
                    cols_sets[col].add(digit)
                    squares_sets[squares_index].add(digit)

        return True
