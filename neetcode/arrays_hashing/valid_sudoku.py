from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        groups = defaultdict(set)
        temp_1 = []
        temp_2 = []
        for i in range(len(board)):
            temp_1.clear()
            for j in range(len(board)):
            
                if i%3 == 0 and j%3 == 0:
                    key = [i,j]
                    groups[key].add(board[i][j])

                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in temp_1:
                        return False
                    else:
                        temp_1.append(board[i][j])

        for i in range(len(board)):
            temp_2.clear()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                else:
                    if board[j][i] in temp_2:
                        return False
                    else:
                        temp_2.append(board[j][i])

sol = Solution()
out = sol.isValidSudoku()
print(out)                        
