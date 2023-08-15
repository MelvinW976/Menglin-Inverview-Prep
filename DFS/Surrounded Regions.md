# 岛屿问题的DFS

这道题咋说呢，刚开始想用两遍dfs做的，第一遍判断是不是包围，第二遍flip，但是第一个dfs的判断visited比较难，如果visited过那究竟是return false or true。
正确思路：
1. 先把边界的O 都dfs了，标记成T, 再iter不是T的就可以flip了

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        surrounded = set()
        m, n = len(board), len(board[0])
        def check(i, j):
            if i < 0 or j < 0 or i >= m or j >= n: return False
            return True
        def dfs(board, i, j):
            if not check(i, j) or board[i][j] != "O":
                return 
            board[i][j] = "T"
            nextStep = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in nextStep:
                dfs(board, i + x, j + y)
        def flip():
            for x in range(m):
                for y in range(n):
                    if board[x][y] == "T":
                        board[x][y] = "O"
                    elif board[x][y] == "O":
                        board[x][y] = "X"
        for x in range(m):
            if board[x][0] == "O" or board[x][n-1] == "O":
                dfs(board, x, 0)
                dfs(board, x, n-1)
        for y in range(n):
            if board[0][y] == "O" or board[m-1][y] == "O":
                dfs(board, 0, y)
                dfs(board, m-1, y)
        flip()
```