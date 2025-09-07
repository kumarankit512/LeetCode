class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r - 1][c]:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1]:
                        perimeter -= 2
        return perimeter

#Brute Force Approach:
#Time Complexity: O(n^2)