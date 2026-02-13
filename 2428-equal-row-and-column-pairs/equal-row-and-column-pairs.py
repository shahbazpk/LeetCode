from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_counts = defaultdict(int)

        # Convert each row to a tuple and count frequencies
        for row in grid:
            row_counts[tuple(row)] += 1

        count = 0
        # Iterate through columns
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            
            # Check if the column exists in our row counts
            col_tuple = tuple(col)
            count += row_counts[col_tuple]
        
        return count