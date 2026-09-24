class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k = rowShift[i] % n
            row = [0] * n
            for j in range(n):
                row[(j-k)%n] = grid[i][j]
            grid[i] = row
        for j in range(n):
            k = colShift[j] % n
            col = [0] * n
            for i in range(n):
                col[(i-k)%n] = grid[i][j]
            for i in range(n):
                grid[i][j] = col[i]
        return grid