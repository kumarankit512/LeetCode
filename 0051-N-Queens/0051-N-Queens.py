class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in colSet or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

#Time Complexity: O(n!), as we are trying to place queens in each row and for each row, we have n choices.
#Space Complexity: O(n), for the recursion stack and the sets used to track columns and diagonals.