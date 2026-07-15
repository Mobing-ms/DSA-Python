from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                value = board[i][j]
                box = (i // 3, j // 3)

                if value in rows[i]:
                    return False

                if value in cols[j]:
                    return False

                if value in boxes[box]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)

        return True