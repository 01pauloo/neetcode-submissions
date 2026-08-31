from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)  # nbr de lignes
        m = len(board[0])  # nbr de colonnes
        for i in range(n):
            c1 = Counter()
            for elt in board[i]:
                if elt == ".":
                    continue
                c1[elt] += 1
                if c1[elt] > 1:
                    return False



            for j in range(m):
                c2 = Counter()
                for i in range(n):
                    elt = board[i][j]
                    if elt == ".":
                        continue
                    c2[elt] += 1
                    if c2[elt] > 1:
                        return False
                          
        for box_i in range(0,9,3):
            for box_j in range(0,9,3):
                c3 = Counter()
                for r in range(3):
                    for c in range(3):
                        elt = board[box_i + r][box_j + c]
                        if elt == ".":
                            continue
                        c3[elt] += 1
                        if c3[elt] > 1:
                            return False
        return True
